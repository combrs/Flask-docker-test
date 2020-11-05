import logging
from flask import Flask
mytestteamflask = Flask(__name__)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    mytestteamflask.logger.handlers = gunicorn_logger.handlers
    mytestteamflask.logger.setLevel(gunicorn_logger.level)

@mytestteamflask.route('/')
def hello():
    mytestteamflask.logger.debug('5 my DEBUG message')
    mytestteamflask.logger.info('4 my INFO message')
    mytestteamflask.logger.warning('3 my WARNING message')
    mytestteamflask.logger.error('2 my ERROR message')
    mytestteamflask.logger.critical('1 my CRITICAL message')
    return "Hello World from Mike Lykov for test task for testTeam!"

if __name__ == '__main__':
    mytestteamflask.run()
