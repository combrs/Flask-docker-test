import logging
from flask import Flask
mybaikalteamflask = Flask(__name__)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    mybaikalteamflask.logger.handlers = gunicorn_logger.handlers
    mybaikalteamflask.logger.setLevel(gunicorn_logger.level)

@mybaikalteamflask.route('/')
def hello():
    mybaikalteamflask.logger.debug('5 my DEBUG message')
    mybaikalteamflask.logger.info('4 my INFO message')
    mybaikalteamflask.logger.warning('3 my WARNING message')
    mybaikalteamflask.logger.error('2 my ERROR message')
    mybaikalteamflask.logger.critical('1 my CRITICAL message')
    return "Hello World from Mike Lykov for test task for BaikalTeam!"

if __name__ == '__main__':
    mybaikalteamflask.run()
