# Sieve of Eratosthenes
# 8.28.13 Andrew Montes

numbers = {}
primes = []
limit = 1000

print "PRINTING PRIMES UP TO LIMIT: %i" % limit

for x in range(limit+1):
	numbers[x] = 1

for x in range(limit+1):
	for y in range(limit+1-x):
		if x > 1 and y > 1 and (x*y<limit+1):
			numbers[x*y] = 0   # not prime

for x in range(limit+1):
	if numbers[x] == 1:
		primes.append(x)

for x in xrange(0, len(primes), 8):
	print '\t', primes[x:x+8]