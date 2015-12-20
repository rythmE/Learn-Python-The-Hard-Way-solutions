from ex48.parser import *
from ex48 import lexicon

while True:
	words = raw_input("Please enter a sentence:\n")
	word_list = lexicon.scan(words)
	sentence_tuple = parse_sentence(word_list)
	print sentence_tuple.subject, sentence_tuple.verb, sentence_tuple.object