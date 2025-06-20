# 📒 Projeto Agenda Django

Sistema de agenda de contatos desenvolvido como parte de um curso online de Django.  
Feito para treinar **modelos, views, templates, formulários e rotas** na prática.

---

## 💻 Tecnologias utilizadas

- Python 3.12
- Django 5.2
- SQLite
- HTML5 + CSS3
- Git + GitHub

---

## 📚 Funcionalidades

- ✅ Cadastro de contatos com nome, sobrenome, telefone, e-mail, descrição e categoria.
- ✅ Edição de contatos já cadastrados.
- ✅ Exclusão de contatos com confirmação.
- ✅ Página de detalhes para cada contato.
- ✅ Filtro para mostrar somente contatos ativos (`show=True`).
- ✅ Organização por categorias (Ex: Amigos, Família, etc).
- ✅ Barra de pesquisa funcional.

---

## 🧠 Objetivos do projeto

Este projeto foi desenvolvido como prática para:

- Consolidar conhecimentos em Django
- Aprender a estrutura de um projeto real de backend
- Trabalhar com `CRUD` completo
- Usar templates HTML integrados com formulários Django
- Aprender o uso de `get_object_or_404`, `reverse`, `redirect` e `CSRF token`

---

## ⚙️ Como rodar o projeto localmente

```
git clone https://github.com/seu-usuario/projeto-agenda-django.git
cd projeto-agenda-django
Crie e ative o ambiente virtual:

python -m venv venv
venv\Scripts\activate  # Windows
Instale as dependências:

pip install -r requirements.txt
Execute as migrações e rode o servidor:

python manage.py migrate
python manage.py runserver
```
