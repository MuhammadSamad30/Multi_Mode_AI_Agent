import streamlit as st
import asyncio
from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file!")

client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

config = RunConfig(
    model=model,
    model_provider=client
)

agent = Agent(
    name="Multi-Mode Agent",
    instructions="""
You are an intelligent multi-purpose AI created by Muhammad Samad. 
Always follow the selected mode and respond clearly and helpfully.

If the user asks anything like:
- "Who made you?" 
- "Who is your creator?"
- "Who developed you?"
- "Tumhein kisne banaya?" 
- "تمہیں کس نے بنایا؟"
Then clearly reply:

**English**: "I was created by Muhammad Samad."
**Urdu**: "مجھے محمد سمعاد نے بنایا ہے۔"

Be polite, professional, and concise.
"""
)


st.set_page_config("AI Chatbot by Samad", page_icon="🤖", layout="centered")

st.markdown("""
<style>
@keyframes fadeIn {
  0% {opacity: 0; transform: translateY(-20px);}
  100% {opacity: 1; transform: translateY(0);}
}

.title {
  font-size: 2em;
  font-weight: 800;
  color: #4ADEDE;
  text-align: center;
  margin-bottom: 0.5em;
  animation: fadeIn 1s ease-in-out;
}

.subtitle {
  text-align: center;
  font-size: 1.1em;
  color: #999;
  margin-bottom: 2em;
}

.codebox {
  background: #0f172a;
  color: #f8fafc;
  padding: 1.2em;
  border-radius: 12px;
  font-family: 'Fira Code', monospace;
  font-size: 1em;
  box-shadow: 0 4px 14px rgba(0,0,0,0.3);
  margin-top: 1em;
}

button[kind="primary"] {
  background: linear-gradient(to right, #4ADEDE, #38BDF8);
  color: black;
  font-weight: bold;
  border-radius: 8px;
  padding: 0.5em 1.5em;
  transition: 0.3s ease-in-out;
}

button[kind="primary"]:hover {
  background: linear-gradient(to right, #38BDF8, #4ADEDE);
  transform: scale(1.02);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🤖 Samad\'s Multi-Mode AI Agent</div>',
            unsafe_allow_html=True)
st.markdown('<div class="subtitle">Choose a mode, enter your input, and let the AI do the rest ✨</div>',
            unsafe_allow_html=True)

mode = st.selectbox("🎯 Select a Mode", [
    "💬 Chat",
    "✍️ Write Code",
    "🧠 Explain Code",
    "🐞 Fix Bug",
    "✍️ Summarize",
    "📚 Ask Concept",
    "🌐 Translate",
    "💡 Project Idea"
])

user_input = st.text_area("💬 Your Input", height=180,
                          placeholder="Type your code or question here...")


def generate_prompt(mode, text):
    prompts = {
        "💬 Chat": text,
        "✍️ Write Code": f"Write code for this:\n{text}",
        "🧠 Explain Code": f"Explain this code line by line:\n{text}",
        "🐞 Fix Bug": f"Find and fix bugs in this code:\n{text}",
        "✍️ Summarize": f"Summarize this:\n{text}",
        "📚 Ask Concept": f"Explain this concept:\n{text}",
        "🌐 Translate": f"Translate this: {text}",
        "💡 Project Idea": f"Suggest project ideas based on:\n{text}"
    }
    return prompts.get(mode, text)


async def run_agent(prompt):
    return await Runner.run(agent, input=prompt, run_config=config)

if st.button("🚀 Run"):
    if not user_input.strip():
        st.warning("⚠️ Please enter something first.")
    else:
        with st.spinner("🤔 Thinking..."):
            prompt = generate_prompt(mode, user_input)
            response = asyncio.run(run_agent(prompt))

        st.markdown("### ✅ AI Response:")
        st.markdown(
            f"<div class='codebox'>{response.final_output}</div>", unsafe_allow_html=True)
