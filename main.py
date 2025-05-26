from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import subprocess

app = FastAPI()

@app.get("/get_video_url")
def get_video_url(url: str = Query(..., description="YouTube URL")):
    try:
        result = subprocess.run(
            [
                "yt-dlp",
                "-f",
                "bestvideo[height<=720]+bestaudio/best[height<=720]",
                "-g",
                url
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        video_urls = result.stdout.strip().split("\n")
        return {
            "video_url": video_urls[0],
            "audio_url": video_urls[1] if len(video_urls) > 1 else None,
        }
    except subprocess.CalledProcessError as e:
        return JSONResponse({"error": e.stderr.strip()}, status_code=500)
