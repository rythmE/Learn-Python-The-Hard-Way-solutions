from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            nextscene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(nextscene_name)


class Death(Scene):

    def enter(self):
        print "You are dead233333333333"
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print "You are in CentralCorridor, and what do you do?"
        print "Laser, Bridge or Escape?"
        action = raw_input("> ")
        if action == "Bridge":
            return 'dead'
        elif action == "Escape":
            return 'dead'
        elif action == "Laser":
            return 'Laser'
        else:
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "You are in LaserWeaponArmory, and guess a number?"
        print "1~6, 3 times."
        guess = raw_input("> ")
        num1 = "%d" % (randint(1, 6))
        times = 1

        while guess != num1 and times < 3:
            print "please guess agian!"
            times += 1
            guess = raw_input("> ")

        if guess == num1:
            print "You are a lucky dog, and you can go to the bridge."
            return 'Bridge'
        else:
            print "Sorry, but you have to die."
            return 'dead'


class TheBridge(Scene):

    def enter(self):
        print "You are in TheBridge, and the alien found you."
        print "What do you do?"
        print "Battle, Escape or Wet pants?"
        action = raw_input("> ")

        if action == "Battle":
            return 'dead'
        elif action == "Escape":
            return 'Escape'
        elif action == "Wet pants":
            return 'dead'
        else:
            return 'Bridge'


class EscapePod(Scene):

    def enter(self):
        print "You are in LaserWeaponArmory, and guess a number?"
        print "1~3, 1 time."
        guess = raw_input("> ")
        num2 = "%d" % randint(1, 3)

        if guess == num2:
            print "Lucky dog, you win."
            exit(1)
        else:
            print "Sorry, you took a wrong pod."
            return 'dead'


class Map(object):

    scenes = {'Laser': LaserWeaponArmory(),
              'Bridge': TheBridge(),
              'Escape': EscapePod(),
              'dead': Death(),
              'central_corridor': CentralCorridor()
              }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes[scene_name]

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
