from flask import Flask
from routes import routes
import logging
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
logging.basicConfig(filename='record.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
routes.create_routes(app)
if __name__ == '__main__':
    app.run()
