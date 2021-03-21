import pandas as pd
import os

def conv():
	read_file = pd.read_csv('/****/****/subd.txt')
	read_file.to_csv (r'/****/****/subd.csv', index=None)
  
def impping():
	with open('/****/****/subd.csv') as imp:
		for line in imp:
			res = os.system("ping -c 1 " + line)
			if res == 0:
				print(line + ' is alive')
			else:
				print(line + ' is dead')
        
conv()
impping()
