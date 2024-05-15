def Levenshtein(seq1,seq2):
    Matrix=[[0]*(len(seq2)+2) for _ in range(len(seq1) + 2)]
    Matrix[0][0]='*'
    Matrix[1][0]='|'
    Matrix[0][1]='__'
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
     
def combination(Seqs):
  Matrix=Levenshtein(Seqs[0],Seqs[1])
  Min_Score=Matrix[len(Matrix)-1][len(Matrix[0])-1]
  IndexI=0
  IndexJ=1
  for i in range(len(Seqs)-1):
   j=i+1
   while(j<len(Seqs)):
     Matrix=Levenshtein(Seqs[i],Seqs[j])
     if(Min_Score > Matrix[len(Matrix)-1][len(Matrix[0])-1] ):
      Min_Score=Matrix[len(Matrix)-1][len(Matrix[0])-1]
      IndexI=i
      IndexJ=j
     j+=1
   return Min_Score , Seqs[IndexI] , Seqs[IndexJ], 
   
def Path(Matrix):
  P=[]
  i=len(Matrix)-1 
  j=len(Matrix[0])-1
  P.append({'i':i,'j':j,'value':Matrix[i][j]}) 
  while i >1 and j>1 : 
      Min_Score=min(Matrix[i-1][j-1],Matrix[i-1][j],Matrix[i][j-1])
      if(Matrix[i-1][j-1]==Min_Score):
       P.append({'i':i-1,'j':j-1,'value':Matrix[i-1][j-1]})
       j=j-1
       i=i-1
      else : 
       if(Matrix[i-1][j] == Min_Score ):
        P.append({'i':i-1,'j':j,'value':Matrix[i-1][j]})
        i=i-1
       else :
        P.append({'i':i,'j':j-1,'value':Matrix[i][j-1]})
        j=j-1
  if {'i':1,'j':1,'value':0} not in P :
   P.append({'i':1,'j':1,'value':0})      
  return P
  
def CreatNewSeqs(P,Matrix):
 Index=len(P)-1
 NewSeq1=''
 IndexSeq1=2
 NewSeq2=''
 IndexSeq2=2
 while Index>0 :
  print(f"Index ! {Index}",end='')
  if(P[Index]['j'] < P[Index-1]['j'] and P[Index]['i'] < P[Index-1]['i']  ) :
    print(f"\t  IndexSeq1 : {IndexSeq1} \t IndexSeq2 : {IndexSeq2} ")
    NewSeq1+=Matrix[0][IndexSeq1]
    NewSeq2+=Matrix[IndexSeq2][0]
    IndexSeq1+=1
    IndexSeq2+=1
  else : 
    if P[Index]['j'] < P[Index-1]['j'] :
      NewSeq1+=Matrix[0][IndexSeq1]
      NewSeq2+='_'
      IndexSeq1+=1
      print(f"\t IndexSeq1 : {IndexSeq2} ")

    else :
      NewSeq2+=Matrix[IndexSeq2][0]
      NewSeq1+='_'
      IndexSeq2+=1
      print(f"\t IndexSeq2 : {IndexSeq2} ")

  Index-=1
 return NewSeq1 , NewSeq2


Min_Score , Seq1 , Seq2 =combination(["TAT","GAOTO","TAITI","AA"])
print(Min_Score , Seq1 , Seq2)
Matrix=Levenshtein(Seq1,Seq2)
ShowMatrix(Matrix)
P=Path(Matrix)
print(P)
SEQ,SEQ2=CreatNewSeqs(P,Matrix)
print(f"{SEQ} \n{SEQ2}")
