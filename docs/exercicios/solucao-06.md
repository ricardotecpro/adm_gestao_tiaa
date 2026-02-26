# Solução 06 - Services e Regras de Negócio 🧠

!!! tip "Navegação"
[← Exercício 06](exercicio-06.md) | [Próxima Solução →](solucao-07.md)

## 🟢 Respostas Fáceis

### 1. Lógica fora do Controller

!!! success "Resposta 1"
**Por que não colocar lógica no Controller:**

    **❌ Problemas da Lógica no Controller:**
    - **Responsabilidade única violada**: Controller vira "faz-tudo"
    - **Reutilização impossível**: Lógica presa a uma rota específica
    - **Testes complexos**: Precisa mockar HTTP para testar regra de negócio
    - **Manutenção difícil**: Mudança de regra afeta estrutura da API

    **✅ Controller deve apenas:**
    ```javascript
    // ✅ Controller limpo e focado
    async function criarUsuario(req, res) {
        try {
            const usuario = await usuarioService.criar(req.body);
            return res.status(201).json(usuario);
        } catch (error) {
            return handleError(error, res);
        }
    }
    ```

    **🏗️ Separação de Responsabilidades:**
    ```mermaid
    graph TD
        A[Controller] --> B[Receber Requisição]
        A --> C[Validar Entrada]
        A --> D[Chamar Service]
        A --> E[Formatar Resposta]

        F[Service] --> G[Regras de Negócio]
        F --> H[Validações Complexas]
        F --> I[Orquestração]
        F --> J[Transformações]

        style A fill:#e3f2fd
        style F fill:#fff3e0
    ```

### 2. Tarefas da Camada Service

!!! success "Resposta 2"
**3 Exemplos de Tarefas do Service:**

    1. **Validações Complexas de Negócio**:
       ```javascript
       // Regra: Cliente VIP tem desconto especial
       validarDescontoVIP(cliente, valorPedido) {
           return cliente.tipo === 'VIP' && valorPedido > 1000;
       }
       ```

    2. **Cálculos e Transformações**:
       ```javascript
       // Calcular valor final com impostos e descontos
       calcularValorFinal(itens, descontos, regiao) {
           const subtotal = itens.reduce((acc, item) => acc + item.total, 0);
           const desconto = this.aplicarDescontos(subtotal, descontos);
           const impostos = this.calcularImpostos(subtotal, regiao);
           return subtotal - desconto + impostos;
       }
       ```

    3. **Orquestração de Múltiplos Repositories**:
       ```javascript
       // Coordena operações em diferentes entidades
       async transferirSaldo(origemId, destinoId, valor) {
           await this.contaRepository.debitar(origemId, valor);
           await this.contaRepository.creditar(destinoId, valor);
           await this.transacaoRepository.registrar(origemId, destinoId, valor);
       }
       ```

## 🟡 Respostas Médias

### 3. Tratamento de Erros no Service

!!! warning "Resposta 3"
**Por que Service lança erro em vez de retornar Status Code:**

    **🎯 Separação de Responsabilidades:**
    - **Service**: Responsável por **lógica de negócio**
    - **Controller**: Responsável por **protocolo HTTP**

    ```javascript
    // ❌ Service não deve conhecer HTTP
    class UsuarioService {
        async buscar(id) {
            const usuario = await this.repository.buscarPorId(id);
            if (!usuario) {
                return { status: 404, message: 'Not found' }; // ❌ ERRADO!
            }
            return usuario;
        }
    }

    // ✅ Service foca na regra, Controller no HTTP
    class UsuarioService {
        async buscar(id) {
            const usuario = await this.repository.buscarPorId(id);
            if (!usuario) {
                throw new UsuarioNaoEncontradoError(`Usuário ${id} não existe`);
            }
            return usuario;
        }
    }

    class UsuarioController {
        async buscar(req, res) {
            try {
                const usuario = await this.service.buscar(req.params.id);
                return res.status(200).json(usuario);
            } catch (error) {
                if (error instanceof UsuarioNaoEncontradoError) {
                    return res.status(404).json({ erro: error.message });
                }
                return res.status(500).json({ erro: 'Erro interno' });
            }
        }
    }
    ```

    **🔄 Benefícios:**
    - **Reutilização**: Service usado em Web, CLI, Jobs sem mudanças
    - **Testabilidade**: Testa regra de negócio sem HTTP
    - **Flexibilidade**: Mesmo erro pode virar diferentes status codes

### 4. Reutilização do EmailService

!!! warning "Resposta 4"
**Controllers que usariam EmailService:**

    **1. AuthController** - Autenticação:
    ```javascript
    class AuthController {
        async registrar(req, res) {
            const usuario = await this.usuarioService.criar(req.body);
            // Enviar e-mail de boas-vindas
            await this.emailService.enviarBoasVindas(usuario.email, usuario.nome);
            return res.status(201).json(usuario);
        }

        async resetarSenha(req, res) {
            const { email } = req.body;
            const token = await this.authService.gerarTokenReset(email);
            // Enviar e-mail com link de reset
            await this.emailService.enviarResetSenha(email, token);
            return res.status(200).json({ sucesso: true });
        }
    }
    ```

    **2. PedidoController** - E-commerce:
    ```javascript
    class PedidoController {
        async finalizar(req, res) {
            const pedido = await this.pedidoService.finalizar(req.body);
            // Enviar confirmação de pedido
            await this.emailService.enviarConfirmacaoPedido(
                pedido.cliente.email,
                pedido
            );
            return res.status(201).json(pedido);
        }

        async atualizar(req, res) {
            const pedido = await this.pedidoService.atualizarStatus(req.params.id, req.body);
            if (pedido.status === 'enviado') {
                // Enviar código de rastreamento
                await this.emailService.enviarCodigoRastreamento(
                    pedido.cliente.email,
                    pedido.codigoRastreamento
                );
            }
            return res.status(200).json(pedido);
        }
    }
    ```

## 🔴 Resposta Desafio

### 5. PedidoService.finalizar() - Pseudocódigo

!!! danger "Resposta 5"
**Implementação Completa com Validações:**

    ```javascript
    class PedidoService {
        async finalizar(pedidoId) {
            // 1. BUSCAR E VALIDAR PEDIDO
            const pedido = await this.pedidoRepository.buscarPorId(pedidoId);
            if (!pedido) {
                throw new PedidoNaoEncontradoError(`Pedido ${pedidoId} não existe`);
            }

            if (pedido.status !== 'carrinho') {
                throw new PedidoJaFinalizadoError(
                    `Pedido ${pedidoId} já foi finalizado (status: ${pedido.status})`
                );
            }

            // 2. VALIDAR CLIENTE
            const cliente = await this.clienteRepository.buscarPorId(pedido.clienteId);
            if (!cliente.ativo) {
                throw new ClienteInativoError(`Cliente ${cliente.id} está inativo`);
            }

            // 3. VALIDAR ESTOQUE E COLETAR ITENS
            const itensValidados = [];
            for (const item of pedido.itens) {
                const produto = await this.produtoRepository.buscarPorId(item.produtoId);

                if (!produto) {
                    throw new ProdutoNaoEncontradoError(`Produto ${item.produtoId} não existe`);
                }

                if (produto.estoque < item.quantidade) {
                    throw new EstoqueInsuficienteError(
                        `Produto ${produto.nome} tem apenas ${produto.estoque} unidades, solicitado: ${item.quantidade}`
                    );
                }

                itensValidados.push({
                    ...item,
                    produto,
                    valorUnitario: produto.preco
                });
            }

            // 4. CALCULAR TOTAIS
            const subtotal = itensValidados.reduce(
                (acc, item) => acc + (item.valorUnitario * item.quantidade), 0
            );

            const desconto = await this.calculadoraDescontoService.calcular(cliente, itensValidados);
            const frete = await this.calculadoraFreteService.calcular(cliente.endereco, itensValidados);
            const impostos = this.calculadoraImpostosService.calcular(subtotal, cliente.endereco.estado);

            const valorTotal = subtotal - desconto + frete + impostos;

            // 5. VALIDAR LIMITE DE CRÉDITO
            if (cliente.limiteCreditoDisponivel < valorTotal) {
                throw new LimiteCreditoExcedidoError(
                    `Limite insuficiente. Disponível: R$ ${cliente.limiteCreditoDisponivel}, Necessário: R$ ${valorTotal}`
                );
            }

            // 6. INICIAR TRANSAÇÃO (atomicidade)
            const transaction = await this.database.beginTransaction();

            try {
                // 7. RESERVAR ESTOQUE
                for (const item of itensValidados) {
                    await this.produtoRepository.reduzirEstoque(
                        item.produtoId,
                        item.quantidade,
                        transaction
                    );
                }

                // 8. ATUALIZAR PEDIDO
                const pedidoFinalizado = await this.pedidoRepository.finalizar({
                    id: pedidoId,
                    status: 'processando',
                    subtotal,
                    desconto,
                    frete,
                    impostos,
                    valorTotal,
                    dataFinalizacao: new Date(),
                    itens: itensValidados
                }, transaction);

                // 9. REGISTRAR MOVIMENTAÇÃO FINANCEIRA
                await this.financeiroRepository.registrarDebito(
                    cliente.id,
                    valorTotal,
                    `Pedido ${pedidoId}`,
                    transaction
                );

                // 10. COMMIT DA TRANSAÇÃO
                await transaction.commit();

                // 11. PROCESSOS ASSÍNCRONOS (PÓS-COMMIT)
                this.eventBus.publish('pedido.finalizado', {
                    pedidoId: pedidoFinalizado.id,
                    clienteId: cliente.id,
                    valorTotal
                });

                // 12. RETORNAR DTO PARA O CONTROLLER
                return {
                    id: pedidoFinalizado.id,
                    numero: pedidoFinalizado.numero,
                    status: pedidoFinalizado.status,
                    cliente: {
                        nome: cliente.nome,
                        email: cliente.email
                    },
                    itens: itensValidados.map(item => ({
                        produto: item.produto.nome,
                        quantidade: item.quantidade,
                        valorUnitario: item.valorUnitario,
                        subtotal: item.valorUnitario * item.quantidade
                    })),
                    resumoFinanceiro: {
                        subtotal,
                        desconto,
                        frete,
                        impostos,
                        valorTotal
                    },
                    dataFinalizacao: pedidoFinalizado.dataFinalizacao,
                    estimativaEntrega: await this.logisticaService.calcularEstimativaEntrega(
                        cliente.endereco
                    )
                };

            } catch (error) {
                await transaction.rollback();
                throw error;
            }
        }

        // TRATAMENTO DO ERRO "Produto Sem Estoque"
        async tratarEstoqueInsuficiente(pedidoId, produtoId) {
            // Opções disponíveis:

            // 1. Remover item do pedido
            await this.removerItemDoPedido(pedidoId, produtoId);

            // 2. Reduzir quantidade para disponível
            const estoque = await this.produtoRepository.obterEstoque(produtoId);
            if (estoque > 0) {
                await this.atualizarQuantidadeItem(pedidoId, produtoId, estoque);
            }

            // 3. Sugerir produtos similares
            const similares = await this.produtoRepository.buscarSimilares(produtoId);
            return {
                acao: 'estoque_insuficiente',
                produtoOriginal: produtoId,
                estoqueDisponivel: estoque,
                produtosSimilares: similares
            };
        }
    }
    ```

    **🎯 DTO de Retorno para o Controller:**
    ```typescript
    interface PedidoFinalizadoDTO {
        id: number;
        numero: string;
        status: 'processando';
        cliente: {
            nome: string;
            email: string;
        };
        itens: ItemPedidoDTO[];
        resumoFinanceiro: {
            subtotal: number;
            desconto: number;
            frete: number;
            impostos: number;
            valorTotal: number;
        };
        dataFinalizacao: Date;
        estimativaEntrega: Date;
    }
    ```

    **🚨 Tratamento de "Produto Sem Estoque":**
    ```mermaid
    flowchart TD
        A[Validar Estoque] --> B{Estoque >= Quantidade?}
        B -->|Sim| C[Continuar Processamento]
        B -->|Não| D[EstoqueInsuficienteError]

        D --> E[Controller Captura Erro]
        E --> F[Status 409 Conflict]
        F --> G[Retornar Opções ao Cliente]

        G --> H[1. Remover Item]
        G --> I[2. Reduzir Quantidade]
        G --> J[3. Produtos Similares]
        G --> K[4. Aguardar Reestoque]

        style D fill:#ff6b6b
        style F fill:#ffa726
    ```

---

!!! tip "Dicas para Próximos Estudos" - Implemente **Domain Driven Design (DDD)** para regras complexas - Use **Events** para desacoplar processos assíncronos - Pratique **Transaction Scripts** vs **Domain Model** patterns - Configure **Circuit Breakers** para serviços externos

!!! tip "Navegação"
[← Exercício 06](exercicio-06.md) | [Próxima Solução →](solucao-07.md)
