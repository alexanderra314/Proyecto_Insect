from fastapi import FastAPI
from contextlib import asynccontextmanager
from models import InsectModel, Framework
from insect_model_api import router as insect_model_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    print("here you should add the code you want to run when the app is starting")
    print("Loading the ML models.....")
    # create a dictionary to save a ref to the registered models (model garden)
    app.state.model_garden = dict()  #Jardin de modelos
    insect_model = InsectModel()   

    app.state.model_garden["insect-model"] = insect_model

    yield  
    # Clean up the ML models and release the resources
    print("here you should add the code you want to run when the app is shutting down")

# creating the API
print("api")
app = FastAPI(lifespan=lifespan)
app.include_router(insect_model_router, prefix="/insect-model")

# creating global routes
@app.get("/")
async def root():
    return {"message": "Welcome to the models API"}
