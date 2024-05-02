import copy
MatrixBLOSUM62 = {
    "A": {
        "A": 4, "R": -1, "N": -2, "D": -2, "C": 0, "Q": -1, "E": -1, "G": 0, "H": -2, "I": -1, "L": -1, "K": -1, "M": -1, "F": -2, "P": -1, "S": 1, "T": 0, "W": -3, "Y": -2, "V": 0
    },
    "R": {
        "A": -1, "R": 5, "N": 0, "D": -2, "C": -3, "Q": 1, "E": 0, "G": -2, "H": 0, "I": -3, "L": -2, "K": 2, "M": -1, "F": -3, "P": -2, "S": -1, "T": -1, "W": -3, "Y": -2, "V": -3
    },
    "N": {
        "A": -2, "R": 0, "N": 6, "D": 1, "C": -3, "Q": 0, "E": 0, "G": 0, "H": 1, "I": -3, "L": -3, "K": 0, "M": -2, "F": -3, "P": -2, "S": 1, "T": 0, "W": -4, "Y": -2, "V": -3
    },
    "D": {
        "A": -2, "R": -2, "N": 1, "D": 6, "C": -3, "Q": 0, "E": 2, "G": -1, "H": -1, "I": -3, "L": -4, "K": -1, "M": -3, "F": -3, "P": -1, "S": 0, "T": -1, "W": -4, "Y": -3, "V": -3
    },
    "C": {
        "A": 0, "R": -3, "N": -3, "D": -3, "C": 9, "Q": -3, "E": -4, "G": -3, "H": -3, "I": -1, "L": -1, "K": -3, "M": -1, "F": -2, "P": -3, "S": -1, "T": -1, "W": -2, "Y": -2, "V": -1
    },
    "Q": {
        "A": -1, "R": 1, "N": 0, "D": 0, "C": -3, "Q": 5, "E": 2, "G": -2, "H": 0, "I": -3, "L": -2, "K": 1, "M": 0, "F": -3, "P": -1, "S": 0, "T": -1, "W": -2, "Y": -1, "V": -2
    },
    "E": {
        "A": -1, "R": 0, "N": 0, "D": 2, "C": -4, "Q": 2, "E": 5, "G": -2, "H": 0, "I": -3, "L": -3, "K": 1, "M": -2, "F": -3, "P": -1, "S": 0, "T": -1, "W": -3, "Y": -2, "V": -2
    },
    "G": {
        "A": 0, "R": -2, "N": 0, "D": -1, "C": -3, "Q": -2, "E": -2, "G": 6, "H": -2, "I": -4, "L": -4, "K": -2, "M": -3, "F": -3, "P": -2, "S": 0, "T": -2, "W": -2, "Y": -3, "V": -3
    },
    "H": {
        "A": -2, "R": 0, "N": 1, "D": -1, "C": -3, "Q": 0, "E": 0, "G": -2, "H": 8, "I": -3, "L": -3, "K": -1, "M": -2, "F": -1, "P": -2, "S": -1, "T": -2, "W": -2, "Y": 2, "V": -3
    },
    "I": {
        "A": -1, "R": -3, "N": -3, "D": -3, "C": -1, "Q": -3, "E": -3, "G": -4, "H": -3, "I": 4, "L": 2, "K": -3, "M": 1, "F": 0, "P": -3, "S": -2, "T": -1, "W": -3, "Y": -1, "V": 3
    },
    "L": {
        "A": -1, "R": -2, "N": -3, "D": -4, "C": -1, "Q": -2, "E": -3, "G": -4, "H": -3, "I": 2, "L": 4, "K": -2, "M": 2, "F": 0, "P": -3, "S": -2, "T": -1, "W": -2, "Y": -1, "V": 1
    },
    "K": {
        "A": -1, "R": 2, "N": 0, "D": -1, "C": -3, "Q": 1, "E": 1, "G": -2, "H": -1, "I": -3, "L": -2, "K": 5, "M": -1, "F": -3, "P": -1, "S": 0, "T": -1, "W": -3, "Y": -2, "V": -2   
        },
    "M": {
        "A": -1, "R": -1, "N": -2, "D": -3, "C": -1, "Q": 0, "E": -2, "G": -3, "H": -2, "I": 1, "L": 2, "K": -1, "M": 5, "F": 0, "P": -2, "S": -1, "T": -1, "W": -1, "Y": -1, "V": 1
    },
    "F": {
        "A": -2, "R": -3, "N": -3, "D": -3, "C": -2, "Q": -3, "E": -3, "G": -3, "H": -1, "I": 0, "L": 0, "K": -3, "M": 0, "F": 6, "P": -4, "S": -2, "T": -2, "W": 1, "Y": 3, "V": -1
    },
    "P": {
        "A": -1, "R": -2, "N": -2, "D": -1, "C": -3, "Q": -1, "E": -1, "G": -2, "H": -2, "I": -3, "L": -3, "K": -1, "M": -2, "F": -4, "P": 7, "S": -1, "T": -1, "W": -4, "Y": -3, "V": -2
    },
    "S": {
        "A": 1, "R": -1, "N": 1, "D": 0, "C": -1, "Q": 0, "E": 0, "G": 0, "H": -1, "I": -2, "L": -2, "K": 0, "M": -1, "F": -2, "P": -1, "S": 4, "T": 1, "W": -3, "Y": -2, "V": -2  },
    "T": {
        "A": 0, "R": -1, "N": 0, "D": -1, "C": -1, "Q": -1, "E": -1, "G": -2, "H": -2, "I": -1, "L": -1, "K": -1, "M": -1, "F": -2, "P": -1, "S": 1, "T": 5, "W": -2, "Y": -2, "V": 0    },
    "W": {
        "A": -3, "R": -3, "N": -4, "D": -4, "C": -2, "Q": -2, "E": -3, "G": -2, "H": -2, "I": -3, "L": -2, "K": -3, "M": -1, "F": 1, "P": -4, "S": -3, "T": -2, "W": 11, "Y": 2, "V": -3
    },
    "Y": {
        "A": -2, "R": -2, "N": -2, "D": -3, "C": -2, "Q": -1, "E": -2, "G": -3, "H": 2, "I": -1, "L": -1, "K": -2, "M": -1, "F": 3, "P": -3, "S": -2, "T": -2, "W": 2, "Y": 7, "V": -1
    },
    "V": {
        "A": 0, "R": -3, "N": -3, "D": -3, "C": -1, "Q": -2, "E": -2, "G": -3, "H": -3, "I": 3, "L": 1, "K": -2, "M": 1, "F": -1, "P": -2, "S": -2, "T": 0, "W": -3, "Y": -1, "V": 4
    }
}
Indel=-2

def NewAligments(seq1,seq2,path):
  Newseq1=''
  Newseq2=''
  indexSeq1=0
  indexSeq2=0
  pIndex=len(path)-1
  while pIndex > 0:
#    i+1 , j+1 , j+1,i+1
   if(path[pIndex]["i"] < path[pIndex-1]["i"] and path[pIndex]["j"] < path[pIndex-1]["j"] ):
     Newseq1+=seq1[indexSeq1]
     Newseq2+=seq2[indexSeq2]
     indexSeq1+=1
     indexSeq2+=1
   elif(path[pIndex]["i"] < path[pIndex-1]["i"]):
      Newseq1+=seq1[indexSeq1]
      Newseq2+='-'
      indexSeq1+=1
   elif(path[pIndex]["j"] < path[pIndex-1]["j"]):
      Newseq2+=seq2[indexSeq2]
      Newseq1+='-'
      indexSeq2+=1  
   pIndex-=1
  return Newseq1,Newseq2
def Path_Exist(i,j,filepath,move):
  if(not filepath):
    return False
  for Crossed in filepath: 
    if(Crossed['indexs']["i"]==i and Crossed['indexs']["j"]==j and Crossed["move"]==move ):
      return True
  return False    

def OptimalPath(paths):
  if(len(paths)==1):
    return paths[0]
  else: 
    scores=[]
    for path in paths:
     sum=0
     for move in path:
       sum+=move['value']
     scores.append(sum)  
     max_score= max(scores) 
     max_index = scores.index(max_score)
    return paths[max_index]
def GeneratePaths(Matrix):
 path=[]
 paths=[]
 filepath=[]
 m=len(Matrix)
 n=len(Matrix[0]) 
 path.append({'i':n-1,'j':m-1,'value':Matrix[m-1][n-1]})
 i=n-1
 j=m-1
 path,filepath=GenerateChemin(Matrix,path,filepath,i,j)
 paths.append(path)
 fileIndex=0
 while(fileIndex < len(filepath) ):
   i=filepath[fileIndex]['indexs']['i']
   j=filepath[fileIndex]['indexs']['j']
   path,filepath=GenerateChemin(Matrix,path=filepath[fileIndex]['path'],filepath=filepath,i=i,j=j)
   paths.append(path)
   fileIndex+=1

#  print(filepath)
 return paths


def GenerateChemin(Matrix,path,filepath,i,j):

 while i>1 and j>1 :
    if(Matrix[j][0]==Matrix[0][i]):
      path.append({'i':i-1,'j':j-1,'value':Matrix[j-1][i-1]})
      j=j-1
      i=i-1
    else : 
      Max=max(Matrix[j-1][i],Matrix[j-1][i-1],Matrix[j][i-1])
      if(Matrix[j-1][i] == Max and not Path_Exist(i,j,filepath,"UP") ):
       if(Matrix[j][i-1] == Max or Matrix[j-1][i-1] == Max):  # en cas il ya un ou plusieur autre chemin ( le cas ou les 3 ont la meme valeur )
         filepath.append({'path':copy.deepcopy(path),'move':"UP",'indexs':{'i':i,'j':j}})

       path.append({'i':i,'j':j-1,'value':Matrix[j-1][i]})
       j=j-1

      elif(Matrix[j][i-1] == Max and not Path_Exist(i,j,filepath,"RIGHT")) :
        if(Matrix[j-1][i-1] == Max): # en cas il ya un ou plusieur autre chemin ( le cas ou les 3 ont la meme valeur )
         filepath.append({'path':copy.deepcopy(path),'move':"RIGHT",'indexs':{'i':i,'j':j}})
        path.append({'i':i-1,'j':j,'value':Matrix[j][i-1]})
        i=i-1
     
      elif(Matrix[j-1][i-1] == Max) :   
        path.append({'i':i-1,'j':j-1,'value':Matrix[j-1][i-1]})
        j=j-1
        i=i-1
 if(path[len(path)-1]!={'i': 1, 'j': 1, 'value': 0})   :    
  path.append({'i':1,'j':1,'value':Matrix[1][1]})
 return path,filepath


def Affichage(Matrix):
 for i in range(len(Matrix)):
  print("\n")
  for j in range(len(Matrix[0])):
    print(f" {Matrix[i][j]} \t " , end='')
 print("\n")   


def FillMatrix(Matrix):
 for i in range(2,len(Matrix)):
  for j in range(2,len(Matrix[0])):
     Matrix[i][j]=max(Matrix[i-1][j-1]+MatrixBLOSUM62[Matrix[i][0]][Matrix[0][j]],Matrix[i][j-1]+Indel,Matrix[i-1][j]+Indel)
 return Matrix

def initiatMatrix(seq1,seq2):
  Matrix=[[0]*(len(seq1)+2) for _ in range(len(seq2) + 2)]
  Matrix[0][0]='/'
  Matrix[0][1]='i'
  Matrix[1][0]='j'
  Matrix[1][1]=0
  j=2
  for i in seq1:
    Matrix[0][j]=i
    j=j+1
  j=2
  for i in seq2:
    Matrix[j][0]=i
    j=j+1  

  for i in range(2,len(Matrix[0])):
   Matrix[1][i]=Matrix[1][i-1] + Indel 
  for j in range(2,len(Matrix)):
    Matrix[j][1]=Matrix[j-1][1] + Indel 
  return Matrix

seq1="ACGT" ; seq2="ACGTA"
Matrix=initiatMatrix(seq1,seq2)
Matrix=FillMatrix(Matrix)
# Matrix[6][4]=24
# Matrix[5][4]=24
Affichage(Matrix)
paths=GeneratePaths(Matrix)
for path in paths:
 print(f"paths : {path} ")
Bestpath=OptimalPath(paths) 
print(f"Bestpath : {Bestpath}")
seq1,seq2=NewAligments(seq1,seq2,Bestpath)
print(seq1)
print(seq2)

