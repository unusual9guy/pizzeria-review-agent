# 🍕 Pizzeria AI Agent

This project creates a simple AI agent that can answer questions about a pizzeria based on customer reviews. The agent uses LangChain with Ollama to retrieve relevant reviews and generate accurate responses.

## 📋 Project Overview

The AI agent uses:
- **LangChain**: Framework for developing applications powered by language models
- **Ollama**: Local LLM runner
- **Llama 3.2**: For generating responses
- **MXBai Embeddings**: For creating vector embeddings of reviews
- **ChromaDB**: Vector database for storing and retrieving reviews

## 🔍 Prerequisites

- Python 3.8+
- Git
- Ollama installed on your system

## 🛠️ Installation Instructions

### 1. 📥 Install Ollama

Download and install Ollama for your operating system from [the official website](https://ollama.com/download).

### 2. 🤖 Pull the Required Models

Open a terminal and launch Ollama:

```bash
ollama
```

In a new terminal window, pull the required models:

```bash
ollama pull llama3.2
ollama pull mxbai-embed-large
```

Wait for the models to download completely.

### 3. 📂 Clone the Repository

```bash
git clone https://github.com/unusual9guy/pizzeria-review-agent.git
cd pizzeria-review-agent
```

### 4. 🔧 Create and Activate a Virtual Environment

#### For Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

#### For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 5. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Make sure Ollama is running in a separate terminal window
2. Run the main script:

```bash
python src/main.py
```

3. Start asking questions about the pizzeria when prompted
4. Type 'q' to quit the application

## 💬 Example Questions

- "What do customers say about the pizza crust?"
- "Are there any complaints about the delivery service?"
- "What's the overall rating of the restaurant?"
- "What dishes are most recommended by customers?"

## 📁 Project Structure

- `src/main.py`: The main application that processes user questions
- `src/vector.py`: Handles vector database creation and retrieval
- `data/realistic_restaurant_reviews.csv`: Dataset containing pizzeria reviews
- `chrome_langchain_db/`: Directory where the vector database is stored

## 📚 Dependencies

- langchain-ollama
- langchain-core
- langchain-chroma
- pandas
- chromadb

## 🙏 Acknowledgements

This project was inspired by the YouTube video: [Build an AI Agent with LangChain](https://www.youtube.com/watch?v=E4l91XKQSgw). 

The dataset was also obtained from the author of the YouTube video. 