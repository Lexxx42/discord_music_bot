from bot.handlers import client
from bot import TOKEN

if __name__ == "__main__":
    client.run(TOKEN, log_handler=None)
