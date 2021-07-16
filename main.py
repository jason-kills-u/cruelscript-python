from sys import argv
from interpret import interpret

argc = len(argv) - 1

if argc < 1:
	print("CruelScript Version 1.3.1 Final.")
	G = input(">>> ")
	if G == 'exit' or "quit" or "x" or "X":
		break
	interpret(G)
	print(end = "\n")
else:
	h = open(argv[1], "r")
	interpret(h.read())
