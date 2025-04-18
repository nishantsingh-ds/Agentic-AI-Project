from configparser import ConfigParser

class Config:
    def __init__(self, config_file=r"E:\LANGGRAPHPROJECT\src\langgraphagenticai\ui\uiconfigfile.ini"):
        if config_file is None:
            # compute the path next to this file
            here = os.path.dirname(__file__)
            config_file = os.path.join(here, "uiconfigfile.ini")

        self.parser = ConfigParser()
        self.parser.read(config_file)

    def get_llm_options(self):
        raw = self.parser.get("DEFAULT", "LLM_OPTIONS", fallback="")
        # split on commas, strip whitespace, drop any empty strings
        return [opt.strip() for opt in raw.split(",") if opt.strip()]

    def get_usecase_options(self):
        raw = self.parser.get("DEFAULT", "USECASE_OPTIONS", fallback="")
        return [opt.strip() for opt in raw.split(",") if opt.strip()]

    def get_groq_model_options(self):
        raw = self.parser.get("DEFAULT", "GROQ_MODEL_OPTIONS", fallback="")
        return [opt.strip() for opt in raw.split(",") if opt.strip()]

    def get_page_title(self):
        return self.parser.get("UI", "page_title", fallback="")