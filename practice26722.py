"""for i in range (15):
     print(i)
outputs
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
"""
"""for i in range(15):
     print(i,end=" ")
     
outputs
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 
   """
"""for i in range (1,5):
     for j in range (1,5):
          print(j,end="")
     print()
output
1234
1234
1234
1234


"""
"""
for i in range (1,5):
     for j in range (1,i+1):
          print(j,end="")
     print()
     
output
1
12
123
1234
"""

"""
for roshan in range (5,0,-1):
     for obj in range (roshan,0,-1):
          print (obj,end=" ")
     print()
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""


"""for i in range(1,6):
     for j in range(1,i+1):
          print("1" ,end=" ")
     print()
"""
"""
j=11
for i in range (6):
     print(j**i)
output
1
11
121
1331
14641
161051

"""
"""
i=1
j=1
for x in range (7):
     print(i)
     j=j*10+1
     i=j*j
output
1
121
12321
1234321
123454321
12345654321
1234567654321
"""

""" for i in range (1,6):
     for j in range (1,i+1):
          print(j,end=" ")
     print()
output
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 """

"""s=0
for i in range(1,6):
  for j in range(i,6):
      print(" "*s,end=" ")
      print (j,end=" ")
  print(" ")

output
 1  2  3  4  5  
 2  3  4  5  
 3  4  5  
 4  5  
 5
 """
"""
for i in range(2,6):
  for j in range(1,11):
      print(j,end=" ")
  else:
      print()
output
1 2 3 4 5 6 7 8 9 10 
1 2 3 4 5 6 7 8 9 10 
1 2 3 4 5 6 7 8 9 10 
1 2 3 4 5 6 7 8 9 10
"""

"""
for i in range (5,0,-1):
  for j in range(i,0,-1):
      print(j ,end="")
  else:
          print()
output
54321
4321
321
21
1
"""
'''
s=0
for i in range(5,0,-1):
  print(" "*s,end="")
  for j in range (i,0,-1):
      print(j,end="")
  else:
            print()
            s+=1
output
54321
 4321
  321
   21
    1
'''
'''
s=0
for i in range (6,0,-1):
  print(" "*s,end="")
  for j in range (i,0,-1):
      print(j,end="")
  else:
          print()
          s+=1
output:
654321
 54321
  4321
   321
    21
     1
     '''
'''
s=5
for i in range(1,10,2):
  print(" "*s,end="")
  print("*"*i)
  s=s-1

output:
     *
    ***
   *****
  *******
 *********
'''

'''
for i in range (1,6):
  for j in range(i,i+1):
      print(j,end="")
  print()
output:
1
2
3
4
5'''

'''

for i in range (1,6):
  for j in range (1,i+1):
      print(j,end=" ")
  print()

output:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
"""
s=0
for i in range (1,6):
  print(" "*s,end="")
  for j in range (i,6):
      print(j,end="")
  else:
          print()
          s+=1

output:
12345
 2345
  345
   45
    5"""
"""
for i in range (65,90,2):
    for j in range(i,+i+1):
        print(chr(j),end=" ")
    print(end=" ")

print()
output:
A  C  E  G  I  K  M  O  Q  S  U  W  Y  
"""
"""
for i in range (97,123,2):
    for j in range(i,+i+1):
        print(chr(j),end=" ")
    print(end="  ")

output:
a   c   e   g   i   k   m   o   q   s   u   w   y   """





