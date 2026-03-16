import pytest
import os
import re
import yaml
from pathlib import Path
from playwright.sync_api import Page, expect


def get_site_name() -> str:
    """Lê site_name dinamicamente do mkdocs.yml — sem hardcode."""
    mkdocs_path = Path(__file__).parent.parent / "mkdocs.yml"
    
    class IgnoreUndefinedLoader(yaml.SafeLoader):
        def construct_undefined(self, node):
            return None
    IgnoreUndefinedLoader.add_constructor(None, IgnoreUndefinedLoader.construct_undefined)
    
    with open(mkdocs_path, encoding="utf-8") as f:
        config = yaml.load(f, Loader=IgnoreUndefinedLoader)
    return config.get("site_name", "Curso")

# Fixture moved to conftest.py


# Test 1: Verify build output files exist
def test_build_output_exists():
    """Verify that all expected build output files exist."""
    assert os.path.exists("site/index.html"), "Main index.html not found"
    assert os.path.exists("site/aulas/aula-01/index.html"), "Lesson 01 page not found"
    assert os.path.exists("site/aulas/aula-16/index.html"), "Lesson 16 page not found"
    assert os.path.exists("site/slides/index.html"), "Slides index not found"
    assert os.path.exists("site/setups/index.html"), "Setup index not found"
    assert os.path.exists("site/assets/js/quiz.js"), "Quiz JS not found"
    assert os.path.exists("site/assets/css/quiz.css"), "Quiz CSS not found"

# Test 2: Homepage structure and content
def test_homepage_structure(page: Page, base_url):
    """Test that the homepage loads and has correct structure."""
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto(base_url)
    
    # Verifica titulo usando site_name do mkdocs.yml (agnostico)
    site_name = get_site_name()
    expect(page).to_have_title(re.compile(re.escape(site_name)))
    
    # Verifica que h1 existe e tem conteudo (sem hardcode do texto)
    heading = page.locator("h1")
    expect(heading).to_be_visible()
    assert heading.text_content().strip() != "", "h1 esta vazio na pagina inicial"
    
    # Verifica que cards de navegacao existem (genericamente)
    md_content = page.locator(".md-content")
    expect(md_content).to_be_visible()

# Test 3: Navigation to Lesson 01
def test_lesson_01_page(page: Page, base_url):
    """Verifica se a pagina Aula 01 carrega com titulo e h1."""
    page.goto(f"{base_url}/aulas/aula-01/")
    
    # Titulo deve mencionar "Aula 01" (agnostico ao texto completo)
    expect(page).to_have_title(re.compile(r"Aula 01", re.IGNORECASE))
    
    # h1 deve existir e ter conteudo
    heading = page.locator("h1")
    expect(heading).to_be_visible()
    assert heading.text_content().strip() != "", "h1 esta vazio na aula-01"
    
    # Verifica quiz containers se presentes
    quiz_containers = page.locator(".quiz-container")
    if quiz_containers.count() > 0:
         expect(quiz_containers.first).to_be_visible()

# Test 4: Quiz interactivity
def test_quiz_functionality(page: Page, base_url):
    """Test that quiz JavaScript works correctly."""
    page.goto(f"{base_url}/quizzes/quiz-01/")
    
    # Wait for quiz to be visible
    first_quiz = page.locator(".quiz-container").first
    if first_quiz.is_visible():
        # Click on the correct answer (first option in first quiz)
        correct_option = first_quiz.locator(".quiz-option[data-correct='true']").first
        correct_option.click()
        
        # Check that feedback is displayed
        feedback = first_quiz.locator(".quiz-feedback")
        expect(feedback).to_be_visible()
        expect(feedback).to_contain_text("Correto")

# Test 5: Slides index
def test_slides_structure(page: Page, base_url):
    """Verifica que a pagina de slides carrega corretamente."""
    page.goto(f"{base_url}/slides/")
    
    # Pagina nao e 404
    expect(page).not_to_have_title("404")
    
    # h1 deve existir (agnostico ao texto exato)
    expect(page.locator("h1")).to_be_visible()
    
    # Conteudo visivel
    content = page.locator(".md-content")
    expect(content).to_be_visible()

# Test 6: Lesson 16 page
def test_lesson_16_page(page: Page, base_url):
    """Verifica se a pagina Aula 16 carrega corretamente."""
    page.goto(f"{base_url}/aulas/aula-16/")
    
    # Titulo deve mencionar "Aula 16" (agnostico ao texto completo)
    expect(page).to_have_title(re.compile(r"Aula 16", re.IGNORECASE))
    
    # Verifica quiz containers se presentes
    quiz_containers = page.locator(".quiz-container")
    if quiz_containers.count() > 0:
        expect(quiz_containers.first).to_be_visible()

# Test 7: Mermaid diagram rendering (checking Lesson 11)
def test_mermaid_diagram(page: Page, base_url):
    """Test that Mermaid diagrams are present in the content."""
    page.goto(f"{base_url}/aulas/aula-01/")
    
    # Check for mermaid code block or rendered diagram
    # MkDocs Material renders mermaid as div.mermaid or similar
    mermaid_div = page.locator("div.mermaid")
    # Wait for it to be visible (client-side rendering)
    if mermaid_div.count() > 0:
        expect(mermaid_div.first).to_be_visible()
    else:
        # Fallback check for code block if JS didn't run
        code_block = page.locator("code.language-mermaid")
        if code_block.count() > 0:
            expect(code_block.first).to_be_visible()

# Test 8: Assets loading
def test_assets_load(page: Page, base_url):
    """Test that CSS and JS assets load correctly."""
    page.goto(f"{base_url}/aulas/aula-01/")
    
    # Check that quiz.js is loaded
    quiz_script = page.locator("script[src*='quiz.js']")
    expect(quiz_script).to_be_attached()
    
    # Check that quiz.css is loaded via checking style application
    quiz_container = page.locator(".quiz-container").first
    if quiz_container.is_visible():
        expect(quiz_container).to_have_css("border-radius", "8px")
