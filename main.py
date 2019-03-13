from ping import ping
from util import getStatus

def main():
    while True:
    	cardId = input("cardId: ")
    	if getStatus():
    		# TODO: get RFID tag and call borrow
    # TODO: return umbrellas

if __name__ == '__main__':
    main()
