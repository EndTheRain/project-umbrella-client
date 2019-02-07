import os

url = os.environ['ENDTHERAIN_API_URL']
auth = {'Authorization': os.environ['ENDTHERAIN_API_KEY']}

online = False

def setStatus(status):
	online = status
	# TODO: toggle LED indicator on dispenser

def getStatus():
	return online
