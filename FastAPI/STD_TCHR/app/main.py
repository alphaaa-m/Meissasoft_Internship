from fastapi import FastAPI
from app.database.db import Base, engine
from app.models import students, teachers, courses, associations
from app.routers import std_router, tchr_router, crs_router


app=FastAPI(title='Student_Teacher_Course')

#Base.metadata.create_all(bind=engine)


app.include_router(std_router.router)
app.include_router(tchr_router.router)
app.include_router(crs_router.router)

@app.get('/')
async def home():
    return {"Message": "Welcome to the Student-Teacher-Course API..!"}