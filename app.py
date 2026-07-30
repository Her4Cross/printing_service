from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from printer import print_barcode

app = FastAPI(title="Barcode Printing Service")

templates = Jinja2Templates(directory="templates")


class PrintRequest(BaseModel):
    barcode: str
    quantity: int


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/print")
async def print_label(request: PrintRequest):

    try:

        print_barcode(
            request.barcode,
            request.quantity
        )

        return {
            "message": f"Se enviaron {request.quantity} etiquetas correctamente."
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )