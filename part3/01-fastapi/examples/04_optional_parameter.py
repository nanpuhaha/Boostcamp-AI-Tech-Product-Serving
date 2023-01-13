from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/{item_id}")
def read_item(item_id: str, q: Optional[str] = None):
    return {"item_id": item_id, "q": q} if q else {"item_id": item_id}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
