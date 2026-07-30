from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import PrintRequest
from printer import print_items


app = FastAPI(title="Barcode Printing Service")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/print")
async def print_labels(request: PrintRequest):

    if len(request.items) == 0:
        raise HTTPException(
            status_code=400,
            detail="Debe enviar al menos un producto."
        )

    if len(request.items) > 5:
        raise HTTPException(
            status_code=400,
            detail="Solo se permiten hasta 5 productos."
        )

    try:

        print_items(request.items)

        total = sum(item.quantity for item in request.items)

        return {
            "message": f"Se enviaron {total} etiquetas correctamente."
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )