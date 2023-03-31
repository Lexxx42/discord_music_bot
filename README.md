# discord_music_bot

+ Simple discord music bot that plays YouTube music in your channel.

---

## Used libraries:

+ discord.py==2.1.0
  Discord API: + URL https://discordpy.readthedocs.io/en/stable/index.html
+ Really cool stuff here: https://github.com/Rapptz/discord.py
+ Coded with Python 3.11.1

---
## Available commands:

+ join - bot joins user's voice chat

``` shell
@music-bot join CHANNEL-NAME
```

+ play - bot play's music from local directory

``` shell
@music-bot play /home/USER/Downloads/MUSIC.mp3
```

+ yt + URL - bot play's music from YouTube. Works with predownloading

``` shell
@music-bot yt https://www.youtube.com/watch?v=LINK
```

+ stream + URL - start playing music from YouTube. Simply copy-paste link from YouTube. Works without predownloading

``` shell
@music-bot stream https://www.youtube.com/watch?v=LINK
```

+ volume + number - changes the volume to number %

``` shell
@music-bot volume 45
```

+ stop - stop playing and disconnect from voice channel

``` shell
@music-bot stop
```

---

## How to start the bot?

+ Quick guide to setup: https://realpython.com/how-to-make-a-discord-bot-python/
+ Use quick guide to the point when the code begins

1. Get the Discord token from Discord Developer Portal
2. Install all requirements from requirements.txt

``` shell
pip install -r requirements.txt  
```

3. Create file .env in project root
4. Copy the line into your .env file with token provided by Discord Developer Portal

``` shell
DISCORD_TOKEN=YOUR_BOT_TOKEN  
```

5. Install FFmpeg: https://ffmpeg.org/download.html


# New features with docker

## If there is an error about lack of access, add current user to the docker group:

```shell
sudo usermod -a -G docker [user]
newgrp docker
```

## Use this sequence of commands to run the container:

1. To run the application in docker, you need to install docker-compose:

```shell
sudo apt install docker-compose 
```

2. Clone the repository

```shell
git clone https://github.com/Lexxx42/discord_music_bot
```

3. Change directory to project dir

```shell
cd discord_music_bot/
```

4. Add your token for discord bot

```shell
nano .env
```

```
DISCORD_TOKEN=YOUR_BOT_TOKEN
```


Don't forget to save changes!

5. Start the build

```shell
docker-compose up --build
```
