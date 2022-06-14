from flask import Flask

class ApiEntrypoint:
    def __init__(self, host: str, port: int, debug: bool):
        self.app = Flask(host=host, port=port, debug=debug)
        