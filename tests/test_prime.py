

from roro.math import prime


def test_ifnegativeisnotprime():
	assert not prime(-7)

def test_ifanevennumberisprime():
	for n in range(3,100):
		if n%2==0:
			assert not prime(n)

def test_ifalistofprimeisprime():
	l=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
	for n in l:
		assert prime(n)
