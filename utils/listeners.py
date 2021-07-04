import discord
from discord.ext import commands


class Listener(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener("on_ready")
    async def status(self):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="_help"))
        print("Inicializado!")

    @commands.Cog.listener("on_message")
    async def respuesta(self, msg):
        counter = 0
        if (not msg.author.bot and False):
            text = msg.content
            channel = msg.channel
            author = msg.author
            await msg.delete()
            # Embed Message
            embed = discord.Embed(
                title="Sugerencia: #{}".format(counter),
                description=text,
                color=0xFFEF94
            )
            embed.set_footer(
                text="Sugerencia enviada por: {}".format(author.display_name),
                icon_url=author.avatar_url
            )
            await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Listener(bot))
