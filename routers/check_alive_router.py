from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/check_alive")
def hello_world():
    return JSONResponse(content={"message": "Cthulhu F'taghn ! Sum viva !"})
