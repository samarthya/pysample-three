import unittest
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


class FlaskTestCase(unittest.TestCase):
    def test_hello(self):
        tester = app.test_client(self)
        response = tester.get("/", content_type="html/text")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, World!")


if __name__ == "__main__":
    unittest.main()
