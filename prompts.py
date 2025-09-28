from typing import List, Dict

def build_system_prompt(role_instructions:str) -> str:
    base = (
        "Sos un chatbot de consola que responde en español en forma clara y útil"
        "Si el usuario pide código, inclui explicaciones braves"
        "Evita información inventada. Y pedí aclaraciones si faltan datos"
    )
    return base + f"Contexto de rol: {role_instructions}"

def collapse_history(history: List[Dict[str,str]]) -> List[Dict[str,str]]:
    #Mantiene formato {'role': 'user', 'contect': '...'}
    return history