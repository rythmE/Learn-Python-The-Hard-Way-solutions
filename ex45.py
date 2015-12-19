# coding: utf-8 
from sys import exit
from random import randint

class Scene():
	
	def enter(self):
		exit(1)
	
class Engine():
	
	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
	
class Fail(Scene):
	
	def enter(self):
		print "Sorry you failed, and please try again."
		exit(1)
	
class House(Scene):
	
	def enter(self):
		print "You are in a house, and you want to go outside to play."
		print "There are two doors in front of you, and which one do you prefer?"
		
		door = raw_input("> ")
		n = randint(1,2)
		
		if door == str(n):
			print "You chose the right door."
			return 'doorway'
		else:
			return 'fail'
	
class Doorway(Scene):
	
	def enter(self):
		print "You are in a doorway now."
		print "Do you regret?"
		
		ans = raw_input("> ")
		
		if ans == "no": # if ans == ("no" or "No"): 不行
			print "OK, plase go ahead."
			return 'hall'
		elif ans == "yes": # if ans == ("yes" or "Yes"): 不行
			print "OK, you can go back."
			return 'house'
		else:
			return 'fail'
	
class Hall(Scene):
	
	def enter(self):
		print "Now you are in the hall."
		print "Go through the gate and you'll be free."
		
		ans = raw_input("Go?\n> ")
		
		if ans == "yes":
			print "Congratulations! You win!"
			exit(1)
		elif ans == "no":
			print "OK, you can go back."
			return 'doorway'
		else:
			return 'fail'
	
class Map():
	
	scenes = { "house": House(),
	"doorway": Doorway(),
	"hall": Hall(),
	"fail": Fail()
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		return self.scenes[scene_name]
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
	
if __name__ == "__main__":
	a_map = Map("house")
	a_game = Engine(a_map)
	a_game.play()