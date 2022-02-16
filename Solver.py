import numpy as np
import sys
sys.setrecursionlimit(10**6)
AA=[0]*9
global A
A=[AA]*9
A=np.reshape(A,(9,9))

A=np.reshape(A,(9,9))

def Display(A):                 #displays the sudoku
  for i in range(9):
    for j in range(9):
      if j==8:
        print(A[i][j])
      elif j%3==2:
        print(A[i][j]," | ",end=" ")
      else:
        print(A[i][j],end=" ")
    if i%3==2:
      print("-------|---------|--------")


def Clist(A,m,n,val):      #returns a list of elements the particular element affects
  b=[]
  a=[]
  for i in range(9):
    a=[m,i]
    b=[i,n]
    if i!=m:
      x,y=b
      if A[x][y]==val:
        return False
    if i!=n:
      x,y=a
      if A[x][y]==val:
        return False
  g=m//3
  f=n//3
  g=g*3
  f=f*3
  for i in range(3):
    for j in range(3):
      if g+i==m or f+j==n:
        continue 
      else:
        a=[i+g,f+j]
        x,y=a
        if A[x][y]==val:
          return False 
  return True

def Inference(m,n,val):
  l=Clist(m,n)
  for i in l:
    g,h=i
    if A[g][h]==val:
      return 0
  return 1

def Find(A):
  for i in range(9):
    for j in range(9):
      if A[i][j]==0:
        return i,j 
  return False

def Backtrack(A):
  f=Find(A)
  if not f:
    Display(A)
    return True 
  else:
    row,col=f
  for val in range(1,10):
    if Clist(A,row,col,val):
      A[row][col]=val
      if Backtrack(A):
        return True
      A[row][col]=0
  return False 
