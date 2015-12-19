direction = ['north', 'south', 'east', 'west', 'down', 'up',
			'left', 'right', 'back']
verb = ['go', 'stop', 'kill', 'eat']
stop = ['the', 'in', 'of', 'from', 'at', 'it']
noun = ['door', 'bear', 'princess', 'cabinet']
types = {'direction': direction, 'verb': verb, 'stop': stop, 
		'noun': noun}

def scan(strings):
	type_words = []
	words = strings.split()
	for word in words:
		lower_word = word.lower()
		if scan_word(types, lower_word) != None:
			(t, w) = scan_word(types, lower_word)
			type_words.append((t, word))
		elif convert_numbers(word) != None:
			type_words.append(('number', int(word)))
		else:
			type_words.append(('error', word))
	return type_words
	
def scan_word(types, word):
	for (type_name, type) in types.items():
		for i in range(len(type)):
			if word == type[i]:
				return (type_name, type[i])

def convert_numbers(s):
	try:
		return int(s)
	except ValueError:
		return None