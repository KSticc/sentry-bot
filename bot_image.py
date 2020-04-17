from discord.ext import commands
import discord

class Image(commands.Cog):

	def __init__(self, bot):
			self.bot = bot


#    @commands.command(name='begone',help="OWNER ONLY, I don't belong in this world",hidden=1)
#    @commands.is_owner()
	@commands.command(name='noarms',help='Conveys a strong cursed energy')
	async def noarms(self, ctx):
		await ctx.send(file=discord.File('gifs/PlayerWalkRightBobNoArms.gif'))

	@commands.command(name='epic',help='Conveys a strong Gamer™ energy')
	async def epic(self,ctx):
		await ctx.send(file=discord.File('videos/epic.mp4'))


def setup(bot):
	bot.add_cog(Image(bot))