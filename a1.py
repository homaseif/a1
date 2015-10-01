#!/usr/bin/python

import sys
streets = []

def inputAnalysis(input):
	input1=' '.join(input.split())
	input2=input1.split('"')
	cmd=input2[0].strip()
	result = []
	if cmd not in ['a', 'c', 'r', 'g']:
		print>>sys.stderr, "Error: <", cmd. "> is not a valid command.\n",
	if cmd == 'a' || 'c' || 'r':
		if len(input2) != 3:
			print>>sys.stderr, "Error: entered no double cotation-wrong format",
		name=input2[1].strip()
		points= input[2].strip()
		result.append(cmd)
		result.append(name)
		result.append(points)
	elif cmd == 'g':
		if len(input2) != 1
			print>>sys.stderr, "Error: entered points for g",
		result.append(cmd)
	return result

"""def pointsAnalysis(points)
	if len(points) == 0 || len(points) == 1:
		print>>sys.stderr, "Error: entered one or no point",
	temp = points.split()
	for i in range (0, len(points)):
		
	
		
def extraxtNumbers(str):
    result=[]
    i=1
    if str[0]!='(':
       raise IndexError
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
    if (i+1)<len(str):
       raise IndexError    
    return result"""

while True:
	input = raw_input()
	analyzedInput = inputAnalysis(input)
	if analyzedInput[0] == 'a':
		streets.append(analyzedInput[1])
		temp = analyzedInput[2]
		points = '', join(temp.split())
		if points[0] != '(':
			print>>sys.stderr, "Error: wrong format input",
		n = len(points)
		if points[n-1] != ')':
			print>>sys.stderr, "Error: Wrong format input",
		i = 0
		flag = 0
		while points[i] != '\n':
			if points[i] == '(':
				if flag != 3 || flag != 0:
					print>>sts.stderr, "Error: Wrong format input",
				flag = 1
				i++
			elif points[i] == ',':
				if flag != 1:
					print>>sys.stderr, "Error: Wrong format input",
				flag = 2
				i++
			elif points[i] == ')':
				if flag != 2:
					print>>sys.stderr, "Error: Wrong format input",
				flag = 3
				i++					
			else:
				if ord(points[i]) < ord('0') || ord(points[i])> ord('9')
					print>>sys.stderr, "Error: not number",
				i++
		
		
	elif analyzedInput[0] == 'c':
	elif analyzedInput[0] == 'r':
	elif analyzedInput[0] == 'g':
		

