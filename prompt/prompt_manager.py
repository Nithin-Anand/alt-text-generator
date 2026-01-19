from typing import Any


class PromptBuilder:
    def __init__(
        self, prompt_template: str, max_keywords: int = 3, tag_style="broad"
    ):
        self.prompt_template = prompt_template
        self.max_keywords = max_keywords
        self.tag_style = tag_style

    def build_prompt(self) -> str:
        prompt_parameters = {
            "max_keywords": self.max_keywords,
            "tag_style": self.tag_style,
        }

        return self.prompt_template.format_map(prompt_parameters)
