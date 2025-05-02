from typing import Optional, List
from datetime import time
from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, Integer, Time, JSON
from sqlalchemy.ext.declarative import declarative_base

# Declaramos la clase base
Base = declarative_base()

class FibonacciRequest(BaseModel):
    hour: time
    email: Optional[EmailStr] = None
    subject: Optional[str] = None

class FibonacciDatabaseDB(Base):
    __tablename__ = 'fibonacci_databases'

    id = Column(Integer, primary_key=True, index=True)
    hour = Column(Time, nullable=False)
    fibonacci_sequence = Column(JSON, nullable=False)

    def __repr__(self):
        return f"<FibonacciDatabaseDB(id={self.id}, hour={self.hour})>"
