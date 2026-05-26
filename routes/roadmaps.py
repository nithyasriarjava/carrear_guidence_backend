from fastapi import APIRouter,Depends

from sqlalchemy.orm import Session

from database import SessionLocal

from models import Roadmap

from schemas import RoadmapResponse


router=APIRouter()


def get_db():

    db=SessionLocal()

    try:

        yield db

    finally:

        db.close()



@router.get(

"/roadmaps",

response_model=list[RoadmapResponse]

)

def get_roadmaps(

db:Session=Depends(get_db)

):


    roadmaps=db.query(

        Roadmap

    ).all()


    return roadmaps