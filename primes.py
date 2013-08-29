# Sieve of Eratosthenes in Python 2.7
# 8.28.13 Andrew Montes

numbers = {}
primes = []
limit = 50000

print "BUILDING LIST OF PRIMES UP TO LIMIT: %i" % limit

for x in range(2, limit+1):				# build a dictionary with numbers 2 to limit as keys 
	numbers[x] = 1 					# set each number's value to true (i.e. prime)

print "..."
for x in range(2, limit+1):				# for every number until limit...
	if numbers[x] == 1:				# if that number is prime...
		y = x 					# iterate through multiples, starting with square
		while x*y<limit+1:			# while the multiple is less than limit...
			numbers[x*y] = 0		# set the multiple's value to false (i.e. not prime)
			y = y+1

print "..."
for x in range(2, limit+1):				# iterate back through the numbers
	if numbers[x] == 1:				# if value is still true (i.e. prime)
		primes.append(x)			# add the number to the list of primes

for x in xrange(0, len(primes), 10):			# iterate through the list of primes in groups of ten
	print '\t', primes[x:x+10]			# and print. enjoy your prime numbers
