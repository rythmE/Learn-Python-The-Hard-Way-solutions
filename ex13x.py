# -*- coding: utf-8 -*-
# 奇怪的程序，总是说缺argv，写了几个就说缺几个
from sys import argv

fifth = raw_input("Your fifth variable is:")
script, first, second, third, fourth, fifth = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth
print "Your last variable is:", fifth

