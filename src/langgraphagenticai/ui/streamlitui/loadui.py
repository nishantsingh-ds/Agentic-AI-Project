import streamlit as st
import os
from datetime import date

from langchain_core.messages import AIMessage,HumanMessage
from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config =  Config() # config
        self.user_controls = {}

    def initialize_session(self):
        return {
        "current_step": "requirements",
        "requirements": "",
        "user_stories": "",
        "po_feedback": "",
        "generated_code": "",
        "review_feedback": "",
        "decision": None
    }
  

    def load_streamlit_ui(self):
        # 0) Bootstrap Tavily key from Streamlit Secrets (so you don’t need to re‑enter it every run)
        tavily_secret = st.secrets.get("TAVILY_API_KEY", "")
        if tavily_secret:
            os.environ["TAVILY_API_KEY"] = tavily_secret

        # 1) Safely fetch your title (might be None)
        raw_title = self.config.get_page_title() or ""
        full_title = f"🤖 {raw_title}".strip()

        # 2) Use the safe title everywhere
        st.set_page_config(page_title=full_title, layout="wide")
        st.header(full_title)

        # 3) Initialize your session_state keys
        st.session_state.setdefault("timeframe", "")
        st.session_state.setdefault("IsFetchButtonClicked", False)
        st.session_state.setdefault("IsSDLC", False)

        with st.sidebar:
            # 4) Get options from config (always lists)
            llm_options     = self.config.get_llm_options()   or []
            usecase_options = self.config.get_usecase_options() or []

            # 5) LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == "Groq":
                model_options = self.config.get_groq_model_options() or []
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)

                groq_key = st.text_input("Groq API Key", type="password")
                if groq_key:
                    os.environ["GROQ_API_KEY"] = groq_key
                    self.user_controls["GROQ_API_KEY"] = groq_key
                else:
                    st.warning("⚠️ Please enter your GROQ API key (see https://console.groq.com/keys).")

            # 6) Use case selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Use Case", usecase_options)

            if self.user_controls["selected_usecase"] == "Chatbot with Tool":
                # Only prompt if we don’t already have it in the env
                if not os.getenv("TAVILY_API_KEY"):
                    tavily_input = st.text_input(
                        "Tavily API Key",
                        type="password",
                        help="Or set TAVILY_API_KEY in Streamlit Secrets to avoid typing it here."
                    ).strip()

                    if tavily_input:
                        os.environ["TAVILY_API_KEY"] = tavily_input
                        self.user_controls["TAVILY_API_KEY"] = tavily_input
                    else:
                        st.warning("⚠️ Please enter your TAVILY_API_KEY or add it to Streamlit Secrets.")
                else:
                    # already loaded from secrets
                    self.user_controls["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

            # 7) Initialize the app state the first time through
            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()

        return self.user_controls
