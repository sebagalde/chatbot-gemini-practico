import time
from typing import Dict, List, Optional
import google.generativeai as genai
from config import settings

class GeminiClient:
    def __init__(self, api_key: str, model_name: str):
        if not api_key:
            raise ValueError("API key No configurada")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def generative(
            self,
            system_prompt: str,
            history: List[Dict[str, str]],
            user_message: str,
            max_retries: int,  # <-- corregido
            timeout_seconds: int
    ) -> str:
        attempt = 0  # <-- corregido
        last_error: Optional[Exception] = None  # <-- corregido

        convo = self.model.start_chat(history=[{"role": "user", "parts": system_prompt}] + [{"role": m["role"], "parts": m["content"]} for m in history])

        while attempt < max_retries:
            try:
                response = convo.send_message(user_message)
                text = getattr(response, "text", "")
                if not text:
                    raise ValueError("Respuesta vacía del modelo")
                return text
            except Exception as e:
                last_error = e
                sleep_seconds = 2 ** attempt
                time.sleep(sleep_seconds)
                attempt += 1

        raise RuntimeError(f"Fallo tras {max_retries} intentos: {last_error}")