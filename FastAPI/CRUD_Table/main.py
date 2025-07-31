from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
import schema as schemas
from db import engine, LocalSession, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRUD_Table")

def get_db():
    database = LocalSession()
    try:
        yield database
    finally:
        database.close()

@app.get("/")
def home():
    return {'Message': 'Welcome to CRUD_Table'}

@app.post("/items/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, database: Session = Depends(get_db)):
    db_item = models.Item(name=item.name)
    database.add(db_item)
    database.commit()
    database.refresh(db_item)
    return db_item

@app.get("/items/{item_id}", response_model=schemas.ItemResponse)
def read_item(item_id: int, database: Session = Depends(get_db)):
    item = database.query(models.Item).filter(models.Item.item_id == item_id).first()
    if item is None:
        return {"error": "Item not found"}
    return item

@app.put("/items/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, item: schemas.ItemCreate, database: Session = Depends(get_db)):
    db_item = database.query(models.Item).filter(models.Item.item_id == item_id).first()
    if db_item is None:
        return {"error": "Item not found"}

    db_item.name = item.name
    database.commit()
    database.refresh(db_item)
    return db_item

@app.delete("/items/{item_id}")
def delete_item(item_id: int, database: Session = Depends(get_db)):
    item = database.query(models.Item).filter(models.Item.item_id == item_id).first()
    if item is None:
        return {"error": "Item not found"}
    database.delete(item)
    database.commit()
    return {"message": "Item deleted"}
