# Solução 07 - Repositories e Banco de Dados 🗄️

!!! tip "Navegação"
[← Exercício 07](exercicio-07.md) | [Próxima Solução →](solucao-08.md)

## 🟢 Respostas Fáceis

### 1. Fundamentos - SQL

!!! success "Resposta 1"
**SQL - Structured Query Language:**

    - **Significado**: **S**tructured **Q**uery **L**anguage (Linguagem de Consulta Estruturada)
    - **Finalidade**: Linguagem padrão para **gerenciar e manipular** bancos de dados relacionais

    **🎯 Para que serve:**
    - **Consultar** dados (SELECT)
    - **Inserir** novos registros (INSERT)
    - **Atualizar** dados existentes (UPDATE)
    - **Deletar** registros (DELETE)
    - **Definir** estruturas de tabelas (DDL)
    - **Controlar** acesso e permissões

    **🌍 Universalidade:**
    ```mermaid
    graph TD
        A[SQL Standard] --> B[MySQL]
        A --> C[PostgreSQL]
        A --> D[SQL Server]
        A --> E[Oracle]
        A --> F[SQLite]

        style A fill:#e3f2fd
    ```

### 2. CRUD - Comando INSERT

!!! success "Resposta 2"
**Comando SQL para inserir produto:**

    ```sql
    INSERT INTO produtos (nome, preco)
    VALUES ('Mouse', 50.00);
    ```

    **📝 Variações mais completas:**
    ```sql
    -- Com mais campos
    INSERT INTO produtos (nome, preco, categoria, estoque, data_criacao)
    VALUES ('Mouse', 50.00, 'informatica', 100, NOW());

    -- Inserção múltipla
    INSERT INTO produtos (nome, preco) VALUES
        ('Mouse', 50.00),
        ('Teclado', 150.00),
        ('Monitor', 800.00);

    -- Retornando o ID criado (PostgreSQL)
    INSERT INTO produtos (nome, preco)
    VALUES ('Mouse', 50.00)
    RETURNING id;
    ```

## 🟡 Respostas Médias

### 3. Primary Key vs Foreign Key

!!! warning "Resposta 3"
**Diferenciação PK vs FK:**

    | Aspecto | Primary Key (PK) | Foreign Key (FK) |
    |---------|------------------|------------------|
    | **Função** | **Identifica unicamente** cada registro | **Conecta** com outra tabela |
    | **Valores** | **Únicos** e **não nulos** | Podem repetir e ser nulos |
    | **Quantidade** | **1 por tabela** apenas | **Várias** por tabela |
    | **Relacionamento** | **Lado "um"** (1:N) | **Lado "muitos"** (1:N) |

    **🔗 Por que FK é essencial:**
    - **Integridade referencial**: Garante que dados conectados existam
    - **Consistência**: Evita registros "órfãos"
    - **Relacionamentos**: Permite JOINs eficientes entre tabelas
    - **Cascata**: Controla o que acontece quando PK é deletada

    **📊 Exemplo Prático:**
    ```sql
    -- Tabela PAI (lado "um")
    CREATE TABLE categorias (
        id INT PRIMARY KEY,           -- ← PK
        nome VARCHAR(100)
    );

    -- Tabela FILHA (lado "muitos")
    CREATE TABLE produtos (
        id INT PRIMARY KEY,           -- ← PK desta tabela
        nome VARCHAR(100),
        categoria_id INT,             -- ← FK para categorias
        FOREIGN KEY (categoria_id) REFERENCES categorias(id)
    );
    ```

    **⚡ Benefícios da FK:**
    ```mermaid
    graph TD
        A[Foreign Key] --> B[Integridade Referencial]
        A --> C[Previne Dados Órfãos]
        A --> D[Suporte a JOINs]
        A --> E[Cascata de Operações]

        B --> F[Dados Sempre Consistentes]
        C --> G[Sem Produtos sem Categoria]
        D --> H[Consultas Relacionais Eficientes]
        E --> I[DELETE/UPDATE Automático]
    ```

### 4. Padrão Repository vs SQL Direto

!!! warning "Resposta 4"
**Por que usar Repository em vez de SQL direto no Service:**

    **❌ Problemas do SQL Direto no Service:**
    ```javascript
    // ❌ Service conhece detalhes do banco
    class UsuarioService {
        async buscar(id) {
            const result = await db.query(
                'SELECT * FROM usuarios WHERE id = ? AND deletado_em IS NULL',
                [id]
            );
            // Service precisa saber sobre colunas, SQL, etc.
            return result.rows[0];
        }
    }
    ```

    **✅ Benefícios do Repository:**
    ```javascript
    // ✅ Service foca na regra, Repository no banco
    class UsuarioService {
        async buscar(id) {
            const usuario = await this.usuarioRepository.buscarPorId(id);
            if (!usuario) {
                throw new UsuarioNaoEncontradoError(id);
            }
            return usuario;
        }
    }

    class UsuarioRepository {
        async buscarPorId(id) {
            const result = await this.db.query(
                'SELECT * FROM usuarios WHERE id = ? AND deletado_em IS NULL',
                [id]
            );
            return result.rows[0] ? this.mapearParaEntidade(result.rows[0]) : null;
        }
    }
    ```

    **🎯 Vantagens do Repository:**

    1. **Isolamento de Responsabilidades**:
       - Service: Regras de negócio
       - Repository: Acesso a dados

    2. **Testabilidade**:
       ```javascript
       // Fácil de mockar em testes
       const mockRepository = {
           buscarPorId: jest.fn().mockResolvedValue(usuarioFake)
       };
       ```

    3. **Flexibilidade de Implementação**:
       ```javascript
       // Pode trocar MySQL por MongoDB sem afetar Service
       class UsuarioRepositoryMongo extends UsuarioRepository {
           async buscarPorId(id) {
               return await this.collection.findOne({ _id: id });
           }
       }
       ```

    4. **Reutilização**:
       ```javascript
       // Múltiplos Services usam o mesmo Repository
       class UsuarioService { /* usa UsuarioRepository */ }
       class AuthService { /* usa UsuarioRepository */ }
       class RelatorioService { /* usa UsuarioRepository */ }
       ```

## 🔴 Resposta Desafio

### 5. Modelagem Real - Blog System

!!! danger "Resposta 5"
**Sistema Blog - Escritores e Artigos:**

    **a) Modelagem 1:N (Escritor → Artigos):**
    ```sql
    -- Tabela ESCRITORES (lado "um")
    CREATE TABLE escritores (
        id INT PRIMARY KEY AUTO_INCREMENT,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(150) UNIQUE NOT NULL,
        bio TEXT,
        data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- Tabela ARTIGOS (lado "muitos")
    CREATE TABLE artigos (
        id INT PRIMARY KEY AUTO_INCREMENT,
        titulo VARCHAR(200) NOT NULL,
        conteudo TEXT NOT NULL,
        resumo VARCHAR(500),
        escritor_id INT NOT NULL,               -- ← FK para escritores
        data_publicacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        status ENUM('rascunho', 'publicado', 'arquivado') DEFAULT 'rascunho',

        FOREIGN KEY (escritor_id) REFERENCES escritores(id)
            ON DELETE RESTRICT   -- Não permite deletar escritor com artigos
            ON UPDATE CASCADE    -- Atualiza FK se PK do escritor mudar
    );
    ```

    **b) Query SQL - Artigos do Autor ID 5:**
    ```sql
    SELECT a.titulo
    FROM artigos a
    WHERE a.escritor_id = 5
      AND a.status = 'publicado'    -- Opcional: só publicados
    ORDER BY a.data_publicacao DESC;
    ```

    **📋 Queries Adicionais Úteis:**
    ```sql
    -- Com informações do escritor (JOIN)
    SELECT
        e.nome as escritor,
        a.titulo,
        a.data_publicacao
    FROM artigos a
    INNER JOIN escritores e ON a.escritor_id = e.id
    WHERE e.id = 5
    ORDER BY a.data_publicacao DESC;

    -- Contagem de artigos por escritor
    SELECT
        e.nome,
        COUNT(a.id) as total_artigos
    FROM escritores e
    LEFT JOIN artigos a ON e.id = a.escritor_id
    WHERE e.id = 5
    GROUP BY e.id, e.nome;
    ```

    **c) Assinatura do ArtigoRepository:**
    ```typescript
    interface ArtigoRepository {
        // Busca artigos por escritor
        buscarPorEscritorId(escritorId: number): Promise<Artigo[]>;

        // Versões mais específicas
        buscarPorEscritorIdPublicados(escritorId: number): Promise<Artigo[]>;
        buscarPorEscritorIdComPaginacao(
            escritorId: number,
            page: number,
            limit: number
        ): Promise<{ artigos: Artigo[], total: number }>;

        // Com filtros
        buscarPorEscritorIdComFiltros(
            escritorId: number,
            filtros: {
                status?: 'rascunho' | 'publicado' | 'arquivado';
                dataInicio?: Date;
                dataFim?: Date;
                termoBusca?: string;
            }
        ): Promise<Artigo[]>;
    }
    ```

    **🛠️ Implementação do Repository:**
    ```javascript
    class ArtigoRepository {
        constructor(database) {
            this.db = database;
        }

        async buscarPorEscritorId(escritorId) {
            const query = `
                SELECT
                    a.id,
                    a.titulo,
                    a.conteudo,
                    a.resumo,
                    a.data_publicacao,
                    a.status,
                    e.nome as escritor_nome
                FROM artigos a
                INNER JOIN escritores e ON a.escritor_id = e.id
                WHERE a.escritor_id = ?
                ORDER BY a.data_publicacao DESC
            `;

            const result = await this.db.query(query, [escritorId]);
            return result.rows.map(row => this.mapearParaEntidade(row));
        }

        async buscarPorEscritorIdPublicados(escritorId) {
            const query = `
                SELECT * FROM artigos
                WHERE escritor_id = ?
                  AND status = 'publicado'
                ORDER BY data_publicacao DESC
            `;

            const result = await this.db.query(query, [escritorId]);
            return result.rows.map(row => this.mapearParaEntidade(row));
        }

        async buscarPorEscritorIdComPaginacao(escritorId, page = 1, limit = 10) {
            const offset = (page - 1) * limit;

            // Query para dados
            const queryDados = `
                SELECT * FROM artigos
                WHERE escritor_id = ?
                ORDER BY data_publicacao DESC
                LIMIT ? OFFSET ?
            `;

            // Query para contagem total
            const queryTotal = `
                SELECT COUNT(*) as total
                FROM artigos
                WHERE escritor_id = ?
            `;

            const [resultDados, resultTotal] = await Promise.all([
                this.db.query(queryDados, [escritorId, limit, offset]),
                this.db.query(queryTotal, [escritorId])
            ]);

            return {
                artigos: resultDados.rows.map(row => this.mapearParaEntidade(row)),
                total: resultTotal.rows[0].total,
                page,
                limit,
                totalPages: Math.ceil(resultTotal.rows[0].total / limit)
            };
        }

        // Mapeamento privado para entidade
        mapearParaEntidade(row) {
            return {
                id: row.id,
                titulo: row.titulo,
                conteudo: row.conteudo,
                resumo: row.resumo,
                escritorId: row.escritor_id,
                dataPublicacao: row.data_publicacao,
                status: row.status,
                // Computed properties
                url: `/artigos/${row.id}`,
                palavras: row.conteudo.split(' ').length
            };
        }
    }
    ```

    **📊 Diagrama do Relacionamento:**
    ```mermaid
    erDiagram
        ESCRITORES {
            int id PK
            string nome
            string email UK
            text bio
            timestamp data_cadastro
        }

        ARTIGOS {
            int id PK
            string titulo
            text conteudo
            string resumo
            int escritor_id FK
            timestamp data_publicacao
            enum status
        }

        ESCRITORES ||--o{ ARTIGOS : "escreve"
    ```

    **🧪 Uso no Service:**
    ```javascript
    class ArtigoService {
        constructor(artigoRepository, escritorRepository) {
            this.artigoRepository = artigoRepository;
            this.escritorRepository = escritorRepository;
        }

        async listarArtigosPorEscritor(escritorId, page = 1) {
            // Validar se escritor existe
            const escritor = await this.escritorRepository.buscarPorId(escritorId);
            if (!escritor) {
                throw new EscritorNaoEncontradoError(escritorId);
            }

            // Buscar artigos com paginação
            const resultado = await this.artigoRepository.buscarPorEscritorIdComPaginacao(
                escritorId,
                page,
                10
            );

            return {
                escritor: {
                    nome: escritor.nome,
                    bio: escritor.bio
                },
                ...resultado
            };
        }
    }
    ```

---

!!! tip "Dicas para Próximos Estudos" - Pratique **Normalização** de banco (1NF, 2NF, 3NF) - Configure **Índices** para melhorar performance de JOINs - Implemente **Soft Delete** em vez de DELETE físico - Use **Query Builder** (Knex.js) ou **ORM** (Prisma, TypeORM)

!!! tip "Navegação"
[← Exercício 07](exercicio-07.md) | [Próxima Solução →](solucao-08.md)
