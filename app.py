from fastapi import FastAPI, File, UploadFile, Form, Request , HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse

import base64
import requests 
import io
from PIL import Image
import os
import logging
from dotenv import load_dotenv


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")



if not GROQ_API_KEY:
    raise ValueError("GROQ API KEY is not set in the env file")

@app.get("/",response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/upload_and_query")
async def upload_and_query(image: UploadFile = File(...), query:str = Form(...)):
    try:
        image_content = await image.read()
        if not image_content:
            raise HTTPException(status_code=400, detail="Empty File")
        encoded_image = base64.b64encode(image_content).decode("utf-8")

        try:
            img = Image.open(io.BytesIO(image_content))
            img.verify()
        except Exception as e:
            logger.error(f"Invalid Image format: {str(e)}")
            raise HTTPException(status_code=400,detail=f"Invalid Image format: {str(e)}")
        
        messages = [
            {
                "role":"user",
                "content":[
                    {"type": "text", "text": query},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}
                    ]
            }
        ]
        
        def make_api_request(model):
            
            response = requests.post(
                GROQ_API_URL,
                json={
                    "model": model,
                    "messages": messages,
                    "max_tokens": 1000
                },
                headers={
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json"
                },
                timeout=30
            )

            return response
        
        Llama_4_Scout = make_api_request("meta-llama/llama-4-scout-17b-16e-instruct")
        Llama_4_Maverick  = make_api_request("meta-llama/llama-4-maverick-17b-128e-instruct")

        responses = {}
        for model,response in [("llama_scout",Llama_4_Scout),("llama_maverick",Llama_4_Maverick)]:
            if response.status_code == 200:
                results = response.json()
                answer = results["choices"][0]["message"]["content"]
                logger.info(f"Processed response from {model} API: {answer[:100]}...")
                responses[model] = answer
            else:
                logger.error(f"Error from {model} API: {response.status_code} - {response.text}")
                responses[model] = f"Error from {model} API: {response.status_code}"
        
        return JSONResponse(status_code=200,content=responses)

    except HTTPException as he:
        logger.error(f"HTTP exception: {str(he)}")
        raise he
    except Exception as e:
        logger.error(f"An unexpected error occured:{str(e)}")
        raise HTTPException(status_code=500,detail=f"An unexpected error occured:{str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port= 8000)