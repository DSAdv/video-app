from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/video/trim")
def trim_video():
    """Input video, start time, end time.
    Output trimmed video URL from S3."""
    return {"message": "Trimmed video"}


@app.get("/video/download")
def download_video():
    return {"message": "Downloaded video"}
