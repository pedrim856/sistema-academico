# Tutorial de Configuração e Execução do Sistema Acadêmico

Este tutorial guiará você nas etapas que precisam ser realizadas manualmente para colocar o sistema em funcionamento, incluindo a criação do repositório no GitHub, a configuração do banco de dados PostgreSQL e a execução inicial do projeto Django.

---

## 1. Criação do Repositório no GitHub

Para manter seu código versionado e seguro, siga estes passos:

| Passo | Ação | Descrição |
| :--- | :--- | :--- |
| **1** | **Acesse o GitHub** | Entre em sua conta no [GitHub](https://github.com). |
| **2** | **Novo Repositório** | Clique no botão **"+"** no canto superior direito e selecione **"New repository"**. |
| **3** | **Configurações** | Dê o nome de `sistema-academico` (ou o de sua preferência), marque como **Public** ou **Private** e clique em **"Create repository"**. |
| **4** | **Subir o Código** | No seu terminal local, dentro da pasta do projeto, execute os comandos abaixo: |

```bash
git init
git add .
git commit -m "Initial commit - Sistema Acadêmico"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/sistema-academico.git
git push -u origin main
```

---

## 2. Configuração do Banco de Dados PostgreSQL

O projeto está configurado para utilizar o PostgreSQL. Você precisará criar o banco de dados antes de rodar o Django.

| Etapa | Comando/Ação | Observação |
| :--- | :--- | :--- |
| **Criar Banco** | `CREATE DATABASE sistema_academico;` | Execute no terminal do PostgreSQL (`psql` ou via pgAdmin). |
| **Ajustar Settings** | Arquivo `settings.py` | Localize a seção `DATABASES` e insira seu **USER** e **PASSWORD** do PostgreSQL. |

---

## 3. Preparação do Ambiente Local

Siga estes passos para preparar seu computador para rodar o projeto:

1. **Crie um ambiente virtual (venv):**
   ```bash
   python -m venv venv
   ```
2. **Ative o ambiente virtual:**
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 4. Execução do Projeto

Com o banco criado e as dependências instaladas, finalize a configuração:

| Ordem | Comando | O que faz |
| :--- | :--- | :--- |
| **1** | `python manage.py makemigrations core` | Cria os arquivos de migração baseados nos modelos. |
| **2** | `python manage.py migrate` | Cria as tabelas no seu banco de dados PostgreSQL. |
| **3** | `python manage.py createsuperuser` | Cria um usuário administrador para acessar o `/admin`. |
| **4** | `python manage.py runserver` | Inicia o servidor de desenvolvimento. |

Acesse o sistema em: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 5. Dicas Adicionais

- **Admin:** Para cadastrar dados e testar os Inlines, acesse `/admin` com o superusuário criado.
- **Inlines:** Ao editar uma "Instituição de Ensino", você verá os "Cursos" vinculados diretamente na mesma página, conforme solicitado nos requisitos.
- **Página Inicial:** A página inicial lista todos os dados cadastrados em tabelas formatadas com Bootstrap.
