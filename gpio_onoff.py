import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
GPIO.setwarnings(False)

def on(PIN):
	GPIO.setup(PIN, GPIO.OUT) # GPIO Assign mode
	GPIO.output(PIN, GPIO.LOW) # out
	GPIO.output(PIN, GPIO.HIGH) # on

def off(PIN):
	GPIO.setup(PIN, GPIO.OUT) # GPIO Assign mode
        GPIO.output(PIN, GPIO.HIGH) # out
        GPIO.output(PIN, GPIO.LOW) # off


def main(state,PIN):
#	GPIO.setup(PIN, GPIO.OUT) # GPIO Assign mode
	if state == "on":
		print ("running on")
        	on(PIN)
	else:
        	if state == "off":
			print ("running off")
			off(PIN)

if __name__ == '__main__':
	state = sys.argv[1]
	PIN = int(sys.argv[2])
	main(state,PIN)

#GPIO.cleanup()
#sys.exit()

