from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Speech Transcription API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Speech Transcription API!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
