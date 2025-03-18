from fastapi import FastAPI
import uvicorn


app = FastAPI(title="Speech Transcription API")

# Register the health check and transcribe routers
#app.include_router(transcribe.router)

@app.get("/")
def read_root():
    return {"message": "FastAPI setup successful"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
