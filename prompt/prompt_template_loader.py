"""Class to load prompt template. Designed for forward compatibility if storage format of prompt changes."""


_BASE_PROMPT = """I am asking you to analyse the following image, and create an alt-text caption that can be used for social media.
Please follow alt-text best practices, which include:
    - Brevity, please restrict output to 1-2 sentences per caption.
    - A focus on the key elements of the image.
    - Do not start the caption with an unnecessary descriptor such as 'Image of' or 'Picture of'
    - Please do highlight the image type, e.g. is this a photography, illustration.

    Please generate up to {max_captions} appropriate alt-text captions for the supplied image.
"""



def load_prompt_template() -> str:
    return _BASE_PROMPT
