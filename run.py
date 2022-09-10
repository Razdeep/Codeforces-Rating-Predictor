from app import *
import logging
import os

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()

if __name__ == '__main__':
	port = os.getenv('PORT', 5000)
	logger.info(f'Application is supposed to run on {port}')
	app.run(host='0.0.0.0', port=port, debug=False)