import logging
import traceback
from optparse import OptionParser

from superdog import SuperDog

logger = None

def main():
    token = None
    global logger
    parser = OptionParser()
    parser.add_option("-t", "--token", dest="token", help="SLACK API TOKEN")
    parser.add_option("-n", "--name", dest="name", help="SLACK Bot Name")
    parser.add_option("-L", "--logging", dest="logging", help="logging level(DEBUG|INFO|WARNING|ERROR|CRITICAL)")
    try:
        (options, args) = parser.parse_args()
        level = logging.INFO
        if options.logging:
            LEVEL = {'DEBUG':logging.DEBUG,
                'WARNING': logging.WARNING,
                'INFO': logging.INFO,
                'ERROR': logging.ERROR,
                'CRITICAL':  logging.CRITICAL}
            level = LEVEL[options.logging]
        logging.basicConfig(format='[%(levelname)s] %(message)s', level=level)
        logger = logging.getLogger('bixby-bot')

        if options.token:
            logger.info("Slack API token:%s" % options.token)
            token = options.token
        else:
            logger.info("Slack API token is not specified")
            token = raw_input("Slack API token: ")
        if options.name:
            logger.info("Slack Bot Name:%s" % options.name)
            name = options.name
        else:
            logger.info("Slack Bot Name is not specified")
            name = raw_input("Slack Bot Name: ")
 
    except:
        logger.error("There is error!")
        traceback.print_exc()

    S = SuperDog(token, name, logger)

if __name__ == "__main__":
    main()	
