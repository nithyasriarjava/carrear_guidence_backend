# fastapi library la irunthu FastAPI import panrom
#
# Purpose:
# Main backend application create panna

from fastapi import FastAPI


from fastapi.middleware.cors import CORSMiddleware



# Skills router import panrom
#
# Purpose:
# /skills API work panna

from routes.skills import router as skills_router




# Departments router import panrom
#
# Purpose:
# /departments API work panna

from routes.departments import router as department_router




# Interests router import panrom
#
# Purpose:
# /interests API work panna

from routes.interests import router as interests_router




# Careers router import panrom
#
# Purpose:
# /careers API work panna

from routes.careers import router as careers_router




# Roadmaps router import panrom
#
# Purpose:
# /roadmaps API work panna

from routes.roadmaps import router as roadmaps_router




# Career Skills router import panrom
#
# Purpose:
# /career-skills API work panna

from routes.career_skills import router as career_skills_router




# Career Interests router import panrom
#
# Purpose:
# /career-interests API work panna

from routes.career_interests import router as career_interests_router

from routes.career_departments import router as career_departments_router

from routes.learning_resources import router as learning_resources_router

from routes.user_progress import router as user_progress_router

# FastAPI app create panrom

app = FastAPI()


app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


# Skills API connect panrom

app.include_router(

    skills_router

)


app.include_router(
    career_departments_router
)


# Departments API connect panrom

app.include_router(

    department_router

)




# Interests API connect panrom

app.include_router(

    interests_router

)




# Careers API connect panrom

app.include_router(

    careers_router

)




# Roadmaps API connect panrom

app.include_router(

    roadmaps_router

)




# Career Skills API connect panrom

app.include_router(

    career_skills_router

)




# Career Interests API connect panrom

app.include_router(

    career_interests_router

)


app.include_router(

learning_resources_router

)

app.include_router(

user_progress_router

)

# Home page API

@app.get("/")

def home():

    return {

        "message":"Career Guidance Backend Running"

    }

