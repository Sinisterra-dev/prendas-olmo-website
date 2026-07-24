import os
import re
import shutil

# Rutas de origen y destino
pages_dir = 'pages'
folders = ['mujer', 'hombre', 'colecciones', 'ofertas', 'nosotros', 'contacto']

def replace_links_in_content(content, is_root=False):
    if is_root:
        # En index.html root
        content = re.sub(r'href=[\'"]pages/mujer\.html[\'"]', 'href="mujer/"', content)
        content = re.sub(r'href=[\'"]pages/hombre\.html[\'"]', 'href="hombre/"', content)
        content = re.sub(r'href=[\'"]pages/colecciones\.html[\'"]', 'href="colecciones/"', content)
        content = re.sub(r'href=[\'"]pages/ofertas\.html[\'"]', 'href="ofertas/"', content)
        content = re.sub(r'href=[\'"]pages/nosotros\.html[\'"]', 'href="nosotros/"', content)
        content = re.sub(r'href=[\'"]#contacto[\'"]', 'href="contacto/"', content)
        content = re.sub(r'href=[\'"]index\.html#contacto[\'"]', 'href="contacto/"', content)
        content = re.sub(r'href=[\'"]index\.html[\'"]', 'href="/"', content)
    else:
        # En las subpáginas
        content = re.sub(r'href=[\'"]mujer\.html[\'"]', 'href="../mujer/"', content)
        content = re.sub(r'href=[\'"]hombre\.html[\'"]', 'href="../hombre/"', content)
        content = re.sub(r'href=[\'"]colecciones\.html[\'"]', 'href="../colecciones/"', content)
        content = re.sub(r'href=[\'"]ofertas\.html[\'"]', 'href="../ofertas/"', content)
        content = re.sub(r'href=[\'"]nosotros\.html[\'"]', 'href="../nosotros/"', content)
        content = re.sub(r'href=[\'"]\.\./index\.html#contacto[\'"]', 'href="../contacto/"', content)
        content = re.sub(r'href=[\'"]\.\./index\.html[\'"]', 'href="../"', content)
        content = re.sub(r'href=[\'"]index\.html[\'"]', 'href="../"', content)
        
    return content

# 1. Crear las carpetas
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# 2. Mover archivos y actualizar enlaces (excepto contacto que se creará de otra forma)
for page in ['mujer', 'hombre', 'colecciones', 'ofertas', 'nosotros']:
    src_file = os.path.join(pages_dir, f'{page}.html')
    if os.path.exists(src_file):
        with open(src_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update internal links
        new_content = replace_links_in_content(content, is_root=False)
        
        # Guardar en la nueva ubicación
        dest_file = os.path.join(page, 'index.html')
        with open(dest_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        # Borrar el original
        os.remove(src_file)

# 3. Crear contacto/index.html a partir de nosotros (como plantilla) y la seccion contacto de index.html
# Primero leemos index.html
with open('index.html', 'r', encoding='utf-8') as f:
    root_content = f.read()

# Extraemos la seccion de contacto de index.html
contacto_match = re.search(r'(<section id="contacto".*?</section>)', root_content, re.DOTALL)
if contacto_match and os.path.exists('nosotros/index.html'):
    contacto_section = contacto_match.group(1)
    # Remove the section from root_content? The user said "sin modificar el diseño ni el comportamiento". 
    # Mmm, si quito la seccion contacto del index, cambia el diseño del index. 
    # Mejor lo dejo en el index, pero la navegacion ira a /contacto/ que tendra esta misma seccion.
    # O quizas solo saco la seccion y actualizo el form. 
    # Vamos a usar 'nosotros/index.html' como base para construir contacto/index.html
    with open('nosotros/index.html', 'r', encoding='utf-8') as f:
        nosotros_content = f.read()
        
    # Reemplazar el main tag completo en nosotros_content con la seccion de contacto
    # O buscar algo como <main ...> ... </main>
    main_match = re.search(r'(<main.*?>).*?(</main>)', nosotros_content, re.DOTALL)
    if main_match:
        # Reemplazamos todo dentro del main por la seccion contacto
        contacto_main = f"{main_match.group(1)}\n{contacto_section}\n{main_match.group(2)}"
        contacto_content = nosotros_content[:main_match.start()] + contacto_main + nosotros_content[main_match.end():]
        # Cambiamos titulo y otras cositas si es necesario
        contacto_content = re.sub(r'<title>.*?Nosotros.*?</title>', '<title>Prendas Olmo - Contacto</title>', contacto_content)
        with open('contacto/index.html', 'w', encoding='utf-8') as f:
            f.write(contacto_content)

# 4. Actualizar index.html root
new_root_content = replace_links_in_content(root_content, is_root=True)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_root_content)

# 5. Intentar borrar pages_dir si esta vacio
try:
    os.rmdir(pages_dir)
except OSError:
    pass # Quiza queden otros archivos, no importa

# 6. Actualizar SEO: robots.txt y sitemap.xml
if os.path.exists('sitemap.xml'):
    with open('sitemap.xml', 'r', encoding='utf-8') as f:
        sitemap = f.read()
    sitemap = sitemap.replace('pages/mujer.html', 'mujer/')
    sitemap = sitemap.replace('pages/hombre.html', 'hombre/')
    sitemap = sitemap.replace('pages/colecciones.html', 'colecciones/')
    sitemap = sitemap.replace('pages/ofertas.html', 'ofertas/')
    sitemap = sitemap.replace('pages/nosotros.html', 'nosotros/')
    # Añadir contacto si no estaba
    if 'contacto' not in sitemap:
        new_url = '''  <url>
    <loc>https://tudominio.com/contacto/</loc>
    <lastmod>2023-11-20</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
</urlset>'''
        sitemap = sitemap.replace('</urlset>', new_url)
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
        
print("Reorganización completada")
