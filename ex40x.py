t = (["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
					

class Song(object):

	def __init__(self):
		self.lyrics = t
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song()
					
happy_bday.sing_me_a_song()