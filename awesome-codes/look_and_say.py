#!/usr/bin/python3


'''
	look_and_say
	From:TuTu
'''


def times_to_play(N):

	a = "1"

	for _ in range(N - 1):

		b = ""
		c = 1

		for i in range(1, len(a)):
			if a[i] == a[i-1]:

				c += 1
			else:

				b += str(c) + a[i-1]
				c = 1

		b += str(c) + a[-1]
		a = b

	print(len(a))


n = 30

times_to_play(n)



