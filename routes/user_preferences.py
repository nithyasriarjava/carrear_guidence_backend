from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import SessionLocal

from models import (
    UserPreferences,
    UserSelectedSkills,
    UserSelectedInterests
)

from pydantic import BaseModel



router = APIRouter()



class PreferenceRequest(BaseModel):

    user_id:str

    department_id:int

    skills:list[int]

    interests:list[int]



def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



@router.get("/user_preferences/{user_id}")

def check_preferences(

    user_id:str,

    db:Session = Depends(get_db)

):

    existing = db.query(
        UserPreferences
    ).filter(

        UserPreferences.user_id == user_id

    ).first()



    if existing:

        return {

            "exists":True

        }



    return {

        "exists":False
    }



@router.post("/save_preferences")

def save_preferences(

    request:PreferenceRequest,

    db:Session = Depends(get_db)

):

    existing = db.query(
        UserPreferences
    ).filter(

        UserPreferences.user_id == request.user_id

    ).first()



    if existing:

        return {

            "message":"Preferences Already Exists"

        }



    preference = UserPreferences(

        user_id=request.user_id,

        department_id=request.department_id

    )

    db.add(preference)



    for skill in request.skills:

        skill_item = UserSelectedSkills(

            user_id=request.user_id,

            skill_id=skill

        )

        db.add(skill_item)



    for interest in request.interests:

        interest_item = UserSelectedInterests(

            user_id=request.user_id,

            interest_id=interest

        )

        db.add(interest_item)



    db.commit()



    return {

        "message":"Preferences Saved"

    }

