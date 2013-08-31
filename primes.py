# Sieve of Eratosthenes 2.0 in Python 2.7
# 8.28.13 Andrew Montes


########## EDIT THE LIMIT HERE #########
### TRY NOT TO GO OVER A FEW MILLION ###
limit = 1000000 ########################
########################################


### FUNCTIONS ###

def build_primes_list(primes, limit):
	numbers = {}
	print "\nBUILDING LIST OF PRIMES UP TO LIMIT: %i" % limit
	for x in range(2, limit+1):				# build a dictionary with numbers 2 to limit as keys 
		numbers[x] = 1 					# set each number's value to true (i.e. prime)

	print "\n...\n"
	for x in range(2, limit+1):				# for every number until limit...
		if numbers[x] == 1:				# if that number is prime...
			y = x 					# iterate through multiples, starting with square
			while x*y<limit+1:			# while the multiple is less than limit...
				numbers[x*y] = 0		# set the multiple's value to false (i.e. not prime)
				y += 1

	print "\n...\n"
	for x in range(2, limit+1):				# iterate back through the numbers
		if numbers[x] == 1:				# if value is still true (i.e. prime)
			primes.append(x)			# add the number to the list of primes

def list_primes(primes):
	print "PRINTING PRIMES\n"
	for x in xrange(0, len(primes), 10):			# iterate through the list of primes in groups of ten
		print '\t', primes[x:x+10]			# and print. enjoy your prime numbers

def twin_primes(primes, limit):
	twins = []
	pairs = 0
	print "\nBUILDING LIST OF TWIN PRIMES UP TO LIMIT: %i" % limit
	print "\n...\n"
	for x in range(1, len(primes)-1):			# for every number in primes
		if primes[x]+2 == primes[x+1]:			# if the next prime is the first plus two
			twins.append(primes[x])			# add both to twins list
			twins.append(primes[x+1])
			pairs += 1
	print "PRINTING TWIN PRIMES\n"
	for x in xrange(0, len(twins), 4):			# iterate through the list of twins in groups of four
		print '\t', twins[x:x+2], '   ', twins[x+2:x+4]		# print in pairs
	return pairs

def cousin_primes(primes, limit):
	cousins = []
	pairs = 0
	print "\nBUILDING LIST OF COUSIN PRIMES UP TO LIMIT: %i" % limit
	print "\n...\n"
	if len(primes) > 5:
		for x in range(1, len(primes)-4):					# for every number in primes
			if primes[x]+4 == primes[x+1] or primes[x]+4 == primes[x+2]:	# if the number plus 4 is prime
				cousins.append(primes[x])				# add both to cousins list
				cousins.append(primes[x]+4)
				pairs += 1
		print "PRINTING COUSIN PRIMES\n"
		for x in xrange(0, len(cousins), 4):			# iterate through the list of cousins in groups of four
			print '\t', cousins[x:x+2], '   ', cousins[x+2:x+4]		# print in pairs
	else:
		cousins = [3, 7]
		pairs = 1
		print '\t', cousins
	return pairs

def sum_digits(number):
  result = 0
  while number:									# sum digits using modular division
    digit = number % 10 						# found this somewhere on stack overflow.
    result += digit
    number /= 10
  return result

def additive_primes(primes, limit):
	additive = [2, 3, 5, 7]
	x=4
	print "\nBUILDING LIST OF ADDITIVE PRIMES UP TO LIMIT: %i" % limit
	print "\n...\n"

	while x < len(primes) and sum_digits(primes[x]) < primes[-1]:
		if sum_digits(primes[x]) in primes[:25]:			# if the sum of the digits is also prime
			additive.append(primes[x])	
		x += 1						# add it to additive list
	print "PRINTING ADDITIVE PRIMES\n"
	for x in xrange(0, len(additive), 5):			# iterate through the list of twins in groups of five
		print '\t', additive[x:x+5]
	return len(additive)

def print_totals(primes, twins_total, cousins_total, additive_total, limit):
	print "\nTotal of %i prime numbers under %i." % (len(primes), limit)
	print "\nTotal of %i twin prime pairs under %i." % (twins_total, limit)
	print "\nTotal of %i cousins prime pairs under %i." % (cousins_total, limit)
	print "\nTotal of %i additive prime numbers under %i." % (additive_total, limit)


### MAIN ###

def main(limit):
	primes = []

	build_primes_list(primes, limit)
	list_primes(primes)
	twins_total = twin_primes(primes, limit)
	cousins_total = cousin_primes(primes, limit)
	additive_total = additive_primes(primes, limit)
	print_totals(primes, twins_total, cousins_total, additive_total, limit)


### RUNTIME ###

main(limit)
