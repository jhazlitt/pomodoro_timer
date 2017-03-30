import math
import os
import time

open('round_count.txt', 'w').write('0')

def waitSeconds(seconds):
	while True:
		if (time.time() - startTime >= seconds):
			os.system('aplay doorbell.wav || afplay doorbell.wav')
			break

while True:
	os.system('clear')		
	roundCount = int(open('round_count.txt').readlines()[0])
	print ('Pomodoro round ' + str(roundCount + 1))
	startTime = time.time()
	waitSeconds(25 * 60)
	roundCount += 1
	waitSeconds(5 * 60)
	if (roundCount == 4):
		os.system('clear')
		print ('Break time')
		roundCount = 0
		waitSeconds(25 * 60)
	open('round_count.txt', 'w').write(str(roundCount))
