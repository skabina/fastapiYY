from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()

books = [  
    {
        "id":1,
        "title": "Pythonbb",
        "author": "MMbist",
    },

    {
    
        "id": 2,
        "title": "bb",
        "author": "MM",

    }
]    

@app.get("/books",
        tags=["Книжки"],
        summary="Отримати всі книги"
        )
def read_books():
    return books


@app.get("/books/{id}",
        tags=["Книжки"],
        summary="Отримати конкретну книгу"
        )
def get_books(id: int):
    for book in books:
       if book["id"] == id:
           return book
    raise HTTPException(status_code=404, detail=f"Книга з {id} id неіснує")

class NewBook(BaseModel):
    title: str
    author: str

@app.post("/books",
          tags=["Книжки"],
          summary="Додати книгу")
def creat_book(new_book: NewBook):
    books.append({
        "id": len(books)+1,
        "title": new_book.title,
        "author": new_book.author
    })
    return {"success": True, "message": "Книга успішно додана"}
       
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)