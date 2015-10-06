#!/usr/bin/python

import sys
streets = {}
vertex = set()

def inputAnalysis(input):
	input1=' '.join(input.split())
	input2=input1.split('"')
	cmd=input2[0].strip()
	result = []
	if cmd not in ['a', 'c', 'r', 'g']:
		print>>sys.stderr, "Error: <", cmd, "> is not a valid command.\n",
	if cmd == 'a' or cmd == 'c' or cmd == 'r':
		if len(input2) != 3:
			print>>sys.stderr, "Error: entered no double cotation-wrong format\n",
		temp=input2[1].strip()
		name = ' '.join(temp.split())
		if name == '':
			print>>sys.stderr, "Error: Name of street can not be empty.\n",
		points= input2[2].strip()
		result.append(cmd)
		result.append(name)
		result.append(points)
	elif cmd == 'g':
		if len(input2) != 1:
			print>>sys.stderr, "Error: entered points or street names for g.\n",
		result.append(cmd)
	return result


def pointsError(points):
	if points[0] != '(':
		print>>sys.stderr, "Error: wrong format input.\n",
	n = len(points)
        if points[n-2] != ')':
		print>>sys.stderr, "Error: Wrong format input.\n",
        i = 0
        flag = 0
        while points[i] != '\n':
		if points[i] == '(':
                	if flag == 1 or flag == 2:
				print>>sys.stderr, "Error: Wrong format input.\n",
                        flag = 1
                        i=i+1
                elif points[i] == ',':
                       	if flag != 1:
				print>>sys.stderr, "Error: Wrong format input.\n",
                        flag = 2
                        i=i+1
                elif points[i] == ')':
                        if flag != 2:
				print>>sys.stderr, "Error: Wrong format input.\n",
                        flag = 3
                        i=i+1
                else:
			if points[i] != '-':
				if ord(points[i]) < ord('0') or ord(points[i])> ord('9'):
					print>>sys.stderr, "Error: not number.\n",
                        i=i+1


		
def extractNumbers(str):
	result=[]
	i=0
	number1=[]
    	number2=[]
    	while str[i]!=',':
		number1.append(str[i])
        	i=i+1
    	temp1=''.join(number1)
    	result.append(float(temp1))
    	i=i+1
    	while str[i]!=')':
        	number2.append(str[i])
        	i=i+1
    	temp2=''.join(number2)
    	result.append(float(temp2))
    	return result

def findIntersection(x1, y1, x2, y2, w1, z1, w2, z2):
	a1 = y2 - y1
	b1 = x1 - x2
	c1 = a1*x1 + b1*y1
	a2 = z2 - z1
	b2 = w1 - w2
	c2 = a2*w1 + b2*z1
	slopesDif = a1*b2 - a2*b1
	if (slopesDif != 0):
		x = (b2*c1 - b1*c2)/slopesDif
		y = (a1*c2 - a2*c1)/slopesDif
		if x >= min([x1,x2]) and x <= max([x1,x2]) and x >= min([w1,w2]) and x <= max([w1,w2]) and y >= min([y1,y2]) and y <= max([y1,y2]) and y >= min([z1,z2]) and y <= max([z1,z2]):
			return [x,y]


while True:
  try:
	input = raw_input()
	analyzedInput = inputAnalysis(input)

	if analyzedInput[0] == 'a':
		if streets.has_key(analyzedInput[1]):
			print>>sys.stderr, "Error: This street exists.\n",
		else:
			temp = analyzedInput[2]
			points = ''. join(temp.split())
			pointsError(points+'\n')
			twoPoint = points.split('(')
			analyzedNumbers = []
			for i in range(1, len(twoPoint)):
				analyzedNumbers.append(extractNumbers(twoPoint[i]))
			for i in range(0,len(analyzedNumbers)):
                                for j in range(i+1,len(analyzedNumbers)):
                                        if analyzedNumbers[i]==analyzedNumbers[j]:
                                                print>>sys.stderr, "Error: same points for one street.\n",
			streets[analyzedInput[1]] = analyzedNumbers

	elif analyzedInput[0] == 'c':
                if streets.has_key(analyzedInput[1]):
                        temp = analyzedInput[2]
                        points = ''. join(temp.split())
                        pointsError(points+'\n')
                        twoPoint = points.split('(')
                        analyzedNumbers = []
                        for i in range(1, len(twoPoint)):
                                analyzedNumbers.append(extractNumbers(twoPoint[i]))
			for i in range(0,len(analyzedNumbers)):
            			for j in range(i+1,len(analyzedNumbers)):
                			if analyzedNumbers[i]==analyzedNumbers[j]:
                   				print>>sys.stderr, "Error: same points for one street.\n",
                        streets[analyzedInput[1]] = analyzedNumbers

                else:
                        print>>sys.stderr, "Error: This street does not exist.\n",
	
	elif analyzedInput[0] == 'r':
		if analyzedInput[2] != '':
			print>>sys.stderr, "Error: r command does not come with points\n",
		if streets.has_key(analyzedInput[1]):
			del streets[analyzedInput[1]]
		else:
			print>>sys.stderr, "Error: This street does not exist.\n",

	
	elif analyzedInput[0] == 'g':
		lines = []
		lines.extend(streets.values())
		for i in range ()		
	print streets			
  except EOFError:
	break
