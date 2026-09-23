# Sitio personal de Guillermo Álvarez Sánchez

Sitio estático publicado en [wowito68.github.io](https://wowito68.github.io/), basado en el CV proporcionado por Guillermo y en sus repositorios públicos. El gráfico de contribuciones usa datos públicos de GitHub y se regenera diariamente mediante GitHub Actions.

## Actualizar

Editar `index.html` para actualizar el contenido y `assets/styles.css` para cambiar el diseño. Los cambios en `main` activan el workflow de publicación de GitHub Pages; el gráfico también se actualiza diariamente.

El HTML funciona sin herramientas de compilación. Para verlo localmente: `python3 -m http.server 8000` y abrir `http://localhost:8000`.

## Contenido

- `index.html`: contenido, enlaces, metadatos.
- `assets/styles.css`: presentación adaptable a móvil y escritorio.
- `assets/wave.webp`: recorte de la imagen de referencia proporcionada.
- `assets/snake.svg`: actividad pública actual, con un recorrido animado.
- `scripts/generate_snake.py`: regeneración del gráfico.
- `.github/workflows/pages.yml`: publicación y actualización diaria.

El CV original sirvió como fuente de información y no forma parte de los archivos públicos del sitio.
