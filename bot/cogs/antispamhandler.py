from antispam import AntiSpamHandler
from discord.ext.commands import Cog, Bot


class AntiSpam(Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @Cog.listeners("on_message")
    def spam_handler(self, message):
        handler = AntiSpamHandler(self.bot)
        await handler.propagate(message)
        await self.bot.process_commands(message)
 
def setup(bot: Bot):
    bot.add_cog(Antispam(bot))
    
