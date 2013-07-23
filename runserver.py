import logging
import tornado.web
import tornado.ioloop
import tornado.httpserver
import settings as config
from tornado_start.handlers import Index


class Application(tornado.web.Application):
    """Tornado web class. Create all the routes used by tornado_start"""

    def __init__(self):
        handlers = [
            (r"/", Index)
        ]

        settings = {
            "template_path": config.TEMPLATE_DIR,
            "static_path": config.STATIC_DIR,
            "debug": config.DEBUG,
            "cookie_secret": config.COOKIE_SECRET,
            "login_url": config.LOGIN_URL
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    application = Application()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(config.PORT, '0.0.0.0')
    logging.info('listening on port: %s' % config.PORT)
    tornado.ioloop.IOLoop.instance().start()