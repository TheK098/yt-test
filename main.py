from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import subprocess, shlex

app = FastAPI()

@app.get("/get_video_url")
def get_video_url(url: str = Query(..., description="YouTube URL")):
    try:
        cmd = [
            "yt-dlp",
            "-f",
            "bestvideo[height<=720]+bestaudio/best[height<=720]",
            "-g",
            url,
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        proc.check_returncode()
        links = proc.stdout.strip().split("\n")
        return {"video_url": links[0], "audio_url": links[1] if len(links) > 1 else None}
    except subprocess.CalledProcessError as e:
        return JSONResponse({"error": e.stderr.strip() or "yt-dlp failed"}, status_code=500)
    except Exception as ex:
        return JSONResponse({"error": str(ex)}, status_code=500)
