
def countFreq(file, min_value=1):
	"""Return a list of pairs containing passwords and the number of times they were used.

	Args:
		file (filename):
			A file containing usernames followed by tabs followed by passwords.

	Optional:
		min_value (int):
			Limit returned list to only contain passwords with frequencies greater
			than or equal to min_value
	"""
	dic = {}
	curr_file = open(file, 'r')
	for line in curr_file:
		password = line.split('\t')[-1][:-1]  # Indexing to -1 removes the \n from each string
		if password in dic:
			dic[password] += 1
		else:
			dic[password] = 1
	curr_file.close()
	for key, item in list(dic.items()):
		if item < min_value:
			del(dic[key])
	ret = sorted(((key, value) for (key,value) in dic.items()), reverse = True)
	return ret