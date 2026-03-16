import os
import re
import json
import sys

def audit_lessons(docs_dir):
    lessons_path = os.path.join(docs_dir, 'aulas')
    if not os.path.exists(lessons_path):
        return {"error": f"Directory not found: {lessons_path}"}

    features = {
        "admonitions": r"!!!\s+\w+",
        "tabs": r"===",
        "annotations": r"\(\d+\)",
        "math": r"\$[^\$]+\$|\\\[.*\\\]",
        "mermaid": r"mermaid",
        "termynal": r"<!--\s*termynal\s*-->",
        "grids": r"grid cards",
        "buttons": r"{\s*\.md-button",
        "tooltips": r"\*\[[^\]]+\]:",
    }

    report = {}
    
    for i in range(1, 17):
        filename = f'aula-{i:02d}.md'
        filepath = os.path.join(lessons_path, filename)
        
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            lesson_results = {}
            for feature, pattern in features.items():
                count = len(re.findall(pattern, content, re.MULTILINE))
                lesson_results[feature] = count
            
            report[filename] = lesson_results
        else:
            report[filename] = "MISSING"

    return report

if __name__ == "__main__":
    docs_directory = sys.argv[1] if len(sys.argv) > 1 else "docs"
    results = audit_lessons(docs_directory)
    
    if "error" in results:
        print(results["error"])
        sys.exit(1)

    # Save to logs directory (relative to script location or current dir)
    logs_dir = os.path.join(os.path.dirname(docs_directory), "logs")
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
        
    with open(os.path.join(logs_dir, 'ui_audit_data.json'), 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
        
    # Generate Markdown Report
    report_md = "# 📋 Relatório de Auditoria de UI (Aulas 01-16)\n\n"
    report_md += "| Aula | Admonitions | Tabs | Annotations | Math | Mermaid | Termynal | Grids | Buttons | Tooltips |\n"
    report_md += "|---|---|---|---|---|---|---|---|---|---|\n"
    
    for filename, data in results.items():
        if data == "MISSING":
            report_md += f"| {filename} | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |\n"
        else:
            report_md += f"| {filename} | {data['admonitions']} | {data['tabs']} | {data['annotations']} | {data['math']} | {data['mermaid']} | {data['termynal']} | {data['grids']} | {data['buttons']} | {data['tooltips']} |\n"
            
    with open(os.path.join(logs_dir, 'ui_audit_report.md'), 'w', encoding='utf-8') as f:
        f.write(report_md)

    print(f"Audit complete. Report generated in {os.path.join(logs_dir, 'ui_audit_report.md')}")
