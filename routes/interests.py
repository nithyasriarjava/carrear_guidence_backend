# fastapi la irunthu APIRouter, Depends import panrom
#
# APIRouter
# Meaning:
# Separate API create panna
#
# Depends
# Meaning:
# Function automatic ah call panna

from fastapi import APIRouter, Depends




# SQLAlchemy la irunthu Session import panrom
#
# Purpose:
# Database work panna

from sqlalchemy.orm import Session




# database.py la irunthu SessionLocal import panrom
#
# Purpose:
# Database connection open panna

from database import SessionLocal




# models.py la irunthu Interest model import panrom
#
# Purpose:
# interests table access panna

from models import Interest




# schemas.py la irunthu response schema import panrom
#
# Purpose:
# API output format define panna

from schemas import InterestResponse




# Router object create panrom
#
# Purpose:
# API store panna

router=APIRouter()




# Database open → work → close function
#
# Purpose:
# Database connection manage panna

def get_db():

    # DB connection open pannum

    db=SessionLocal()


    try:

        # Temporary DB object use pannum

        yield db


    finally:

        # Work mudinja DB close pannum

        db.close()




# GET API create panrom
#
# Browser:
#
# http://localhost:8000/interests
#
# open panna intha function run aagum

@router.get(

"/interests",

response_model=list[InterestResponse]

)




# Function create panrom
#
# get_interests
#
# Meaning:
# Interests data fetch pannum

def get_interests(

db:Session=Depends(get_db)

):


    # Interests table la iruka
    # ella rows fetch pannum

    interests=db.query(

        Interest

    ).all()



    # User-ku data return pannum

    return interests