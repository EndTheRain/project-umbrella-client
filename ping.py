import time, os, requests
from util import url, auth, setStatus

def ping():
	r = requests.get(url + 'dispensers/ping', headers=auth)
	if r.status_code != 200:
		setStatus(false)
	else
		setStatus(true)
	time.sleep(300)
	ping()
