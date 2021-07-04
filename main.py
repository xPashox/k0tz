import sys
import os
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands
from dislash import SlashClient

# EventLoopPolicy
if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

if __name__ == "__main__":
    # Inicializar Bot
    bot = commands.Bot(command_prefix='_',
                       description="Bot de prueba", help_command=None)
    slash = SlashClient(bot)

    # Cogs
    bot.load_extension("utils.commands")
    bot.load_extension("utils.listeners")

    # Ejecutar Bot
    load_dotenv()
    bot.run(os.getenv('BOT_TOKEN'))
