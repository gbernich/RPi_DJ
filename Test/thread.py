#!/usr/bin/python
import sys, thread, time

def main():
	thread.start_new(threadDelay, (5,))
	for i in range(10000000):
		print i
		time.sleep(0.1)
	time.sleep(100000)


def threadDelay(d):
	time.sleep(5)
	print '             done'

main()
