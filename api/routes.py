from fastapi import APIRouter, HTTPException
from api.schemas import ChatRequest, ChatResponse

router = APIRouter()

chat_service = ChatService(role=RolePresets.ASISTENTE)

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    if not request.mensaje:
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío.")
    if request.reset:
        chat_service.reset()

    rol_lower = request.role.lower()
    try:
        chat_service.set_role(RolePreset(rol_lower))
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Rol desconocido: {request.role}")
    
    try:
        respuesta = chat_service.ask(request.mensaje)
        return ChatResponse(respuesta=respuesta)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))