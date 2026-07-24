import os, glob, re

seo_base = """
    <!-- SEO & Meta Tags -->
    <meta name="description" content="{description}">
    <meta name="keywords" content="moda, ropa, mujer, hombre, alta costura, Prendas Olmo, Palmira, Valle del Cauca, Colombia, diseño exclusivo, {extra_keywords}">
    <meta name="author" content="Alexander Sinisterra (sinisterradev)">
    <link rel="author" href="https://sinisterradev.com">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:site_name" content="Prendas Olmo">
    <meta property="og:locale" content="es_CO">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:title" content="{title}">
    <meta property="twitter:description" content="{description}">
    <meta name="twitter:creator" content="@sinisterradev">

    <!-- JSON-LD Structured Data -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "Prendas Olmo",
      "description": "{description}",
      "publisher": {
        "@type": "Organization",
        "name": "Prendas Olmo",
        "location": {
          "@type": "Place",
          "address": {
            "@type": "PostalAddress",
            "addressLocality": "Palmira",
            "addressRegion": "Valle del Cauca",
            "addressCountry": "CO"
          }
        }
      },
      "developer": {
        "@type": "Person",
        "name": "Alexander Sinisterra",
        "alternateName": "sinisterradev",
        "url": "https://sinisterradev.com",
        "jobTitle": ["Python Developer", "Data Analyst"],
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "Palmira",
          "addressRegion": "Valle del Cauca",
          "addressCountry": "CO"
        }
      }
    }
    </script>
"""

pages_info = {
    'index.html': {
        'title': 'Prendas Olmo | Viste con Estilo',
        'description': 'Descubre Prendas Olmo: Moda premium y alta costura para mujer y hombre. Diseños exclusivos y calidad inigualable desde Palmira, Valle del Cauca, Colombia.',
        'extra_keywords': 'tienda de ropa, estilo, tendencias'
    },
    'mujer.html': {
        'title': 'Moda Femenina | Prendas Olmo',
        'description': 'Explora nuestra colección de moda femenina en Prendas Olmo. Vestidos de lino, blazers y prendas de alta costura para la mujer moderna en Palmira, Colombia.',
        'extra_keywords': 'ropa de mujer, vestidos, blazers femeninos, moda femenina'
    },
    'hombre.html': {
        'title': 'Moda Masculina | Prendas Olmo',
        'description': 'Descubre la colección para hombre de Prendas Olmo. Ropa masculina de lujo, diseño contemporáneo y máxima calidad. Palmira, Valle del Cauca.',
        'extra_keywords': 'ropa de hombre, moda masculina, trajes, lujo'
    },
    'colecciones.html': {
        'title': 'Colecciones | Prendas Olmo',
        'description': 'Nuevas colecciones de Prendas Olmo. Ropa de diseño atemporal y sostenible. Conoce nuestras últimas novedades en moda desde Palmira.',
        'extra_keywords': 'nuevas colecciones, temporada, moda sostenible, novedades'
    },
    'ofertas.html': {
        'title': 'Ofertas | Prendas Olmo',
        'description': 'Encuentra las mejores ofertas y ediciones limitadas en Prendas Olmo. Ropa de alta calidad a precios excepcionales.',
        'extra_keywords': 'ofertas, descuentos, rebajas, ropa barata'
    },
    'nosotros.html': {
        'title': 'Nosotros | Prendas Olmo',
        'description': 'Conoce más sobre Prendas Olmo, nuestra historia, procesos sostenibles y el equipo detrás de la moda de alta costura en Palmira, Colombia.',
        'extra_keywords': 'sobre nosotros, historia, sostenibilidad, Palmira'
    }
}

files = glob.glob('*.html') + glob.glob('pages/*.html')

for file in files:
    filename = os.path.basename(file)
    info = pages_info.get(filename, pages_info['index.html'])
    
    seo_content = seo_base.format(
        title=info['title'],
        description=info['description'],
        extra_keywords=info['extra_keywords']
    )
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Avoid duplicate injection
    if '<!-- SEO & Meta Tags -->' not in content:
        # insert right before </head>
        content = content.replace('</head>', seo_content + '\n</head>')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Injected SEO into {file}")
    else:
        print(f"SEO already present in {file}")

