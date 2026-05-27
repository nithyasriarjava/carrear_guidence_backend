# pydantic library la irunthu BaseModel import panrom
# Purpose:
# API request/response format create panna use aagum

from pydantic import BaseModel



# SkillResponse nu oru schema class create panrom
# Purpose:
# Skill data API response la epdi return aaganum nu define pannum

class SkillResponse(BaseModel):


    # id variable create panrom
    # :
    # Type annotation use panrom
    # int = integer(number)

    id:int


    # skill_name variable create panrom
    # str = string(text)

    skill_name:str

    

    # Config class create panrom
    # Purpose:
    # SQLAlchemy model data ah schema-ku convert panna

    class Config:


        # SQLAlchemy object attributes read panna allow pannum

        from_attributes=True



class DepartmentResponse(BaseModel):

    id:int

    department_name:str


    class Config:

        from_attributes=True


class InterestResponse(BaseModel):

    id:int
    interest_name:str

    class Config:

        from_attributes=True




class CareerResponse(BaseModel):

    id:int
    career_name:str
    description:str
    salary:str
    difficulty:str
    growth:str

    class Config:

        from_attributes=True




class RoadmapResponse(BaseModel):

    id:int
    career_id:int
    step_number:int
    step_title:str
    step_description:str

    class Config:

        from_attributes=True




class CareerSkillResponse(BaseModel):

    id:int
    career_id:int
    skill_id:int

    class Config:

        from_attributes=True




class CareerInterestResponse(BaseModel):

    id:int
    career_id:int
    interest_id:int

    class Config:

        from_attributes=True


        # LearningResource response schema create panrom

class LearningResourceResponse(BaseModel):


    id:int


    career_id:int


    title:str


    resource_type:str


    url:str



    class Config:

        from_attributes=True



        # UserProgress response schema create panrom

class UserProgressResponse(BaseModel):


    id:int


    user_id:str


    career_id:int


    completed_step:int


    progress_percentage:int



    class Config:

        from_attributes=True