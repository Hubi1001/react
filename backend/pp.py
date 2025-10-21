import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# Database configuration
DATABASE_URL = "postgresql://admin:admin@localhost:5432/mydb"  # Change if using ElephantSQL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy model for DB
class Fruit(Base):
    __tablename__ = "fruits"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

Base.metadata.create_all(bind=engine)

# Pydantic models for request/response
class AddFruit(BaseModel):
    name: str

class FruitResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True  # Important for SQLAlchemy objects

# FastAPI app
app = FastAPI(debug=True)

origins = [
    "http://localhost:3000",  # React frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST endpoint to add fruit
@app.post("/fruits", response_model=FruitResponse)
def add_fruit(fruit: AddFruit, db: Session = Depends(get_db)):
    db_fruit = Fruit(name=fruit.name)
    db.add(db_fruit)
    db.commit()
    db.refresh(db_fruit)
    return db_fruit

# GET endpoint to list fruits
@app.get("/fruits", response_model=List[FruitResponse])
def get_fruits(db: Session = Depends(get_db)):
    return db.query(Fruit).all()

# Run server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)