from typing import Optional
from config import settings
from roles import RolesPresent, ROLES_SYSTEM_PROMPT
from prompts import build_system_prompt, collapse_history
from memory import ConversationMemory
from llmclient import GeminiClient

# Esta clase se encarga de gestionar la conversacion con el modelo
class ChatService:
    # El rol por defecto es ASISTENTE
    def __init__(self, role: RolesPresent = RolesPresent.ASISTENTE):
        self.role = role
        self.memory = ConversationMemory(max_message=settings.max_history)
        self.client = GeminiClient(
            api_key=settings.api_key,
            model_name=settings.model
        )

    # Esta funcion ask hace la pregunta al modelo y guarda el contexto
    def ask(self, prompt: str) -> str:
        system_prompt = build_system_prompt(
            ROLES_SYSTEM_PROMPT[self.role]
        )

        # Obtener el historial colapsado
        history = collapse_history(self.memory.get())

        # Llamar al cliente Gemini para generar la respuesta
        response_text = self.client.generative(
            system_prompt=system_prompt,
            history=history,
            user_message=prompt,
            max_retries=settings.max_retries,
            timeout_seconds=settings.timeout
        )

        # Actualizar la memoria con el nuevo mensaje y la respuesta del modelo
        self.memory.add_user_message(prompt)
        self.memory.add_model(response_text)

        return response_text

    def set_role(self, role: RolesPresent):
        """Cambia el rol del ChatService"""
        self.role = role

    def reset(self):
        self.memory.clear()