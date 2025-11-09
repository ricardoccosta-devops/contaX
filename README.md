# ContaX - Website com Integração LLM

Website da empresa ContaX - Soluções Contábeis Inteligentes com tecnologia de Inteligência Artificial.

## 🚀 Características

- **Website Responsivo**: Interface moderna e responsiva construída com Flask
- **Integração LLM**: Assistente virtual inteligente usando OpenAI GPT-3.5
- **Chat em Tempo Real**: Suporte 24/7 através de chatbot com IA
- **Design Moderno**: Interface clean e profissional
- **Múltiplas Páginas**: Início, Sobre, Serviços e Contato

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Conta OpenAI (opcional, para funcionalidade completa do chatbot)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/ricardoccosta-devops/contaX.git
cd contaX
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Configure as variáveis de ambiente:
```bash
cp .env.example .env
```

Edite o arquivo `.env` e configure suas chaves:
- `OPENAI_API_KEY`: Sua chave de API do OpenAI (opcional)
- `FLASK_SECRET_KEY`: Uma chave secreta para o Flask
- `FLASK_ENV`: development ou production

## ▶️ Executando o Projeto

1. Certifique-se de que o ambiente virtual está ativado

2. Execute a aplicação:
```bash
python app.py
```

3. Acesse no navegador:
```
http://localhost:5000
```

## 🐳 Docker (Opcional)

Se preferir usar Docker:

```bash
docker build -t contax .
docker run -p 5000:5000 --env-file .env contax
```

## 📁 Estrutura do Projeto

```
contaX/
├── app.py                 # Aplicação Flask principal
├── requirements.txt       # Dependências Python
├── .env.example          # Exemplo de variáveis de ambiente
├── .gitignore           # Arquivos ignorados pelo Git
├── README.md            # Este arquivo
├── templates/           # Templates HTML
│   ├── base.html       # Template base
│   ├── index.html      # Página inicial
│   ├── about.html      # Página sobre
│   ├── services.html   # Página de serviços
│   └── contact.html    # Página de contato
└── static/             # Arquivos estáticos
    ├── css/
    │   └── style.css   # Estilos CSS
    └── js/
        ├── main.js     # JavaScript principal
        └── chat.js     # Funcionalidade do chat
```

## 🤖 Funcionalidade LLM

O assistente virtual utiliza a API do OpenAI (GPT-3.5-turbo) para responder perguntas sobre:
- Serviços contábeis
- Informações fiscais
- Dúvidas sobre a empresa
- Orientações gerais sobre contabilidade

### Modo Demo
Se a chave da API do OpenAI não estiver configurada, o chat funcionará em modo demo com uma mensagem padrão.

## 🔒 Segurança

- Nunca commit suas chaves de API (já configurado no .gitignore)
- Use variáveis de ambiente para informações sensíveis
- Mantenha o Flask em modo de produção quando em deploy

## 🛠️ Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **IA**: OpenAI GPT-3.5 Turbo
- **Estilo**: CSS customizado

## 📝 Licença

Este projeto é de código fechado e pertence à ContaX.

## 👥 Suporte

Para suporte, envie um email para contato@contax.com.br ou use nosso assistente virtual no website.

## 🚀 Deploy

### Heroku

```bash
heroku create contax-app
heroku config:set OPENAI_API_KEY=sua_chave_aqui
heroku config:set FLASK_SECRET_KEY=sua_chave_secreta_aqui
git push heroku main
```

### Render/Railway/Vercel

Configure as variáveis de ambiente no painel de controle da plataforma escolhida.

## 📊 Próximas Funcionalidades

- [ ] Sistema de autenticação de usuários
- [ ] Dashboard para clientes
- [ ] Integração com sistemas contábeis
- [ ] Chatbot multilíngue
- [ ] Análise de documentos com IA
- [ ] Relatórios automáticos

## 🤝 Contribuindo

Este é um projeto privado. Contribuições são restritas à equipe interna.
