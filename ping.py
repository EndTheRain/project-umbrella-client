import time, os, requests
from util import url, auth, setStatus

def ping():
	try:
		req = requests.get(url + 'dispensers/ping', headers=auth)
		if req.status_code == 200:
			setStatus(True)
		else
			setStatus(False)
	except requests.ConnectionError:
		setStatus(False)
	time.sleep(300)
	ping()
