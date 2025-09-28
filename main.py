import sys
from roles import RolePreset
from chat_service import ChatService
from config import Settings

def choose_role() -> RolePreset:
    print("Elegí un rol:")
    print("1) profesor, 2) traductor, 3) programador, 4) asistente")
    sel = input("Selecciona una opción (1-4): ")

    mapping = {
        "1": RolePreset.PROFESOR,
        "2": RolePreset.TRADUCTOR,
        "3": RolePreset.PROGRAMADOR,
        "4": RolePreset.ASISTENTE
    }
    return mapping.get(sel, RolePreset.ASISTENTE)

def print_help():
    print("\nComandos disponibles")
    print(":rol profesor|traductor|programador|asistente - Cambia el rol actual")
    print(":reset - Reinicia la conversación")
    print(":salir - Salir de la aplicación\n")

def main():
    print(f"'robot' {Settings.system_name}")
    role = choose_role()
    chat = ChatService(role=role)
    print_help()

    while True:
        try:
            user_input = input("vos: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nSaliendo de la aplicación, hasta luego!")
            break
        if not user_input:
            continue

        if user_input.lower() in (":salir", "salir", "exit", "quit"):
            print("Saliendo de la aplicación, hasta luego!")
            break
        if user_input.lower() == ":reset":
            chat.reset()
            print("Conversación reiniciada.")
            continue
        if user_input.lower().startswith(":rol "):
            new_role_str = user_input[5:].strip().lower()
            mapping = {
                "profesor": RolePreset.PROFESOR,
                "traductor": RolePreset.TRADUCTOR,
                "programador": RolePreset.PROGRAMADOR,
                "asistente": RolePreset.ASISTENTE
            }
            if new_role_str in mapping:
                chat.role = mapping[new_role_str]
                print(f"Rol cambiado a {new_role_str}")
            else:
                print("Rol inválido. Opciones: profesor, traductor, programador, asistente.")
            continue
        if user_input.lower() == ":help":
            print_help()
            continue

        try:
            answer = chat.ask(user_input)
            print(f"'robot' {answer}")
        except Exception as e:
            print(f"Error al obtener respuesta: {e}")

if __name__ == "__main__":
    main()