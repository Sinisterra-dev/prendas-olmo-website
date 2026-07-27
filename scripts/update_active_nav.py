import os
import re

ROOT = os.path.dirname(os.path.dirname(__file__))

pages = {
    "index.html": "Inicio",
    os.path.join("mujer", "index.html"): "Mujer",
    os.path.join("hombre", "index.html"): "Hombre",
    os.path.join("colecciones", "index.html"): "Colecciones",
    os.path.join("ofertas", "index.html"): "Ofertas",
    os.path.join("nosotros", "index.html"): "Nosotros",
    os.path.join("contacto", "index.html"): "Contacto",
}


def clean_classes(classes: str) -> str:
    """Quita las clases que indican enlace activo."""
    remove = [
        "text-primary",
        "border-b-2",
        "border-primary",
    ]

    for item in remove:
        classes = re.sub(rf"\b{re.escape(item)}\b", "", classes)

    classes = re.sub(r"\s+", " ", classes).strip()
    return classes


for relative_path, active_page in pages.items():

    filepath = os.path.join(ROOT, relative_path)

    if not os.path.exists(filepath):
        continue

    with open(filepath, encoding="utf-8") as f:
        html = f.read()

    pattern = r'<a([^>]*?)class="([^"]*?)"([^>]*?)>(.*?)</a>'

    def replace(match):

        before = match.group(1)
        classes = match.group(2)
        after = match.group(3)
        text = match.group(4)

        plain_text = re.sub("<.*?>", "", text).strip()

        classes = clean_classes(classes)

        if plain_text == active_page:
            classes += " text-primary border-b-2 border-primary"

        classes = re.sub(r"\s+", " ", classes).strip()

        return f'<a{before}class="{classes}"{after}>{text}</a>'

    html = re.sub(pattern, replace, html, flags=re.DOTALL)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✔ Actualizado: {relative_path}")

print("\nTodo listo 🚀")
