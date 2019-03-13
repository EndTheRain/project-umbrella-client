import os, redis
from requests.auth import HTTPBasicAuth

db_host = os.environ['ETR_DB_URL']
db_port = os.environ['ETR_DB_PORT']
db_password = os.environ['ETR_DB_PASSWORD']
db = redis.Redis(host=db_host, port=db_port, password=db_password)

url = os.environ['ETR_API_URL']
auth = HTTPBasicAuth(os.environ['ETR_DISP_ID'], os.environ['ETR_SECRET'])

online = False

def setStatus(status):
	online = status
	# TODO: toggle LED indicator on dispenser

def getStatus():
	return online

def msTime():
	return int(round(time.time() * 1000))

def queueReturn(umbId):
	r.set(umbId, msTime())

def dequeueReturn(umbId):
	r.delete(umbId)
