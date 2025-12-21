# 🤖 Customer Complaint Resolver Agent

An intelligent agentic system that automatically processes customer complaints through multiple specialized agents, categorizes them, prioritizes urgency, drafts responses, and maintains memory of high-priority issues.

## 🎯 Project Overview

This project demonstrates an **agentic workflow** where multiple AI agents work together to resolve customer complaints efficiently. The system:

1. **Classifies** complaints into categories (Payment, Delivery, Technical, Account, General)
2. **Prioritizes** complaints (High/Medium/Low)
3. **Drafts** professional customer service responses
4. **Recommends** next actions for support teams
5. **Re-evaluates** priority after response (agentic behavior)
6. **Stores** high-priority complaints in memory for tracking

## 🏗️ Architecture

### Agents

- **Classifier Agent**: Categorizes complaints into predefined categories
- **Priority Agent**: Determines urgency level and re-evaluates after response
- **Response Agent**: Drafts professional customer service responses
- **Action Agent**: Recommends next steps for support teams

### Components

- `app.py` - Streamlit UI for interaction
- `agents.py` - All agent implementations and workflow
- `memory.py` - Memory system for storing high-priority complaints
- `utils.py` - Helper functions and LLM integration

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (optional - app works with mock responses if not provided)

### Installation

1. **Clone or download this project**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API key (optional):**
   
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
   
   Or set it as an environment variable:
   ```bash
   export OPENAI_API_KEY=your_api_key_here
   ```
   
   **Note:** If no API key is provided, the app will use mock responses for demonstration purposes.

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser:**
   The app will automatically open at `http://localhost:8501`

## 📖 How to Use

1. **Enter a complaint** in the text area or click an example complaint
2. **Click "Process Complaint"** to run it through all agents
3. **View results:**
   - Category classification
   - Priority level (with color coding)
   - Drafted response
   - Recommended action
   - Agent workflow visualization
4. **Check memory** in the sidebar to see stored high-priority complaints

## 🎯 Why This Is Agentic

This system demonstrates **agentic behavior** because:

1. **Multi-step workflow**: Complaints go through multiple specialized agents
2. **Memory**: High-priority complaints are stored and tracked
3. **Re-evaluation**: The agent re-checks priority after drafting a response
4. **Decision-making**: Each agent makes independent decisions
5. **State management**: The system maintains state across interactions

## 🎨 Features

- ✅ Beautiful Streamlit UI with color-coded priorities
- ✅ Real-time processing through agent workflow
- ✅ Memory dashboard for high-priority complaints
- ✅ Example complaints for quick testing
- ✅ Processing history
- ✅ Works with or without API key (mock mode)

## 📝 Example Complaints

Try these examples:

- "My order is delayed and I haven't received any updates"
- "I requested a refund 2 weeks ago but haven't received it"
- "The app keeps crashing every time I try to login"
- "I can't access my account, it says password is incorrect"
- "The website is showing errors and I can't complete my purchase"

## 🔧 Configuration

The app uses OpenAI's GPT-3.5-turbo by default, but you can modify the model in `utils.py`:

```python
def get_llm_response(prompt: str, model: str = "gpt-3.5-turbo") -> str:
    # Change model here
```

## 📊 Project Structure

```
complaint-agent/
│
├── app.py          → Streamlit UI
├── agents.py       → All agents logic
├── memory.py       → Store high priority complaints
├── utils.py        → Helper functions & LLM integration
├── requirements.txt → Dependencies
└── README.md       → This file
```

## 🎤 Presentation Script (30 seconds)

> "Our system reads customer complaints, categorizes them, assigns priority, drafts responses, and recommends actions. It also remembers high-priority complaints and re-evaluates urgency, which makes it an agentic workflow."

## 🛠️ Technology Stack

- **Python 3.8+**
- **Streamlit** - UI framework
- **OpenAI API** - LLM integration (with mock fallback)
- **Python dictionaries** - Memory storage

## 📄 License

This project is for educational/demonstration purposes.

## 🤝 Contributing

Feel free to fork, modify, and use this project for your own purposes!

---

**Built with ❤️ for demonstrating agentic AI systems**






