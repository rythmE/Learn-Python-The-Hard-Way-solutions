# -*- coding: utf-8 -*-
from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count, f):
	print line_count, f.readline(),

#readline() 函数返回的内容中包含文件本来就有的 \n，而 print 
#在打印时又会添加一个\n，这样一来就会多出一个空行了。解决方法
#是在 print 语句结尾加一个逗号 ,，这样 print 就不会把它自己的
#\n 打印出来了。
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print "Now the current_line is", current_line
print_a_line(current_line, current_file)

current_line += 1
print "Now the current_line is", current_line
print_a_line(current_line, current_file)

current_line += 1
print "Now the current_line is", current_line
print_a_line(current_line, current_file)