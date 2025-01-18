from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()
from bert import keyword_pull_article, extract_keywords, NER_with_SciBERT

class TextInput(BaseModel):
    text: str
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend's URL in production
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/save-keywords/")
async def save_keywords(request: Request):
    data = await request.json()
    with open("keywords.json", "w") as f:
        json.dump(data, f)
    return {"message": "Keywords saved successfully!"}
@app.post("/extract_keywords")
def extract_keywords_endpoint(input: TextInput):
    keywords = NER_with_SciBERT(input.text)
    return {"keywords": keywords}
