from nose.tools import *
from ex49.parser import *


def test_Sentence():
	sentence = Sentence(('noun', 'I'), ('verb', 'love'), ('noun', 'you'))
	assert_equal(sentence.subject, 'I')
	assert_equal(sentence.verb, 'love')
	assert_equal(sentence.object, 'you')

	
def test_peek_match():
	word_list_1 = [('noun', 'I'), ('verb', 'love'), ('noun', 'you')]
	word_list_2 = []
	word_list_3 = [('stop', 'At'), ('stop', 'this'), ('direction', 'place'),
				('noun', 'I'), ('verb', 'love'), ('noun', 'you')]
	
	assert_equal(peek(word_list_1), 'noun')
	assert_equal(peek(word_list_2), None)
	
	assert_equal(match(word_list_1, 'noun'), ('noun', 'I'))
	assert_equal(match(word_list_1, 'noun'), None)
	assert_equal(match(word_list_2, 'noun'), None)


def test_skip():
	word_list_1 = [('noun', 'I'), ('verb', 'love'), ('noun', 'you')]
	word_list_2 = []
	word_list_3 = [('stop', 'At'), ('stop', 'this'), ('direction', 'place'),
				('noun', 'I'), ('verb', 'love'), ('noun', 'you')]
				
	assert_equal(skip(word_list_1, 'noun'), None)
	assert_equal(skip(word_list_3, 'stop'), None)
	assert_equal(skip(word_list_2, 'stop'), None)
	
	
def test_parse_verb_object():
	word_list_11 = [('noun', 'I'), ('verb', 'love'), ('noun', 'you')]
	word_list_12 = [('noun', 'I'), ('verb', 'love'), ('noun', 'you')]
	word_list_31 = [('stop', 'At'), ('stop', 'this'), ('direction', 'place'),
				('noun', 'I'), ('verb', 'love'), ('noun', 'you')]
	word_list_32 = [('stop', 'At'), ('stop', 'this'), ('direction', 'place'),
				('noun', 'I'), ('verb', 'love'), ('noun', 'you')]				
	word_list_5 = [('stop', 'Right'), ('stop', 'here'),('verb', 'Fuck'), 
				('noun', 'you')]
	word_list_6 = [('stop', 'Right'), ('stop', 'now'), ('noun', 'I'),
				 ('verb', 'eat'), ('stop', 'an'), ('noun', 'apple')]

	assert_equal(parse_verb(word_list_5), ('verb', 'Fuck'))
	assert_raises(ParserError, parse_verb, word_list_11)	
	assert_raises(ParserError, parse_verb, word_list_31)	

	word_list_4 = [('stop', 'Right'), ('stop', 'here'),('verb', 'Fuck'), 
				('noun', 'you')]	
	assert_equal(parse_object(word_list_12), ('noun', 'I'))
	assert_equal(parse_object(word_list_32), ('direction', 'place'))
	assert_equal(parse_object(word_list_6), ('noun', 'I'))
	assert_raises(ParserError, parse_object, word_list_4)	
	

def test_parse_subject():
	word_list_41 = [('verb', 'Fuck'), ('noun', 'you')]
	word_list_42 = [('verb', 'Fuck'), ('noun', 'you')]
	word_list_43 = [('verb', 'Fuck'), ('noun', 'you')]

	assert_equal(parse_subject(word_list_41, ('noun', 'I')).subject, 'I')
	assert_equal(parse_subject(word_list_42, ('noun', 'I')).verb, 'Fuck')
	assert_equal(parse_subject(word_list_43, ('noun', 'I')).object, 'you')
	
def test_parse_sentence():
	word_list_2 = []
	word_list_3 = [('stop', 'At'), ('stop', 'this'), ('direction', 'place'),
				('noun', 'I'), ('verb', 'love'), ('noun', 'you')]
	word_list_51 = [('stop', 'Right'), ('stop', 'here'),('verb', 'Fuck'), 
				('noun', 'you')]
	word_list_52 = [('stop', 'Right'), ('stop', 'here'),('verb', 'Fuck'), 
				('noun', 'you')]
	word_list_53 = [('stop', 'Right'), ('stop', 'here'),('verb', 'Fuck'), 
				('noun', 'you')]
	word_list_61 = [('stop', 'Right'), ('stop', 'now'), ('noun', 'I'),
				 ('verb', 'eat'), ('stop', 'the'), ('noun', 'apple')]
	word_list_62 = [('stop', 'Right'), ('stop', 'now'), ('noun', 'I'),
				 ('verb', 'eat'), ('stop', 'the'), ('noun', 'apple')]
	word_list_63 = [('stop', 'Right'), ('stop', 'now'), ('noun', 'I'),
				 ('verb', 'eat'), ('stop', 'the'), ('noun', 'apple')]

	assert_equal(parse_sentence(word_list_51).subject, 'player')
	assert_equal(parse_sentence(word_list_52).verb, 'Fuck')
	assert_equal(parse_sentence(word_list_53).object, 'you')
	
	assert_equal(parse_sentence(word_list_61).subject, 'I')
	assert_equal(parse_sentence(word_list_62).verb, 'eat')
	assert_equal(parse_sentence(word_list_63).object, 'apple')
	
	assert_raises(ParserError, parse_sentence, word_list_3)	
	assert_raises(ParserError, parse_sentence, word_list_2)		