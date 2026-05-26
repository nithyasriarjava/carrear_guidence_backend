from fastapi import APIRouter,Depends

from sqlalchemy.orm import Session

from database import SessionLocal

from models import LearningResource

from schemas import LearningResourceResponse


router=APIRouter()


def get_db():

    db=SessionLocal()

    try:

        yield db

    finally:

        db.close()



@router.get(

"/learning-resources",

response_model=list[LearningResourceResponse]

)

def get_learning_resources(

db:Session=Depends(get_db)

):


    resources=db.query(

        LearningResource

    ).all()


    return resources