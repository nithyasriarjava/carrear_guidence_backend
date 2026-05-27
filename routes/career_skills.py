from fastapi import APIRouter,Depends

from sqlalchemy.orm import Session

from database import SessionLocal

from models import CareerSkill

from schemas import CareerSkillResponse


router=APIRouter()


def get_db():

    db=SessionLocal()

    try:

        yield db

    finally:

        db.close()



@router.get(

"/career_skills",

response_model=list[CareerSkillResponse]

)

def get_career_skills(

db:Session=Depends(get_db)

):


    skills=db.query(

        CareerSkill

    ).all()


    return skills