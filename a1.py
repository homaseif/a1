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
	if cmd == 'a' or 'c' or 'r':
		if len(input2) != 3:
			print>>sys.stderr, "Error: entered no double cotation-wrong format\n",
		name=input2[1].strip()
		if name == '':
			print>>sys.stderr, "Error: Name of street can not be empty.\n",
		points= input2[2].strip()
		result.append(cmd)
		result.append(name)
		result.append(points)
	elif cmd == 'g':
		if len(input2) != 1:
			print>>sys.stderr, "Error: entered points for g.\n",
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


while True:
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
			
