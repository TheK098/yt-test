FROM python:3.10
RUN pip install yt-dlp
COPY . .
CMD ["bash", "run.sh"]
