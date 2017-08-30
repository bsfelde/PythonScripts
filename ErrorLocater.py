def segmentsplitter():
	#Split data by segments
	with open('7114942841.txt', 'r+') as f:
	 	for line in f:
			segment = line.split('~')

		return segment

def elementsplitter(segment):
	#Split segments by elements, return them in a list
	splitdata = [letter.split('*') for letter in segment]
	return splitdata 

def manFinder(data):
	for segment in data:
		if segment[0] == "MAN":
			if len(segment[2]) != 20:
				print '*'.join(segment)

#-------------------------------------

def main():

	print '\n\n'

	segments = segmentsplitter()

	dater = elementsplitter(segments)

	manFinder(dater)

if __name__ == '__main__':
     main()