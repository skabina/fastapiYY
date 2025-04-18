from fastapi import FastAPI, HTTPException
import uvicorn

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
        tags=["Книжки"]
        summary="Отримати всі книги"
        )
def read_books():
    return books


@app.get("/books/{id}",
        tags=["Книжки"]
        summary="Отримати конкретну книгу"
        )
def get_books(id: int):
    for book in books:
       if book["id"] == id:
           return book
    raise HTTPException(status_code=404, detail=f"Книга з {id} id неіснує")
       
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)