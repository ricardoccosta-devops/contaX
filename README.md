# 🏢 ContaX Portal

Portal corporativo desenvolvido em Streamlit para centralizar o acesso a diferentes sistemas e ferramentas da empresa ContaX através de uma interface unificada e moderna.

## 📋 Características

- ✅ Interface moderna e responsiva
- ✅ Navegação por abas configuráveis
- ✅ Logotipo corporativo no cabeçalho
- ✅ Design limpo e profissional
- ✅ Fácil configuração de novas abas
- ✅ Pronto para deploy em Streamlit Cloud, AWS ou GCP

## 🚀 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos

1. **Clone ou baixe o projeto**

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Certifique-se de que o logotipo está no local correto:**
   - O arquivo `contax_logo.png` deve estar em `assets/contax_logo.png`

## 🎯 Como Usar

### Executar Localmente

```bash
streamlit run app.py
```

O portal será aberto automaticamente no navegador em `http://localhost:8501`

### Configurar Abas e URLs

Edite o arquivo `config/urls.py` para adicionar, remover ou modificar as abas:

```python
tabs = {
    "Home": "https://www.contax.com.br",
    "Dashboard Financeiro": "https://app.powerbi.com/view?r=xxxx",
    "Relatórios": "https://drive.google.com/xxxx",
    "Suporte": "https://contax.atlassian.net"
}
```

Basta adicionar novas entradas ao dicionário para criar novas abas.

## 📁 Estrutura do Projeto

```
contax_portal/
├── app.py                 # Aplicação principal Streamlit
├── config/
│   └── urls.py           # Configuração das abas e URLs
├── assets/
│   └── contax_logo.png   # Logotipo da empresa
├── requirements.txt      # Dependências do projeto
└── README.md            # Este arquivo
```

## 🎨 Personalização

### Cores Corporativas

As cores podem ser alteradas no arquivo `app.py`, na seção de constantes:

```python
COLOR_PRIMARY = "#0052CC"      # Azul primário
COLOR_LIGHT_BLUE = "#F4F8FF"  # Azul claro
COLOR_GRAY = "#F7F7F7"        # Cinza suave
COLOR_TEXT = "#333333"        # Cor do texto
```

### Altura do Iframe

A altura padrão dos iframes pode ser ajustada:

```python
IFRAME_HEIGHT = 800  # Altura em pixels
```

## 🌐 Deploy

### Streamlit Cloud

1. Faça upload do projeto para um repositório Git (GitHub, GitLab, etc.)
2. Acesse [Streamlit Cloud](https://streamlit.io/cloud)
3. Conecte seu repositório
4. Configure o arquivo principal como `app.py`
5. Deploy automático!

### Outras Plataformas

O portal pode ser implantado em qualquer plataforma que suporte aplicações Python/Streamlit:
- AWS (EC2, ECS, Lambda)
- Google Cloud Platform (Cloud Run, App Engine)
- Azure (App Service)
- Heroku
- Docker

## 📝 Notas Importantes

- Alguns sites podem bloquear o carregamento em iframes por políticas de segurança (X-Frame-Options). Nesses casos, o portal exibirá uma mensagem de erro e um link para acessar diretamente.
- Para melhor experiência, certifique-se de que as URLs configuradas permitem embedding em iframes.

## 👥 Suporte

Para dúvidas ou sugestões, entre em contato com a equipe de desenvolvimento da ContaX.

---

**ContaX © 2025 – Todos os direitos reservados**

