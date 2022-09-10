from app import *
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)