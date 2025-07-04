from logging import basicConfig 
from logging import DEBUG
from logging import FileHandler
from logging import StreamHandler
from logging import getLogger

basicConfig(format='%(levelname)s:%(asctime)s: %(message)s', datefmt='%Y-%m-%d %I:%M:%S',encoding='utf-8', level="INFO", handlers=[StreamHandler()])
logger = getLogger()
