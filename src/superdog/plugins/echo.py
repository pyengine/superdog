from plugin import Plugin

class Echo(Plugin):
    def __init__(self, bot, channel):
        Plugin.__init__(self, bot, channel)


    def run(self):
        self.reply("Pong")
