[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LzQtp7yd)


## Proceso para Contribuir al Proyecto

A continuación se describe el proceso para contribuir al proyecto mediante la apertura de una Pull Request (PR):

### 1. Clonar el Repositorio

```bash
git clone https://github.com/ICESI-PI1-2024A-3/ccsa-grupo-2.git
cd ccsa-grupo-2
```

### 2. Crear una Nueva Branch

```bash
git checkout dev
git pull origin dev  # Asegurarse de tener la última versión de dev
git checkout -b feat_nombre_funcionalidad
```

### 3. Trabajar en tu Funcionalidad

Realiza los cambios necesarios en tu branch feat_nombre_funcionalidad, agrega y confirma tus cambios:

```bash
git add .
git commit -m "feat: descripción del cambio realizado" # Ejemplo "feat: add new dashboard template"
```

### 4. Mantener tu Rama Actualizada:

Durante el desarrollo, asegúrate de mantener tu rama actualizada con los últimos cambios de la rama dev:

```bash
git checkout feat_nombre_funcionalidad
git merge dev
```

### 5. Resolver Conflictos en Visual Studio Code:

Si se presentan conflictos durante la fusión, resuélvelos utilizando Visual Studio Code. Abre la vista de "Source Control" para visualizar y resolver los conflictos de manera interactiva.

### 6. Enviar Cambios al Repositorio Remoto:

Una vez resueltos los conflictos y completada la funcionalidad, envía tu rama y cambios al repositorio remoto:

```bash
git push origin feat_nombre_funcionalidad
```

### 7. Abrir una Pull Request en GitHub

- Ve a la página de tu repositorio en GitHub.
- Cambia a la pestaña "Pull Requests".
- Haz clic en "New pull request".
- En el menú desplegable "base", selecciona **dev** como el branch base.
- En el menú desplegable "compare", selecciona **feat_nombre_funcionalidad** como el branch que contiene los cambios.
- Proporciona una descripción clara de los cambios realizados.
- Haz clic en "Create pull request" para abrir la Pull Request.

### 8. Revisión y Fusión de la Pull Request

Otros colaboradores revisarán tu Pull Request y podrán hacer comentarios o solicitar modificaciones. Una vez revisada y aprobada, un colaborador con permisos de fusión puede fusionar la Pull Request utilizando la interfaz de GitHub.
