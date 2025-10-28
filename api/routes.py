from fastapi import APIRouter, HTTPException
from api.schemas import ChatRequest, ChatResponse
from chat_service import ChatService
from roles import RolesPresent
router = APIRouter()

chat_service = ChatService(role=RolesPresent.ASISTENTE)

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    if not request.mensaje:
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío.")
    if request.reset:
        chat_service.reset()

    rol_lower = request.role.lower()
    try:
        chat_service.set_role(RolesPresent(rol_lower))
    except ValueError:
        raise HTTPException(status_code=400, detail=f"Rol desconocido: {request.role}")
    
    try:
        respuesta = chat_service.ask(request.mensaje)
        return ChatResponse(respuesta=respuesta)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))