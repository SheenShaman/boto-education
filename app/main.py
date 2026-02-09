import random
import string
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from app.models import ShortenRequest, ShortenResponse
from app.db import init_db, get_connection

ALPHABET = string.ascii_letters + string.digits

app = FastAPI(title="URL shorten")


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.post("/shorten", response_model=ShortenResponse)
def shorten(request: ShortenRequest):
    """
    Принимает длинную ссылку,
    возвращает короткий URL
    """
    with get_connection() as conn:
        code = "".join(random.choices(ALPHABET, k=6))
        try:
            conn.execute(
                """
                INSERT INTO Shorten(code, original_url) 
                VALUES (?, ?)
                """,
                (code, str(request.url))
            )
            conn.commit()
            return {"short_url": f"http://localhost:8000/{code}"}
        except Exception as e:
            print(e)

    raise HTTPException(
        status_code=500, detail="Не удалось сгенерировать короткий url"
    )


@app.get("/{code}")
def redirect_url(code: str):
    """
    Делает редирект
    """
    with get_connection() as conn:
        row = conn.execute(
            "SELECT original_url FROM Shorten WHERE code = ?",
            (code,),
        ).fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="URl not found")

        return RedirectResponse(url=row["original_url"])
