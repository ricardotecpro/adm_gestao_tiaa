"""
Testes automatizados para navegação do site — AGNOSTICOS
Lê site_name e labels do mkdocs.yml dinamicamente para evitar hardcodes.
"""
import pytest
import re
import yaml
from pathlib import Path
from playwright.sync_api import Page, expect


def load_mkdocs_config(path: Path):
    """Carrega o mkdocs.yml ignorando tags desconhecidas (como !!python/name)."""
    class IgnoreUndefinedLoader(yaml.SafeLoader):
        def construct_undefined(self, node):
            return None
    
    IgnoreUndefinedLoader.add_constructor(None, IgnoreUndefinedLoader.construct_undefined)
    
    with open(path, encoding="utf-8") as f:
        return yaml.load(f, Loader=IgnoreUndefinedLoader)


def get_site_name() -> str:
    """Lê site_name dinamicamente do mkdocs.yml — sem hardcode."""
    mkdocs_path = Path(__file__).parent.parent / "mkdocs.yml"
    config = load_mkdocs_config(mkdocs_path)
    return config.get("site_name", "Curso")


def get_nav_tabs() -> list:
    """Retorna os nomes das abas de nível superior do nav no mkdocs.yml."""
    mkdocs_path = Path(__file__).parent.parent / "mkdocs.yml"
    config = load_mkdocs_config(mkdocs_path)
    nav = config.get("nav", [])
    tabs = []
    for entry in nav:
        if isinstance(entry, dict):
            tabs.extend(entry.keys())
    return tabs


class TestNavigation:
    """Testes para navegação do site — agnosticos ao conteudo."""

    def test_home_page_loads(self, page_with_base_url: Page, base_url: str):
        """Verifica se a página inicial carrega com o site_name correto."""
        page = page_with_base_url
        page.goto(base_url)

        site_name = get_site_name()
        expect(page).to_have_title(re.compile(re.escape(site_name)))

    def _ensure_menu_visible(self, page: Page):
        """Helper to ensure menu is visible (opens drawer if needed)."""
        drawer_button = page.locator("label.md-header__button[for='__drawer']")
        if drawer_button.is_visible():
            drawer_button.click()

    def test_nav_tabs_exist(self, page_with_base_url: Page, base_url: str):
        """Verifica se as abas do nav definidas no mkdocs.yml existem na pagina."""
        page = page_with_base_url
        page.goto(base_url)

        self._ensure_menu_visible(page)

        # Verifica a presença das abas principais (4 tabs: Principal, Aulas, Materiais, Impressão)
        tabs = get_nav_tabs()
        for tab in tabs:
            link = page.get_by_role("link", name=tab).first
            expect(link).to_be_attached()

    def test_aulas_tab_exists(self, page_with_base_url: Page, base_url: str):
        """Verifica se a aba 'Aulas' existe no menu."""
        page = page_with_base_url
        page.goto(base_url)

        self._ensure_menu_visible(page)
        link = page.get_by_role("link", name="Aulas").first
        expect(link).to_be_visible()

    def test_print_version_link_exists(self, page_with_base_url: Page, base_url: str):
        """Verifica se o link de impressão existe na page."""
        page = page_with_base_url
        page.goto(base_url)

        print_link = page.locator("a[href*='print_page']")
        expect(print_link.first).to_be_attached()

    def test_navigation_to_lesson_01(self, page_with_base_url: Page, base_url: str):
        """Verifica se e possivel navegar para a pagina da Aula 01."""
        page = page_with_base_url
        page.goto(base_url)

        self._ensure_menu_visible(page)

        # Clica na aba Aulas
        page.get_by_role("link", name="Aulas").first.click(force=True)

        # Navega para aula-01 diretamente pela URL — sem hardcode de label
        page.goto(f"{base_url}/aulas/aula-01/")

        # Verifica que a URL bateu na pagina correta
        expect(page).to_have_url(re.compile(r".*/aulas/aula-01/?$"))

        # Verifica que h1 existe e tem conteudo (sem hardcode do texto)
        heading = page.locator("h1")
        expect(heading).to_be_visible()
        assert heading.text_content().strip() != "", "h1 esta vazio na aula-01"
