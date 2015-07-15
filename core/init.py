

# import Simbed.Core.Windows as W

# def test():
# 	p = W.SimplePlot()
# 	p.Show()
# 	for i in range(10): p.Plot(float(i**2),float(i**3)) 

'''
# Read input from stdin and provide input before running code

name = input('What is your name?\n')
print 'Hi, %s.' % name
'''

# N = int(input(""))
# nums = []
# for i in range(N):
# 	nums.append(int(input('')))
N = 3
nums = [1,2,3]
import itertools
subsets = []
for i in range(N):
	x = list(itertools.combinations(nums,i))
	subsets.extend(x)

maxors = []
for itm in subsets:
	x = None
	if len(itm) > 0:
		x = itm[0]
		for i in range(1,len(itm)):
			x ^= itm[i]
	maxors.append(x)


print(maxors)