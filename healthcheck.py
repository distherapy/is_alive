import pandas as pd
import os

def conv():
	read_file = pd.read_csv('/***/***/subd.txt')
	read_file.to_csv (r'/***/***/subd0.csv', index=None)
conv()

def impping():
	lines = []
	imp = open('/***/***/subd0.csv')
	#exp = open('/***/***/subd0.txt', 'a')
	for line in imp:
		res = os.system("ping -c 2 " + line)
		if res == 0:
			lines.append('\n' + line + 'is alive \n')
		else:
			pass
	print(lines)
impping()
