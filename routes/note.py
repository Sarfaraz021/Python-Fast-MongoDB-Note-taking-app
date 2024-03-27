from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity

note = APIRouter()

templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.Notes.mynotes.find({})

    newDoc = []
    for doc in docs:
        newDoc.append({
            "id": doc["_id"],
            "title": doc["title"],
            "desc": doc["desc"],
            # "important": doc["important"]
        })

    return templates.TemplateResponse("index.html", {"request": request, "newDoc": newDoc})


@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)

    # Set 'important' based on whether the form field 'important' is 'on'
    # formDict["important"] = True if formDict.get(
    #     "important") == "on" else False

    # Insert the form data into the database
    note = conn.Notes.mynotes.insert_one(formDict)

    # Return a success response
    return {"Success": True}
