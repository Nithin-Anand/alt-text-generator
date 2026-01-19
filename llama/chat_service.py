from ollama import generate, ChatResponse
from pathlib import Path

class OllamaGenerateService:
    def __init__(self, model: str, supported_file_extensions: list[str]):
        self.model = model
        self.supported_file_extensions = supported_file_extensions

    def query_model(self, prompt: str, image_location: str) -> ChatResponse:
        if self._check_if_image_is_supported(image_location):
            return generate(model=self.model, prompt=prompt, images=[image_location])
        else:            
            raise ValueError(f"The file {image_location} is not supported by this service.")

    def _check_if_image_is_supported(self, image_location: str) -> bool:
        file_extension = image_location.split(".")[-1]
        if file_extension in self.supported_file_extensions:
            return True
        else: 
            return False
