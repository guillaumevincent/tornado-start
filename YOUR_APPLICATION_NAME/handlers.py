import tornado.web
import tornado.escape


class Index(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")