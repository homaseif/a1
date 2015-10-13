#!/usr/bin/python

import sys
import copy
from copy import deepcopy


streets = {}
vertex = []
intersections = []
edge = []

class Error(Exception):
	pass
class UserInputError(Error):
	pass
class EndPointError(Error):
	pass
	
		

def inputAnalysis(input):
	""" Analysis of the input to separate
	 the command, street name and the coordinates
	 if applicable."""

	input1=' '.join(input.split())
	input2=input1.split('"')
	cmd=input2[0].strip()
	result = []
	if cmd not in ['a', 'c', 'r', 'g', '']:
		print>>sys.stderr, "Error: <", cmd, "> is not a valid command.\n",
	if cmd == 'a' or cmd == 'c' or cmd == 'r':
		if len(input2) != 3:
			print>>sys.stderr, "Error: Name of the street is not specified or specified without double quotation.\n",
		name=input2[1]
		if name == '':
			print>>sys.stderr, "Error: Name of the street can not be empty.\n",
			raise IndexError
		points= input2[2].strip()
		result.append(cmd)
		result.append(name)
		result.append(points)
	elif cmd == 'g':
		if len(input2) != 1:
			print>>sys.stderr, "Error: Street name or coordinates is/are specified for command 'g'.\n",
			raise IndexError
		result.append(cmd)
	return result


def pointsError(points):
	""" Analysis of coordinates
	 to find the errors."""

	if points[0] != '(':
		raise UserInputError
	n = len(points)
        if points[n-2] != ')':
		raise UserInputError
        i = 0
        flag = 0
        while points[i] != '\n':
		if points[i] == '(':
                	if flag == 1 or flag == 2:
				raise UserInputError
                        flag = 1
                        i=i+1
                elif points[i] == ',':
                       	if flag != 1:
				raise UserInputError
                        flag = 2
                        i=i+1
                elif points[i] == ')':
                        if flag != 2:
				raise UserInputError
                        flag = 3
                        i=i+1
                else:
			if points[i] != '-':
				if ord(points[i]) < ord('0') or ord(points[i])> ord('9'):
					raise ValueError
                        i=i+1

		
def extractNumbers(str):
	""" Receives (x,y), extracts x and y, 
	converts them to numbers and
	returns them as a list."""

	result=[]
	i=0
	number1=[]
    	number2=[]
    	while str[i]!=',':
		number1.append(str[i])
        	i=i+1
	if len(number1) == 0:
		raise ValueError
    	temp1=''.join(number1)
    	result.append(float(temp1))
    	i=i+1
    	while str[i]!=')':
        	number2.append(str[i])
        	i=i+1
	if len(number2) == 0:
		raise ValueError
    	temp2=''.join(number2)
    	result.append(float(temp2))
    	return result



def findIntersection(x1, y1, x2, y2, w1, z1, w2, z2):
	""" Receives the coordinates
	 of two line segments, finds
	 the intrsection of them and
	 returns the result as a list
	 if there is any intersection."""

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
			return [round(x,2),round(y,2)]


def printGraph(vertices, edges):
	""" Print the graph by
	 printing the vertices
	 and edges."""

	print>>sys.stdout, "V = {\n",
	for i in range(0, len(vertices)):
		a = int(vertices[i][0])
		b = int(vertices[i][1])
		if a == vertices[i][0]:
			print>>sys.stdout, " ", i+1, ": (",  a, ",",
		else:
			print>>sys.stdout, " ", i+1, ": (", vertices[i][0], ",",
		if b == vertices[i][1]:
			print>>sys.stdout, b, ")\n",
		else:
			print>>sys.stdout, vertices[i][1], ")\n",

	print>>sys.stdout, "}\n",

	print>>sys.stdout, "E = {\n",
	for i in range(0, len(edges)-1):
		print>>sys.stdout, " ", "<", edges[i][0]+1, ",", edges[i][1]+1, ">,\n",
	if len(edges) != 0:
		print>>sys.stdout, " ", "<",  edges[len(edges)-1][0]+1, ",", edges[len(edges)-1][1]+1, ">\n",
	print>>sys.stdout, "}"



while True:
  try:
	input = raw_input()
	analyzedInput = inputAnalysis(input)

	if analyzedInput[0] == 'a':
		if streets.has_key(analyzedInput[1]):
			print>>sys.stderr, "Error: 'a' specified for a street that already exists.\n",
		else:
			temp = analyzedInput[2]
			points = ''. join(temp.split())
			pointsError(points+'\n')
			twoPoint = points.split('(')

			if len(twoPoint) < 3:
				raise EndPointError

			analyzedNumbers = []
			for i in range(1, len(twoPoint)):
				analyzedNumbers.append(extractNumbers(twoPoint[i]))

			for i in range(1, len(analyzedNumbers)):
				if analyzedNumbers[i] == analyzedNumbers[i-1]:
					print>>sys.stderr, "Error: Entered repetitive consecutive coordinates.\n",
					raise IndexError

			streets[analyzedInput[1]] = analyzedNumbers

	elif analyzedInput[0] == 'c':
                if streets.has_key(analyzedInput[1]):
                        temp = analyzedInput[2]
                        points = ''. join(temp.split())
                        pointsError(points+'\n')
                        twoPoint = points.split('(')

			if len(twoPoint) <3:
				raise EndPointError

                        analyzedNumbers = []
                        for i in range(1, len(twoPoint)):
                                analyzedNumbers.append(extractNumbers(twoPoint[i]))

			for i in range(1, len(analyzedNumbers)):
                        	if analyzedNumbers[i] == analyzedNumbers[i-1]:
                                	print>>sys.stderr, "Error: Entered repetitive consecutive coordinates.\n",
					raise IndexError

                        streets[analyzedInput[1]] = analyzedNumbers

                else:
                        print>>sys.stderr, "Error: 'c' specified for a street that does not exist.\n",
	
	elif analyzedInput[0] == 'r':
		if analyzedInput[2] != '':
			print>>sys.stderr, "Error: Coordinates specified for command 'r'.\n",
		elif streets.has_key(analyzedInput[1]) == True:
			del streets[analyzedInput[1]]
		else:
			print>>sys.stderr, "Error: 'r' specified for a street that does not exist.\n",

	
	elif analyzedInput[0] == 'g':
		vertex = []
		edge = []
		intersections = []
		lines = []
		lines = copy.deepcopy(streets.values())
		for i in range(0, len(lines)):
			lines[i].append('\n')

		for i in range(0, len(lines)):
			for j in range(i+1, len(lines)):
				k = 0
				while lines[i][k+1] != '\n':
					l = 0
					while lines[j][l+1] != '\n':
						inters = findIntersection(lines[i][k][0], lines[i][k][1], lines[i][k+1][0], lines[i][k+1][1], lines[j][l][0], lines[j][l][1], lines[j][l+1][0], lines[j][l+1][1])
						if inters != None:
							if inters not in intersections:
								intersections.append(inters)
							if lines[i][k] != inters and lines[i][k+1] != inters:
								lines[i].insert(k+1, inters)
							if lines[j][l] != inters and lines[j][l+1] != inters:
								lines[j].insert(l+1, inters)
						l = l+1
					k= k+1

		# find edges and vertices
		vertex = copy.deepcopy(intersections)
		for x in intersections:
			for i in range(0, len(lines)):
				for j in range(0, len(lines[i])):
					if x == lines[i][j]:
						a = vertex.index(x)
						if j-1 >= 0: 
							if lines[i][j-1] not in vertex:
								vertex.append(lines[i][j-1])
							b = vertex.index(lines[i][j-1])
							minab = min(a,b)
							maxab = max(a,b)
							if [minab,maxab] not in edge:
								edge.append([minab,maxab])
						if j+1 < len(lines[i]): 
							if lines[i][j+1] not in vertex:
								vertex.append(lines[i][j+1])
							c = vertex.index(lines[i][j+1])
							minac = min(a,c)
							maxac = max(a,c)
							if [minac,maxac] not in edge:
								edge.append([minac,maxac])

		# print vertices and edges
		printGraph(vertex, edge)
		
  except EOFError:
     break
  except IndexError:
     pass
  except ValueError:
     print>>sys.stderr, "Error: Entered invalid input instead of numbers for coordinates. \n",
  except UserInputError:
     print>>sys.stderr, "Error: Entered wrong format of coordinates. (Missing parenthesis, comma or etc) \n",
  except EndPointError:
     print>>sys.stderr, "Error: Incomplete coordinates for the street, no end point.\n",
