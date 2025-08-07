# 📚 Virtual Bookstore - Interactive Chat

An interactive chat application for a virtual bookstore built with Streamlit and Pydantic AI

<p>
    <img width="300" src="extras/imagens/screenshot.png" alt="Virtual Bookstore Screenshot">
</p>

## 🚀 Features

- **💬 Interactive Chat**: Converse naturally with the virtual assistant
- **📖 Book Search**: Find books by title, author, or category
- **📋 Book Details**: Get complete information about any book
- **🛒 Inline Purchase System**: Process purchases directly in the chat
- **📧 Email Service**: Automatic purchase confirmation (simulated)
- **📊 Popular Books**: View best-selling titles
- **📖 PDF Books**: Complete and standardized educational material
- **🧠 Conversation Memory**: The AI remembers conversation context
- **🌍 Multilingual**: Detects and responds in the user's language

## 🏗️ Project Structure

```
/
├── main.py                 # Main application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── Makefile               # Development tasks
├── data/
│   ├── __init__.py        # Data package
│   └── db.py              # Database models and operations
├── helper/
│   ├── __init__.py        # Helper package
│   └── email_service.py   # Email services
├── ui/
│   ├── __init__.py        # UI package
│   └── chat.py            # Chat interface with inline purchases
└── ai/
    ├── __init__.py        # AI package
    └── bookstore_agent.py # Pydantic AI agent and tools
```

## 📦 Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/paulocoutinhox/pydanticai-store.git
   cd pydanticai-store
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   # On macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate

   # On Windows
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run main.py
   ```

5. **Open your browser:**
   The application will open automatically at `http://localhost:8501`

## 🎯 How to Use

### Example Conversations:

**Search for Books:**
- "I want to buy the Angelologia book"
- "Search for systematic theology books"
- "Show me books by Pastor Paulo Coutinho"

**View Details:**
- "Details about the Cristologia book"
- "Tell me more about O Vale de Elá"
- "Information about Hermenêutica"

**Popular Books:**
- "Show me the most popular books"
- "What are the best sellers?"
- "Top 5 in the bookstore"

**Make a Purchase:**
- "I want to buy the História da Igreja book"
- "Buy Bibliologia"
- "Buy O Segredo da Prosperidade dos Judeus"

**Get Help:**
- "I need help"
- "How does the purchase work?"
- "What formats do you have?"

## 🛠️ Technologies Used

- **Streamlit**: Interactive web interface
- **Pydantic AI**: Conversational AI agent framework
- **Google Gemini**: Large language model
- **Python**: Primary programming language

## 📚 Available Books (in Portuguese)

### Teologia Sistemática:
- **Angelologia** - Estudo dos Anjos (R$ 10,00)
- **Bibliologia** - Doutrina das Escrituras (R$ 10,00)
- **Cristologia** - Estudo de Cristo (R$ 10,00)
- **Escatologia** - Estudo das Últimas Coisas (R$ 10,00)
- **Hamartiologia** - Estudo do Pecado (R$ 10,00)
- **Pneumatologia** - Estudo do Espírito Santo (R$ 10,00)
- **Soteriologia e Eclesiologia** - Salvação e Igreja (R$ 10,00)
- **Teologia Própria - Teontologia** - Estudo de Deus (R$ 10,00)

### Estudo Bíblico:
- **Antigo Testamento** - Estudo das Escrituras Hebraicas (R$ 10,00)
- **Novo Testamento** - Estudo das Escrituras Cristãs (R$ 10,00)
- **Geografia Bíblica** - Contexto Histórico e Cultural (R$ 10,00)
- **O Vale de Elá** - Quando Deus Planta em Vales (R$ 10,00)

### Hermenêutica:
- **Exegese** - Interpretação das Escrituras (R$ 10,00)
- **Hermenêutica** - Interpretação das Escrituras Sagradas (R$ 10,00)

### História:
- **História da Igreja** - Evolução e Impacto do Cristianismo (R$ 10,00)
- **História e Cultura Judaica** - Tradições e Costumes Bíblicos (R$ 10,00)

### Ministério Prático:
- **Evangelismo e Missões** - Estratégias e Práticas (R$ 10,00)
- **Homilética** - A Arte de Pregar e Comunicar (R$ 10,00)

### Apologética:
- **Religiões, Seitas e Heresias** - Análise Crítica e Comparativa (R$ 10,00)

### Finanças Cristãs:
- **O Segredo da Prosperidade dos Judeus** - Princípios Judaicos para o Sucesso (R$ 10,00)

## 🎨 Interface Features

The application features a clean, focused interface with:
- **Real-time chat** with message history
- **Inline purchase forms** that appear when needed
- **Conversation context management**
- **Simple and intuitive design**

## 📧 Email System

The system simulates sending purchase confirmation emails, displaying in the console:
- Recipient email
- Message subject
- Order number
- Purchase amount

**Note:** This is currently a simulation. For real email functionality, see the TODO comments in `helper/email_service.py`.

## 🔧 Configuration

### Environment Variables

No environment variables are required for basic functionality. The application uses simulated data and services.

### Customization

You can customize the application by:
- Adding more books to the database in `data/db.py`
- Implementing real email functionality in `helper/email_service.py`
- Modifying the AI agent's system prompt in `ai/bookstore_agent.py`
- Customizing the chat interface in `ui/chat.py`

## 🚀 Future Enhancements

- Real database integration (PostgreSQL, MongoDB)
- Payment system integration
- Expanded theological book catalog
- User rating and review system
- Personalized recommendations
- Purchase history tracking
- Real email service integration
- User authentication system

## 🤝 Contributing

We welcome contributions! Please feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

For development, you may want to install additional tools:

```bash
pip install black
```

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2025 Virtual Bookstore

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/paulocoutinhox/pydanticai-store/issues) page
2. Create a new issue with detailed information
3. Contact the maintainers

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) for the AI agent framework
- [Google Gemini](https://ai.google.dev/) for the language model
- All contributors and users of this project
