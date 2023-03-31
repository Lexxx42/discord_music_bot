# base image
FROM debian:bullseye-slim

# installing of work directory (by default) in image
WORKDIR /discord-bot

# installing of requirements
RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		python3-pip \
        ffmpeg \
	; \
	rm -rf /var/lib/apt/lists/*

# copying token data to the container
RUN touch .env

# copying project to image
COPY . .

# installing requirements from pip
RUN pip3 install -r requirements.txt

# start script after container start
ENTRYPOINT ["python3", "app.py"]