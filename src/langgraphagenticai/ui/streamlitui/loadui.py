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
        # 1) Safely fetch your title (might be None)
        raw_title = self.config.get_page_title() or ""
        # 2) Build the display title
        full_title = f"🤖 {raw_title}".strip()

        # 3) Use the safe title everywhere
        st.set_page_config(page_title=full_title, layout="wide")
        st.header(full_title)

        # 4) Initialize your session_state keys
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False

        with st.sidebar:
            # Get options from config (they should each return a list)
            llm_options     = self.config.get_llm_options()   or []
            usecase_options = self.config.get_usecase_options() or []

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                model_options = self.config.get_groq_model_options() or []
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input(
                    "API Key", type="password"
                )
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Refer to https://console.groq.com/keys")

            # Use case selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

            if self.user_controls["selected_usecase"] == "Chatbot with Tool":
                self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input(
                    "TAVILY API KEY", type="password"
                )
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️ Please enter your TAVILY_API_KEY. Refer to https://app.tavily.com/home")

            # Initialize the app state the first time through
            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()

        return self.user_controls
