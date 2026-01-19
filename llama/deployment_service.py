import subprocess
from subprocess import CalledProcessError
from loguru import logger
import time


class OllamaService:
    def __init__(self, initialisation_buffer=2):
        self.deployed = False
        self.initialisation_buffer = initialisation_buffer
        self.ollama_process = None

    def start_ollama_server(self) -> None:
        try:
            self.ollama_process = subprocess.Popen(self.build_ollama_run_command())
        except CalledProcessError:
            logger.warning("Ollama service failed to start")
            return

        time.sleep(self.initialisation_buffer)
        logger.info("Ollama service started")
        self.deployed = True

    def stop_ollama_server(self) -> None:
        logger.info(f"Closing Ollama server with pid {self.ollama_process.pid}.")
        self.ollama_process.terminate()

    def build_ollama_run_command(self):
        return ["ollama", "serve"]
