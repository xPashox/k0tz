import discord
from discord.ext import commands
from dislash import *


class Command(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @slash_commands.command(
        name="ayuda",
        description="Muestra los comandos disponibles",
        guild_ids=[679205771405426720])
    async def ayuda(self, ctx):
        embed = discord.Embed(
            title="Lista de Comandos",
            description="""
            -> **_sugerencia** *<canal>*\n
            ```\n_sugerencia\t#general\n```
            """)
        await ctx.send(content="test", embeds=[embed])

    @commands.command()
    async def sugerencia(self, ctx):
        channels = [c for c in ctx.guild.text_channels]
        msg = await ctx.send(
            "**Selecciona el Canal de Sugerencias**",
            components=[
                SelectMenu(
                    custom_id="suggests",
                    placeholder="Selecciona un Canal",
                    max_values=1,
                    options=[SelectOption("#{}".format(c.name), c.id)
                             for c in channels]
                )
            ]
        )
        # Esperar que salga del menu
        opt = await msg.wait_for_dropdown()
        # Enviar Respuesta
        ids = [option.value for option in opt.select_menu.selected_options]
        channel = opt.channel
        await msg.delete()
        # TODO: Guardar canal seleccionado en modelo y validar errores.
        await channel.send(f"Canal Seleccionado: <#{ids[0]}>")


def setup(bot):
    bot.add_cog(Command(bot))
