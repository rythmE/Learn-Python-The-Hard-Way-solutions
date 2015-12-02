# -*- coding: utf-8 -*-
formatter = "%s %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
print formatter % (
	"我有这个东西。", # 输出是乱码
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)