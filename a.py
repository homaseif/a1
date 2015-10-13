#!/usr/bin/python

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

print findIntersection(0, 0, 1, 0, 0, 1, 1, 1)
