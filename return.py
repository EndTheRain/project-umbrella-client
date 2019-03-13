import requests
from util import url, auth, setStatus, msTime, queueReturn, dequeueReturn

def returnUmb(umbId):
	try:
		payload = {'returnAt': msTime()}
		req = requests(url + '/umbrellas/' + umbId + '/return', data=payload, auth=auth)
		if req.status == 200:
			dequeueReturn(umbId)
		else:
			queueReturn(umbId)
			time.sleep(60)
			returnUmb(umbId)
	except requests.ConnectionError:
		setStatus(False)

