# import required module
import os
import shutil
# assign directory
directory = 'C:\\Users\\venuj\\OneDrive\\Desktop\\folder\\Screenshots'

# iterate over files in
# that directory
def namechange(x,v):
	#path = '/home/User/Documents'
	source = x
	destination = f'C:\\Users\\venuj\\OneDrive\\Desktop\\folder\\one\\{v}.png'
	dest = shutil.copyfile(source, destination)
	
v = 0
for filename in os.listdir(directory):
	f = os.path.join(directory, filename)
	# checking if it is a file
	if os.path.isfile(f):
		namechange(f,v)
		v+=1
		print(f)
