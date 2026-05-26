from sqlalchemy import Column,Integer,String,Text
from database import Base


class Skill(Base):

    __tablename__="skills"

    id=Column(
        Integer,
        primary_key=True,
        index=True
    )

    skill_name=Column(
        String(100)
    )


class Department(Base):


    __tablename__="departments"


    id=Column(

        Integer,

        primary_key=True

    )


    department_name=Column(

        String(100)

    )


    # Interest table model

class Interest(Base):

    __tablename__="interests"

    id=Column(
        Integer,
        primary_key=True
    )

    interest_name=Column(
        String(100)
    )



# Career table model

class Career(Base):

    __tablename__="careers"

    id=Column(
        Integer,
        primary_key=True
    )

    career_name=Column(
        String(100)
    )

    description=Column(
        Text
    )

    salary=Column(
        String(100)
    )

    difficulty=Column(
        String(50)
    )

    growth=Column(
        String(100)
    )



# Roadmap table model

class Roadmap(Base):

    __tablename__="roadmaps"

    id=Column(
        Integer,
        primary_key=True
    )

    career_id=Column(
        Integer
    )

    step_number=Column(
        Integer
    )

    step_title=Column(
        String(255)
    )

    step_description=Column(
        Text
    )



# Career Skills table model

class CareerSkill(Base):

    __tablename__="career_skills"

    id=Column(
        Integer,
        primary_key=True
    )

    career_id=Column(
        Integer
    )

    skill_id=Column(
        Integer
    )



# Career Interests table model

class CareerInterest(Base):

    __tablename__="career_interests"

    id=Column(
        Integer,
        primary_key=True
    )

    career_id=Column(
        Integer
    )

    interest_id=Column(
        Integer
    )


    # LearningResource model create panrom
#
# Purpose:
# learning_resources table connect panna

class LearningResource(Base):


    __tablename__="learning_resources"



    id=Column(

        Integer,

        primary_key=True

    )



    career_id=Column(

        Integer

    )



    title=Column(

        String(255)

    )



    resource_type=Column(

        String(100)

    )



    url=Column(

        String(500)

    )


    # UserProgress model create panrom
#
# Purpose:
# user_progress table connect panna

class UserProgress(Base):


    __tablename__="user_progress"



    id=Column(

        Integer,

        primary_key=True

    )



    user_id=Column(

        String(255)

    )



    career_id=Column(

        Integer

    )



    completed_step=Column(

        Integer

    )



    progress_percentage=Column(

        Integer

    )