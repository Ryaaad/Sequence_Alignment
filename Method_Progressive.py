def Levenshtein(seq1,seq2):
    Matrix=[[0]*(len(seq2)+2) for _ in range(len(seq1) + 2)]
    for i in range(2,len(Matrix)):
     Matrix[i][0]=seq1[i-2]
    for i in range(2,len(Matrix[0])):
     Matrix[0][i]=seq2[i-2] 

    for i in range(2,len(Matrix)):
     Matrix[i][1]=Matrix[i-1][1]+1
    for i in range(2,len(Matrix[0])):
     Matrix[1][i]=Matrix[1][i-1]+1
    for i in range(2,len(Matrix)):
      for j in range(2,len(Matrix[0])):
        cout=0
        if(Matrix[i][0]==Matrix[0][j]): 
           cout=0
        else : 
          cout=1
        Matrix[i][j]=min(Matrix[i-1][j-1]+cout,Matrix[i][j-1]+1,Matrix[i-1][j]+1)
    return Matrix
def ShowMatrix(Matrix):
   for i in range(len(Matrix)): 
     for j in range(len(Matrix[0])) :
      print(f" {Matrix[i][j]} \t " , end='')
     print('\n')
     
Matrix=Levenshtein("NICHE","CHIENS")
ShowMatrix(Matrix)