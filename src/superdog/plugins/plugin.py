# This is Plugin class

class Plugin:
    def __init__(self, bot, channel):
        """
        @param bot : bot object
        """
        self.bot = bot
        self.channel = channel

    def run(self):
        pass

    def reply(self, msg):
        self.bot.api_call("chat.postMessage", channel=self.channel, text=msg, as_user=True)

