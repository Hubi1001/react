import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String   ## Dodano brakujące importy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://admin:admin@localhost:5432/mydb"  # zmień jeśli używasz ElephantSQL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Fruit(Base):
    __tablename__ = "fruits"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

Base.metadata.create_all(bind=engine)

class Fruit(BaseModel):
    name: str

class Fruits(BaseModel):
    fruits: List[Fruit]
    
app = FastAPI(debug=True)

origins = [
    "http://localhost:3000",
    # Add more origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi import Depends
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/fruits")
def add_fruit(fruit: FruitSchema, db: Session = Depends(get_db)):
    db_fruit = Fruit(name=fruit.name)
    db.add(db_fruit)
    db.commit()
    db.refresh(db_fruit)
    return db_fruit

@app.get("/fruits")
def get_fruits(db: Session = Depends(get_db)):
    return db.query(Fruit).all()