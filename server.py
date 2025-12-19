from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
import uvicorn
import os
import shutil
from agent import AnchorAgent

app = FastAPI()

# Initialize Agent
try:
    agent = AnchorAgent()
except Exception as e:
    print(f"Error initializing Agent: {e}")
    agent = None

class ChatRequest(BaseModel):
    message: Optional[str] = None
    context: Optional[str] = None

@app.post("/api/chat")
async def chat_endpoint(
    message: Optional[str] = Form(None),
    context: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None)
):
    if not agent:
        raise HTTPException(status_code=503, detail="Agent not initialized")

    image_path = None
    if image:
        # Save temp file
        os.makedirs("temp_uploads", exist_ok=True)
        image_path = f"temp_uploads/{image.filename}"
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

    response = agent.process_input(text_input=message, image_path=image_path, context=context)

    # Cleanup image
    if image_path and os.path.exists(image_path):
        os.remove(image_path)

    return {"response": response}

@app.get("/api/reflection")
async def reflection_endpoint():
    if not agent:
        raise HTTPException(status_code=503, detail="Agent not initialized")
    return {"response": agent.generate_daily_reflection()}

# Mount Static Files (Frontend)
os.makedirs("static", exist_ok=True)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
