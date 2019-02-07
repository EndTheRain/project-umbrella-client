import os, redis

db_host = os.environ['ENDTHERAIN_DB_URL']
db_port = os.environ['ENDTHERAIN_DB_PORT']
db_password = os.environ['ENDTHERAIN_DB_PASSWORD']
db = redis.Redis(host=db_host, port=db_port, password=db_password)

url = os.environ['ENDTHERAIN_API_URL']
auth = {'Authorization': os.environ['ENDTHERAIN_API_KEY']}

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
