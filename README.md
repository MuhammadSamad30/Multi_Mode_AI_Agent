# 🤖 Samad's Multi-Mode AI Agent

An intelligent, multi-purpose AI chatbot built with **Streamlit** and powered by **Gemini 2.0 Flash** (via OpenAI-compatible API). Created by **Muhammad Samad**, this agent offers various productivity and development-focused modes in a beautifully interactive UI.

---

## 🌟 Features

- 💬 **Chat** — General-purpose conversational AI  
- 🌐 **Translate** — Translate text into different languages  
- 🧠 **Explain Code** — Understand code line-by-line  
- 🐞 **Fix Bug** — Automatically detect and fix code issues  
- ✍️ **Summarize** — Summarize articles, notes, or documentation  
- 📚 **Ask Concept** — Learn about programming and tech concepts  
- 💡 **Project Idea** — Generate coding project ideas based on input  

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MuhammadSamad30/Multi_Mode_AI_Agent.git
cd multi-mode-ai-agent
````

### 2. Install Dependencies

Make sure you have **Python 3.10+** installed.

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory and add your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```


### 4. Run the App

```bash
streamlit run app.py
```

---

## 🧠 About the AI

This agent uses `AsyncOpenAI` with a custom `OpenAIChatCompletionsModel` to send prompts to the Gemini 2.0 Flash model via the OpenAI-compatible API provided by Google.

The bot is designed to:

* Be polite and professional
* Handle multiple task types using custom prompt templates
* Respond with a personalized signature if asked who created it (in both English and Urdu)

---

## 🧑‍💻 Creator

**Muhammad Samad**
🔗 [Portfolio Website](https://portfolio-tailwind-css-by-samad.vercel.app/)
📫 Connect via GitHub, LinkedIn, or your favorite platform!

---

**Made with ❤️ using Streamlit + Gemini API**

```