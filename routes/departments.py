# APIRouter import panrom
# Purpose:
# Separate API create panna

from fastapi import APIRouter, Depends


# Session import panrom
# Purpose:
# Database use panna

from sqlalchemy.orm import Session


# DB connection import panrom

from database import SessionLocal


# Department model import panrom

from models import Department


# API response schema import panrom

from schemas import DepartmentResponse



# Router create panrom

router=APIRouter()




# Database open and close function

def get_db():

    db=SessionLocal()

    try:

        yield db

    finally:

        db.close()




# GET API create panrom

@router.get(

"/departments",

response_model=list[DepartmentResponse]

)

def get_departments(

db:Session=Depends(get_db)

):


    departments=db.query(

        Department

    ).all()



    return departments