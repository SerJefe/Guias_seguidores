import glob
import os

# Exclude the index and combined files if they exist
EXCLUDE = {'index.html', 'combined.html'}

html_files = [f for f in glob.glob('*.html') if os.path.basename(f) not in EXCLUDE]
html_files.sort()

# Generate navigation items
nav_items = "\n".join(
    f'<button onclick="loadPage(\'{file}\')" class="px-3 py-2 border rounded mr-2 mb-2">{os.path.splitext(file)[0]}</button>'
    for file in html_files
)

html_template = f"""
<!DOCTYPE html>
<html lang='es'>
<head>
    <meta charset='UTF-8'>
    <title>Contenido Unificado</title>
    <script src='https://cdn.tailwindcss.com'></script>
</head>
<body class='p-4'>
    <nav class='mb-4'>
        {nav_items}
    </nav>
    <iframe id='content-frame' src='{html_files[0] if html_files else ''}' class='w-full h-[80vh] border rounded'></iframe>
    <script>
    function loadPage(page) {{
        document.getElementById('content-frame').src = page;
    }}
    </script>
</body>
</html>
"""

with open('combined.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Combined {len(html_files)} HTML files into combined.html")
