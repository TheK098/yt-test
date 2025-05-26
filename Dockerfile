FROM python:3.11-slim

# system packages for ffmpeg (merging) if ever needed
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt yt-dlp

WORKDIR /app
COPY . .

# expose 8080 (Fly default)
ENV PORT=8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
