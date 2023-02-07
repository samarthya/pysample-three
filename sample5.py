from flask import Flask


class MyFlaskApp:
    def __init__(self, name):
        self.app = Flask(name)

    def run(self):
        @self.app.route('/')
        def index():
            return "Hello, World!"
        self.app.run()


if __name__ == '__main__':
    app = MyFlaskApp(__name__)
    app.run()
