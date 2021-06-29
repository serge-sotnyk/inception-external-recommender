from ariadne.contrib import *
from ariadne.server import Server
from ariadne.util import setup_logging

setup_logging()

server = Server()
server.add_classifier("the", TheClassifier())  # 'the' as a tag value
server.add_classifier("the_term", TheClassifier('TERM'))  # 'TERM' as a tag value

app = server.app

if __name__ == "__main__":
    server.start(debug=True, port=40022)
