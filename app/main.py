import os
os.environ["NUMBA_DISABLE_CACHE"] = "1"


from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from .utils import remove_background

app = FastAPI(title="Remove Background API")

@app.post("/remove-background/")
async def remove_background_endpoint(file: UploadFile = File(...)):
    """
    Recebe uma imagem (upload) e retorna a imagem com fundo removido no formato PNG.
    """
    image_bytes = await file.read()
    result_bytes = remove_background(image_bytes)
    return Response(content=result_bytes, media_type="image/png")
