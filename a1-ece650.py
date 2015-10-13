#!/usr/bin/python


import sys
import copy
from copy import deepcopy
db=[]
res=[]
vertex=[]

def cartes(str):
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
    return result
     

def modify(line):
         line1=[] 
         line1.append(line[0])
         if len(line)==1:
            raise AssertionError
         if line[2]=='"':
            i=3
            name=[]
            while line[i]!='"':
                  name.append(line[i])
                  i=i+1
                  if i==len(line):
                     raise AttributeError
            name1=''.join(name)
            name2=''.join(name1.split())
            line1.append(name2)
            i=i+2
            cartp=[]
            if i<len(line):
               while i<len(line):
                     cartp.append(line[i])
                     i=i+1
               cartp1=''.join(cartp)
               cartp2=cartp1.split()
               line1.extend(cartp2)
    
            return line1;

    

while True:
 try:
  line=raw_input()
  if len(line)!=0:
   command=['a','c','r','g','	',' ']
   if line[0] not in command:
      print>>sys.stderr,"Error: <",line[0],"> is not an invalid command.\n",
 
   if line[0]=='a':
      try:
        st=modify(line)
        st.pop(0)
        l=1
        tempo=copy.deepcopy(st)
        for i in range(1,len(tempo)):
            for j in range(0,len(tempo[i])-1):
                if tempo[i][j]==')' and tempo[i][j+1]=='(':
                   t1=tempo[i]
                   t2=t1.split(')')
                   if t2[len(t2)-1]!='':
                      raise IndexError
                   t2.pop(len(t2)-1)
                   for k in range(0,len(t2)):
                       t2[k]=t2[k]+')'
                   for k in range(0,len(t2)):
                       st.insert(l,t2[k])
                       l=l+1
                   st.pop(l)
                   l=l-1
                   break
            l=l+1
        for i in range(1,len(st)):
            checking=cartes(st[i])
        for i in range (0,len(db)):
            if (db[i][0]==st[0]):
               raise KeyError
        if len(st)<3:
           raise AssertionError()
        db.append(st)
        for i in range(1,len(st)):
            if st[i] not in vertex:
              vertex.append(st[i])

      except AttributeError:
        print>>sys.stderr,"Error: Entered name of the street in a wrong format.\n",
      except IndexError:
        print>>sys.stderr,"Error: Entered a wrong format of coordinates.\n",
      except ValueError:
        print>>sys.stderr,"Error: Entered invalid input instead of number for coordinates.\n",
      except KeyError:
        print>>sys.stderr,"Error: Entered a street that exists.\n",
      except AssertionError:
        print>>sys.stderr,"Error: At least 2 points should be entered along with the name of a street.\n",

   elif line[0]=='c':     
      try:
        st=modify(line)
        if len(db)==0:
           print>>sys.stderr,"Error: 'c' specified for a street that does not exist.\n",
        flag=False
        for i in range (0,len(db)):
           flag=True
           if (db[i][0]==st[1]):
              flag=False
              st.pop(0)
              l=1
              tempo=copy.deepcopy(st)
              for q in range(1,len(tempo)):
                  for j in range(0,len(tempo[q])-1):
                      if tempo[q][j]==')' and tempo[q][j+1]=='(':
                       t1=tempo[q]
                       t2=t1.split(')')
                       if t2[len(t2)-1]!='':
                          raise IndexError
                       t2.pop(len(t2)-1)
                       for k in range(0,len(t2)):
                           t2[k]=t2[k]+')'
                       for k in range(0,len(t2)):
                           st.insert(l,t2[k])
                           l=l+1
                       st.pop(l)
                       l=l-1
                       break
                  l=l+1

              for j in range(1,len(st)):
                 checking=cartes(st[j])
              if len(st)<3:
                 raise AssertionError
              db.pop(i)
              db.append(st)
              for i in range(1,len(st)):
                    if st[i] not in vertex:
                       vertex.append(st[i])           
              break
        if flag==True:
           print>>sys.stderr,"Error: 'c' specified for a street that does not exist.\n",
      except TypeError:
        print>>sys.stderr,"Error: Entered name of the street in a wrong format.\n",
      except IndexError:
        print>>sys.stderr,"Error: Entered a wrong format of coordinates.\n",
      except ValueError:
        print>>sys.stderr,"Error: Entered invalid input instead of number for coordinates.\n",
      except AssertionError:
        print>>sys.stderr,"Error: At least 2 points should be entered along with the name of a street.\n", 

   elif line[0]=='r':
      try:
         st=modify(line)
         if len(st)>2:
            raise IOError()
         if len(db)==0:
           print>>sys.stderr,"Error: 'r' specified for a street that does not exist.\n",
         flag=False
         for i in range (0, len(db)):
            flag=True
            if(db[i][0]==st[1]):
               flag=False
               db.pop(i)
               break
         if flag==True:
            print>>sys.stderr,"Error: 'r' specified for a street that does not exist.\n",
      except AssertionError:
         print>>sys.stderr,"Error: Name of the street can not be empty.\n",
      except TypeError:
         print>>sys.stderr,"Error: Entered name of the street in a wrong format.\n",
      except IOError:
         print>>sys.stderr,"Error: Command 'r' only comes with name of a street.\n",


   elif line[0]=='g':
      try:
         if len(line)>1:
            raise IOError
         intersect=[]
         db1=[]
         db1=copy.deepcopy(db)
         i=0
         equ=[]
         while i < len(db):
            j=1
            equ.append([])
            while j<(len(db[i])-1):
              a=cartes(db[i][j])
              g=cartes(db[i][j+1])
              res=[]
              res.extend(a)
              res.extend(g)
              if res[2]-res[0]==0:
                 m=float("inf")
                 z=res[0]
              else:
                 m = (res[3]-res[1])/(res[2]-res[0])
                 z = res[1]-m*res[0]
              equ[i].append(m)
              equ[i].append(z)
              j=j+1
            i=i+1

         for i in range(0,len(db)-1):
             j=0
             while j<(len(equ[i])-1):
                 for k in range(i+1,len(equ)):
                     l=0 
                     while l<(len(equ[k])-1):
                         if equ[i][j]!=equ[k][l]:
                            if equ[i][j]==float("inf"):
                               x=equ[i][j+1]
                               y=(equ[k][l]*x)+equ[k][l+1]
                            if equ[k][l]==float("inf"):
                               x=equ[k][l+1]
                               y=(equ[i][j]*x)+equ[i][j+1]
                            if equ[i][j]!=float( "inf") and equ[k][l]!=float("inf"):
                               x = (equ[k][l+1]-equ[i][j+1])/(equ[i][j]-equ[k][l])
                               y= (equ[i][j]*x)+equ[i][j+1]
                            res1=[]
                            c=cartes(db[i][j/2+1])
                            r=cartes(db[i][j/2+2])
                            res1.extend(c)
                            res1.extend(r)
                            res2=[]
                            s=cartes(db[k][l/2+1])
                            p=cartes(db[k][l/2+2])
                            res2.extend(s)
                            res2.extend(p)
                            if ((res1[0]<=x<=res1[2] or res1[2]<=x<=res1[0]) and (res2[0]<=x<=res2[2] or res2[2]<=x<=res2[0])) and ((res1[1]<=y<=res1[3] or res1[3]<=y<=res1[1]) and (res2[1]<=y<=res2[3] or res2[3]<=y<=res2[1])):
                               if (x).is_integer() and (y).is_integer():
                                  x=int(x)
                                  y=int(y)
                               point="("+str(x)+","+str(y)+")"
                               if point not in intersect:
                                  intersect.append(point)
                               if point not in vertex:
                                  vertex.append(point)
                               if db1[i][j/2+2]==db[i][j/2+2]:
                                  if db1[i][j/2+2]!=point and db1[i][j/2+1]!=point:
                                     db1[i].insert(j/2+2,point)
                               if db1[i][j/2+2]!=db[i][j/2+2]:
                                  q=j/2+2
                                  while q<len(db1[i]):
                                        res3=[]
                                        h=cartes(db1[i][q-1])
                                        m=cartes(db1[i][q])
                                        res3.extend(h)
                                        res3.extend(m)
                                        if (res3[0]<=x<=res3[2] or res3[2]<=x<=res3[0]) and (res3[1]<=y<=res3[3] or res3[3]<=y<=res3[1]):
                                           if db1[i][q]!=point and db1[i][q-1]!=point:
                                              db1[i].insert(q,point)
                                              break
                                           else:
                                              break                               
                                        q=q+1

 
                               if db1[k][l/2+2]==db[k][l/2+2]:
                                  if db1[k][l/2+2]!=point and db1[k][l/2+1]!=point:   
                                     db1[k].insert(l/2+2,point)
                               if db1[k][l/2+2]!=db[k][l/2+2]:
                                  q=l/2+2
                                  while q<len(db1[k]):
                                        res4=[]
                                        n=cartes(db1[k][q-1])
                                        o=cartes(db1[k][q])
                                        res4.extend(n)
                                        res4.extend(o)
                                        if (res4[0]<=x<=res4[2] or res4[2]<=x<=res4[0]) and (res4[1]<=y<=res4[3] or res4[3]<=y<=res4[1]):
                                           if db1[k][q]!=point and db1[k][q-1]!=point:
                                              db1[k].insert(q,point)
                                              break
                                           else:
                                              break
                                        q=q+1
                             
                         l=l+2
                 j=j+2

         pvertex=[]
         pvertex.append([])
         pvertex.append([])
         pedge=[]
         for i in range(0,len(intersect)):
             for j in range(0,len(db1)):
                 tmp1=vertex.index(intersect[i])
                 if intersect[i]==db1[j][1]:
                    pvertex[0].append(db1[j][2])
                    tmp5=vertex.index(db1[j][2])
                    pvertex[1].append(tmp5)
                    pedge.append(tmp1)
                    pedge.append(tmp5)
                 if intersect[i]==db1[j][len(db1[j])-1]:
                    pvertex[0].append(db1[j][len(db1[j])-2])
                    tmp6=vertex.index(db1[j][len(db1[j])-2])
                    pvertex[1].append(tmp6)
                    pedge.append(tmp1)
                    pedge.append(tmp6)

                 for k in range(2,len(db1[j])-1):
                     if intersect[i] not in pvertex[0]:
                        pvertex[0].append(intersect[i])
                        pvertex[1].append(tmp1)
                     if intersect[i]==db1[j][k]:
                        pvertex[0].append(db1[j][k-1])
                        tmp2=vertex.index(db1[j][k-1])
                        pvertex[1].append(tmp2)
                        pedge.append(tmp1)
                        pedge.append(tmp2)
                        if (k+1)==(len(db1[j])-1):
                           pvertex[0].append(db[j][-1])
                           tmp3=vertex.index(db[j][-1])
                           pvertex[1].append(tmp3)
                           pedge.append(tmp1)
                           pedge.append(tmp3)

                        else:
                           pvertex[0].append(db1[j][k+1])
                           tmp3=vertex.index(db1[j][k+1])
                           pvertex[1].append(tmp3)
                           pedge.append(tmp1)
                           pedge.append(tmp3) 

         pv=[]
         pv.append([])
         pv.append([])
         for i in range(0,len(pvertex[0])):
             if pvertex[0][i] not in pv[0]:
                pv[0].append(pvertex[0][i])
                pv[1].append(pvertex[1][i])

         pg=[]
         try:
            pg.append(pedge[0])
            pg.append(pedge[1])
            i=2
            while i<len(pedge):
                j=0
                while j<i:
                      checker = True
                      if (pedge[i]==pedge[j+1] and pedge[i+1]==pedge[j]):
                         checker = False
                         break
                      j=j+2
                if checker == True:
                   pg.append(pedge[i])
                   pg.append(pedge[i+1])
                i=i+2
         except IndexError:
                pass

         print>>sys.stdout,"V = {\n",
         for i in range(0,len(pv[0])):
           if pv[0][i] in intersect:
             res=cartes(pv[0][i])
             print>>sys.stdout,"  ",pv[1][i],": (","%.2f"%res[0],",","%.2f"%res[1],")"
           else:
             print>>sys.stdout,"  ",pv[1][i],": ", pv[0][i]
         print>>sys.stdout, "}"
         print>>sys.stdout,"E = {"
         i=0
         while i<len(pg):
             print>>sys.stdout,"  <",pg[i],",",pg[i+1],">,"
             i=i+2
         print>>sys.stdout,"}"


      except IOError:
             print>>sys.stderr,"Error: Command 'g' does not come with name of a street or anythong else.\n",
 except EOFError:
  break
