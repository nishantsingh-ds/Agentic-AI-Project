import configparser
import os

class Config:
    def __init__(self, config_file=None):
        if config_file is None:
            here = os.path.dirname(__file__)
            config_file = os.path.join(here, "uiconfigfile.ini")
        self.parser = configparser.ConfigParser()
        self.parser.read(config_file)

    def _split_list(self, section: str, key: str) -> list[str]:
        raw = self.parser.get(section, key, fallback="")
        # Split on commas, strip whitespace, drop empties
        return [item.strip() for item in raw.split(",") if item.strip()]

    def get_llm_options(self) -> list[str]:
        return self._split_list("DEFAULT", "LLM_OPTIONS")

    def get_usecase_options(self) -> list[str]:
        return self._split_list("DEFAULT", "USECASE_OPTIONS")

    def get_groq_model_options(self) -> list[str]:
        return self._split_list("DEFAULT", "GROQ_MODEL_OPTIONS")

    def get_page_title(self) -> str:
        # Always returns a string
        return self.parser.get("UI", "page_title", fallback="")
