from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from routes.note import note


app = FastAPI()
note.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(note)
