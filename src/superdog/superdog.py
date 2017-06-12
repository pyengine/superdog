import sys

from slackclient import SlackClient

logger = None

READ_WEBSOCKET_DELAY = 1

class SuperDog:
    def __init__(self, token, name, _logger):
        global logger
        logger = _logger
        self.token = token
        self.name = name
        self.client = SlackClient(self.token)
        self.botID = self.getBotId(self.name)
        self.capabilities = {}

        self.run()

    def run(self):
        if self.botID == None:
            sys.exit(1)
        self.at_bot = "<@%s>" % self.botID
        logger.info("Bot ID:%s" % self.botID)

        if not self.client.rtm_connect():
            logger.error("Bot is not connected")
            sys.exit(1)

        logger.info("Bot(%s) is started" % self.name)
        while True:
            (cmd, ch) = self.parseCmd(self.client.rtm_read())
            if cmd and ch:
                logger.debug("###########################")
                logger.debug("ch:%s" % ch)
                logger.debug("cmd:%s" % cmd)
                logger.debug("###########################")
                res = cmd.upper()
                self.client.api_call("chat.postMessage",channel=ch,text=res,as_user=True)

    def parseCmd(self, msg):
        if msg == None:
            return (None, None)
        if len(msg) <= 0:
            return (None, None)

        for output in msg:
            if output.has_key("text") and output.has_key("user"):
                logger.debug("text exist:%s" % output['text'])
                logger.debug("text exist(all):%s" % output)
                # Accept message only for me!
                #if self.at_bot in output['text']:
                if output['user'] == self.botID:
                    # This is my reply
                    pass
                else:
                    # return text after the @ mention, whitespace removed
                    #req = output['text'].split(self.at_bot)[1].strip()
                    req = output['text']
                    channel = output['channel']
                    return (req, channel)
            else:
                logger.warn("text does not exist:%s" % output)
        return (None, None)
    
    def getBotId(self, name):
        api_call = self.client.api_call("users.list")
        if api_call.get("ok"):
            users = api_call.get("members")
            for user in users:
                if "name" in user and user.get("name") == name:
                    return user.get("id")
        logger.error("Cannot find Bot ID by name:%s" % name)
        return None

