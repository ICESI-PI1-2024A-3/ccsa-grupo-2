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

### 4. Fusionar los Cambios en dev

Antes de abrir una Pull Request, asegúrate de tener los últimos cambios de la branch dev:

```bash
git checkout dev
git pull origin dev
```

Fusiona tus cambios en la branch dev:

```bash
git merge feat_nombre_funcionalidad
```

### 5. Enviar Cambios al Repositorio Remoto

Envía tu branch y cambios al repositorio remoto:

```bash
git push origin feat_nombre_funcionalidad
```

### 6. Abrir una Pull Request en GitHub

- Ve a la página de tu repositorio en GitHub.
- Cambia a la pestaña "Pull Requests".
- Haz clic en "New pull request".
- En el menú desplegable "base", selecciona **dev** como el branch base.
- En el menú desplegable "compare", selecciona **feat_nombre_funcionalidad** como el branch que contiene los cambios.
- Proporciona una descripción clara de los cambios realizados.
- Haz clic en "Create pull request" para abrir la Pull Request.

### 7. Revisión y Fusión de la Pull Request

Otros colaboradores revisarán tu Pull Request y podrán hacer comentarios o solicitar modificaciones. Una vez revisada y aprobada, un colaborador con permisos de fusión puede fusionar la Pull Request utilizando la interfaz de GitHub.
