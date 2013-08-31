# Sieve of Eratosthenes 2.1 in Python 2.7
# 8.28.13 Andrew Montes


########## EDIT THE LIMIT HERE #########
### TRY NOT TO GO OVER A FEW MILLION ###
limit = 10000000 ########################
########################################


### FUNCTIONS ###

def build_primes_list(primes, limit):
	numbers = {}
	print "\nBUILDING LIST OF PRIMES UP TO LIMIT: %i" % limit
	for x in range(2, limit+1):				# build a dictionary with numbers 2 to limit as keys 
		numbers[x] = True 					# set each number's value to true (i.e. prime)

	print "\n...\n"
	for x in range(2, limit+1):				# for every number until limit...
		if numbers[x] == True:				# if that number is prime...
			y = x 					# iterate through multiples, starting with square
			while x*y<limit+1:			# while the multiple is less than limit...
				numbers[x*y] = False		# set the multiple's value to false (i.e. not prime)
				y += 1

	print "\n...\n"
	for x in range(2, limit+1):				# iterate back through the numbers
		if numbers[x] == True:				# if value is still true (i.e. prime)
			primes.append(x)			# add the number to the list of primes

def list_primes(primes):
	print "PRINTING PRIMES\n"
	for x in xrange(0, len(primes), 10):			# iterate through the list of primes in groups of ten
		print '\t', primes[x:x+10]			# and print. enjoy your prime numbers

def twin_primes(twins, primes, limit):
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

def cousin_primes(cousins, primes, limit):
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

def additive_primes(additive, primes, limit):
	x=4
	print "\nBUILDING LIST OF ADDITIVE PRIMES UP TO LIMIT: %i" % limit
	print "\n...\n"

	while x < len(primes) and sum_digits(primes[x]) < primes[-1]:
		if sum_digits(primes[x]) in primes[:25]:			# if the sum of the digits is also prime
			additive.append(primes[x])			# add it to additive list
		x += 1
	print "PRINTING ADDITIVE PRIMES\n"
	for x in xrange(0, len(additive), 5):			# iterate through the list of twins in groups of five
		print '\t', additive[x:x+5]
	return len(additive)

def print_totals(primes, twins_total, cousins_total, additive_total, limit):
	print "\nTotal of %i prime numbers under %i." % (len(primes), limit)
	print "\nTotal of %i twin prime pairs under %i." % (twins_total, limit)
	print "\nTotal of %i cousins prime pairs under %i." % (cousins_total, limit)
	print "\nTotal of %i additive prime numbers under %i." % (additive_total, limit)

def primality_test(primes, twins, cousins, additive, limit):
	print "\nEnter a positive number below %i." % limit
	print "Enter a zero to quit."
	number = raw_input('>>')							# accepts user input, checks if a number is prime
	number = check_int(number)					# error-checking first
	if number == "!":
		print "\nERROR: must be an integer"
		return True
	elif number > limit:
		print "\nERROR: integer must be below %i" % limit
		return True
	elif number > 0 and number < limit:				# if it's a positive int beneath the limit
		if number in primes:						# is it prime?
			print "\n%i is a prime number." % number 		# yes it is!
			if number in twins:							# is it a twin?
				print "\n%i is part of a twin pair." % number 	# yes it is!
				if number+2 in twins:							# print the pair
					print "%i  %i" % (number, number+2)
				if number-2 in twins:
					print "%i  %i" % (number-2, number)
			if number in cousins:							# is it a cousin?
				print "\n%i is part of a cousin pair." % number 	# yes it is!
				if number+4 in cousins:						# print the pair
					print "%i  %i" % (number, number+4)
				if number-4 in cousins:
					print "%i  %i" % (number-4, number)
			if number in additive:						# is it an additive?
				print "\n%i is an additive prime." % number 	# yes it is!
				print "The sum of the digits is %i, a prime number." % sum_digits(number)
		else:
			print "\n%i is not a prime number.\n" % number 		# no it isn't!
		return True
	elif number < 0:
		print "\nERROR: must be a positive integer"
		return True
	else:
		print "\nGoodbye\n"					# if it's not an error and not a positive int
		return False 					# it must be 0 for quit. return false to end while loop

def check_int(number):
	try:								# simple error-checking helper function
		return int(number)				# found this on stack overflow 
	except ValueError:
		return "!"


### MAIN ###

def main(limit):
	primes = []
	twins = []
	cousins = []
	additive = [2, 3, 5, 7]

	build_primes_list(primes, limit)		
	list_primes(primes)
	twins_total = twin_primes(twins, primes, limit)
	cousins_total = cousin_primes(cousins, primes, limit)
	additive_total = additive_primes(additive, primes, limit)
	print_totals(primes, twins_total, cousins_total, additive_total, limit)

	while primality_test(primes, twins, cousins, additive, limit) == True:
		continue


### RUNTIME ###

main(limit)
