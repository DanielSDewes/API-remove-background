from rembg import remove

def remove_background(image_bytes: bytes) -> bytes:
    """
    Recebe bytes da imagem e retorna os bytes da imagem com fundo removido.
    """
    result_bytes = remove(image_bytes)
    return result_bytes
