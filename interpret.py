def interpret(G):
	B = 65
	for h in G:
		if h == '+':
			B += 1
		elif h == '-':
			B -= 1
		elif h == '.':
			print(chr(B), end = "")
		else:
			continue