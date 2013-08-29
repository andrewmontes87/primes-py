# Sieve of Eratosthenes
# 8.28.13 Andrew Montes

numbers = {}
primes = []
limit = 10000

print "BUILDING LIST OF PRIMES UP TO LIMIT: %i" % limit

for x in range(2, limit+1):				# build a dictionary with numbers 2 to limit as keys 
	numbers[x] = 1 						# set each number's value to true (i.e. prime)

print "..."
for x in range(2, limit+1):				# for every number until limit...
	for y in range(2, limit+1-x):		# take every other number until limit...
		if x*y<limit+1:					# if the multiple is below limit...
			numbers[x*y] = 0   			# set the multiple's value to false (i.e. not prime)

print "..."
for x in range(2, limit+1):				# iterate back through the numbers
	if numbers[x] == 1:					# if value is still true (i.e. prime)
		primes.append(x)				# add the number to the list of primes

for x in xrange(0, len(primes), 8):		# iterate through the list of primes in groups of 8
	print '\t', primes[x:x+8]			# and print. enjoy your prime numbers