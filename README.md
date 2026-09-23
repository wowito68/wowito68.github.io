# Sitio personal de Guillermo Álvarez Sánchez

Sitio estático para `https://wowito68.github.io`, basado en el CV proporcionado por Guillermo. El gráfico de contribuciones usa datos públicos de GitHub y se regenera diariamente mediante GitHub Actions.

## Publicar

1. Crear en la cuenta `wowito68` un repositorio público llamado exactamente `wowito68.github.io`.
2. Subir **el contenido de esta carpeta** a la rama `main` del repositorio (incluidas las carpetas ocultas `.github` y el archivo `.nojekyll`).
3. En **Settings → Pages → Build and deployment → Source**, seleccionar **GitHub Actions**.
4. En **Actions**, ejecutar el workflow **Publicar sitio y actualizar actividad** si no arranca tras el primer push. Al terminar, abrir `https://wowito68.github.io`.

Para subirlo desde una terminal con Git autenticado, ejecuta dentro de esta carpeta:

```bash
git init
git branch -M main
git add .
git commit -m "Publicar sitio personal"
git remote add origin https://github.com/wowito68/wowito68.github.io.git
git push -u origin main
```

El HTML funciona sin herramientas de compilación. Para verlo localmente: `python3 -m http.server 8000` y abrir `http://localhost:8000`.

## Contenido

- `index.html`: contenido, enlaces, metadatos.
- `assets/styles.css`: presentación adaptable a móvil y escritorio.
- `assets/wave.webp`: recorte de la imagen de referencia proporcionada.
- `assets/snake.svg`: actividad pública actual, con un recorrido animado.
- `scripts/generate_snake.py`: regeneración del gráfico.
- `.github/workflows/pages.yml`: publicación y actualización diaria.

El CV original sirvió como fuente de información y no forma parte de los archivos públicos del sitio.
