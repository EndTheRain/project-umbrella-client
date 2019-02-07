import requests
from util import url, auth, setStatus

def borrowUmb(cardId, umbId):
	try:
		payload = {'cardId': cardId}
		req = requests(url + '/umbrellas/' + umbId + '/borrow', data=payload, headers=auth)
		if req.status == 200:
			# TODO: actually dispense the umbrella
		else:
			setStatus(False)
	except requests.ConnectionError:
		setStatus(False)
