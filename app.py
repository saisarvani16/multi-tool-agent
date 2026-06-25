import streamlit as st
from backend import run_agent

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Session State
# -----------------------------
if "prompt" not in st.session_state:
    st.session_state.prompt = ""

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #334155
    );
}

/* Main Title */
.main-title {
    text-align: center;
    color: white;
    font-size: 3rem;
    font-weight: bold;
    margin-bottom: 25px;
}

/* Glass Card */
.card {
    background: rgba(255,255,255,0.08);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
}

/* Text Input */
.stTextInput input {
    border-radius: 12px !important;
    border: 2px solid #60a5fa !important;
}

/* Button */
.stButton button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    border: none;
    background: #2563eb;
    color: white;
    font-size: 18px;
    font-weight: bold;
}

.stButton button:hover {
    background: #1d4ed8;
}

/* Response Box */
.response-box {
    background: white;
    padding: 20px;
    border-radius: 15px;
    color: black;
    margin-top: 20px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

section[data-testid="stSidebar"] * {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🤖 AI Assistant")

    st.markdown("---")

    st.subheader("🛠 Available Tools")

    st.success("🌤 Weather Information")
    st.success("📈 Stock Prices")
    st.success("💻 System Commands")

    st.markdown("---")

    st.subheader("⚡ Quick Prompts")

    if st.button("🌤 Weather in Vijayawada"):
        st.session_state.prompt = "What is the weather in Vijayawada?"

    if st.button("🌤 Weather in Hyderabad"):
        st.session_state.prompt = "What is the weather in Hyderabad?"

    if st.button("📈 AAPL Stock"):
        st.session_state.prompt = "Get stock price of AAPL"

    if st.button("📈 TSLA Stock"):
        st.session_state.prompt = "Get stock price of TSLA"

    if st.button("📈 MSFT Stock"):
        st.session_state.prompt = "Get stock price of MSFT"

    st.markdown("---")

    st.subheader("💡 Example Questions")

    st.code("What is the weather in Vijayawada?")
    st.code("Get stock price of AAPL")
    st.code("Get stock price of TSLA")
    st.code("Run command: dir")
    st.code("Run command: ipconfig")

    st.markdown("---")

    st.subheader("📖 How to Ask")

    st.write("""
    ✔ Ask naturally

    ✔ Mention city name for weather

    ✔ Mention stock symbol for stocks

    ✔ Mention command for execution

    ✔ Example:
    'Get stock price of NVDA'
    """)

    st.markdown("---")
    st.caption("Powered by Ollama + Qwen 2.5")

# -----------------------------
# Main UI
# -----------------------------
st.markdown(
    '<h1 class="main-title">🤖 AI Assistant</h1>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    user_query = st.text_input(
        "Ask me anything",
        value=st.session_state.prompt,
        placeholder="What is the weather in Vijayawada?"
    )

    if st.button("🚀 Submit"):

        if user_query.strip():

            with st.spinner("Thinking..."):

                result = run_agent(user_query)

            st.markdown(
                f"""
                <div class="response-box">
                    <h3>Response</h3>
                    <p>{result}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("</div>", unsafe_allow_html=True)