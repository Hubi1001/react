
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# Database configuration
DATABASE = "sqlite:///./test.db"

engine = create_engine(DATABASE)
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
        orm_mode = True

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]  # Or specify your frontend URL
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/fruits", response_model=List[FruitResponse])
def get_fruits(db: Session = Depends(get_db)):
    fruits = db.query(Fruit).all()
    return fruits

@app.post("/fruits", response_model=FruitResponse)
def add_fruit(new_fruit: AddFruit, db: Session = Depends(get_db)):
    fruit = Fruit(name=new_fruit.name)
    db.add(fruit)
    db.commit()
    db.refresh(fruit)
    return fruit

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# Database configuration
DATABASE = "sqlite:///./test.db"

engine = create_engine(DATABASE)
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
        orm_mode = True

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]  # Or specify your frontend URL
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/fruits", response_model=List[FruitResponse])
def get_fruits(db: Session = Depends(get_db)):
    fruits = db.query(Fruit).all()
    return fruits

@app.post("/fruits", response_model=FruitResponse)
def add_fruit(new_fruit: AddFruit, db: Session = Depends(get_db)):
    fruit = Fruit(name=new_fruit.name)
    db.add(fruit)
    db.commit()
    db.refresh(fruit)
    return fruit

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# Database configuration
DATABASE = "sqlite:///./test.db"

engine = create_engine(DATABASE)
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
        orm_mode = True

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]  # Or specify your frontend URL
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/fruits", response_model=List[FruitResponse])
def get_fruits(db: Session = Depends(get_db)):
    fruits = db.query(Fruit).all()
    return fruits

@app.post("/fruits", response_model=FruitResponse)
def add_fruit(new_fruit: AddFruit, db: Session = Depends(get_db)):
    fruit = Fruit(name=new_fruit.name)
    db.add(fruit)
    db.commit()
    db.refresh(fruit)
    return fruit

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# Database configuration
DATABASE = "sqlite:///./test.db"

engine = create_engine(DATABASE)
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
        orm_mode = True

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]  # Or specify your frontend URL
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/fruits", response_model=List[FruitResponse])
def get_fruits(db: Session = Depends(get_db)):
    fruits = db.query(Fruit).all()
    return fruits

@app.post("/fruits", response_model=FruitResponse)
def add_fruit(new_fruit: AddFruit, db: Session = Depends(get_db)):
    fruit = Fruit(name=new_fruit.name)
    db.add(fruit)
    db.commit()
    db.refresh(fruit)
    return fruit

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)