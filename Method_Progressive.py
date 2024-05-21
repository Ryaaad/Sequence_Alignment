import copy

def Char_Equal(S1, S2):
  # Vérifie si S1 est une liste et S2 n'est pas une liste, ou vice versa (c'est le cas où on compare un profil avec une séquence normale). 
   # dans ce cas en vérifie si le caractère de la séquence à cet indice est inclus dans la liste des caractères du profil à cet indice.
    if isinstance(S1, list) and not isinstance(S2, list):
        for i in S1:
            if S2 == i:
                return True 
        return False
    if isinstance(S2, list) and not isinstance(S1, list):
        for i in S2:
            if S1 == i:
                return True
        return False

    # Si aucun des deux n'est une liste ( cas normal au en compare sequence avec sequence)
    return S1 == S2

# flatten & transform_structure sont des Fonction qui flat une list cad si on a une list : [a,b,[[c,d],e]] elle vas devenir [a,b,[c,d,e]]  
# c'est pas mon code c'est just pour fixe la sturtuce de la list pour avoir la structure desire
def flatten(nested_list): 
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list
def transform_structure(input_list):
    """Transforms the input list to the desired structure."""
    output_list = []
    for element in input_list:
        if isinstance(element, list) and isinstance(element[0], list):
            output_list.append(flatten(element))
        else:
            output_list.append(element)
    return output_list

def Levenshtein(seq1, seq2):
    # Fonction qui calcule la matrice Levenshtein
    Matrix = [[0] * (len(seq2) + 2) for _ in range(len(seq1) + 2)]
    Matrix[0][0] = '*'  
    Matrix[1][0] = '|'
    Matrix[0][1] = '__'

    # Initialisation de la 1ere colonne avec les caractères de seq1 et 1ere ligne avec les caractères de seq2
    for i in range(2, len(Matrix)):
        Matrix[i][0] = seq1[i-2]
    for i in range(2, len(Matrix[0])):
        Matrix[0][i] = seq2[i-2]

    # Initialisation des couts dans la première colonne et la première ligne
    for i in range(2, len(Matrix)):
        Matrix[i][1] = Matrix[i-1][1] + 1
    for i in range(2, len(Matrix[0])):
        Matrix[1][i] = Matrix[1][i-1] + 1

    for i in range(2, len(Matrix)):
        for j in range(2, len(Matrix[0])):
            cost = 0
            if Char_Equal(Matrix[i][0], Matrix[0][j]): # tester si les caractères sont egaux ou dans le cas ou en calcul avec profil en vois si l'autre caractères est inclu dans la list des caractères que la profil peut prendre a l'indice
                cost = 0
            else:
                cost = 1
            Matrix[i][j] = min(Matrix[i-1][j-1] + cost, Matrix[i][j-1] + 1, Matrix[i-1][j] + 1)

    return Matrix

def Show_LevMatrix(Matrix):
    # Fonction qui affiche la matrix Levenshtein
   for i in range(len(Matrix)): 
     for j in range(len(Matrix[0])) :
      print(f" {Matrix[i][j]} \t " , end='')
     print('\n')

def Best_Score(Seqs): 
  # Fonction Calcule la Combinison avec best score
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
  # la meme avec la fonction path celle de Needleman_Wunsch.py mais just elle prend min a chaque car en travail avec Levenshtein
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
  
def NewSeqs(Path,Matrix):
 Index=len(Path)-1
 NewSeq1=[]
 IndexSeq1=2
 NewSeq2=[]
 IndexSeq2=2
 while Index>0 :
  if(Path[Index]['j'] < Path[Index-1]['j'] and Path[Index]['i'] < Path[Index-1]['i']  ) :
    NewSeq1.append(Matrix[0][IndexSeq1])
    NewSeq2.append(Matrix[IndexSeq2][0])
    IndexSeq1+=1
    IndexSeq2+=1
  else : 
    if Path[Index]['j'] < Path[Index-1]['j'] :
      NewSeq1.append(Matrix[0][IndexSeq1])
      NewSeq2+='_'
      IndexSeq1+=1

    else :
      NewSeq2.append(Matrix[IndexSeq2][0])
      NewSeq1+='_'
      IndexSeq2+=1

  Index-=1
 return NewSeq1 , NewSeq2

def Creat_Profil(Seq1,Seq2):
  # Function qui creat profil
  profil=[[] for _ in range(len(Seq1))] 
  i=0
  while i<len(Seq1):
    if Char_Equal(Seq1[i],Seq2[i]):
         profil[i]=Seq1[i]
    else :
       profil[i].append(Seq1[i])
       profil[i].append(Seq2[i])
     
    i+=1
  # to flatten the array from ['T', 'A', 'T', ['_', 'A'], [[['O', '_'], 'I'], 'A']] to ['T', 'A', 'T', ['_', 'A'], ['O', '_', 'I', 'A']]
  profil=transform_structure(profil)
  return profil  

def Main(Seqs):
  SeqsCopy=copy.deepcopy(Seqs)
  while(len(Seqs)>1):
   Min_Score , Seq1 , Seq2 =Best_Score(Seqs)  
   Matrix=Levenshtein(Seq1,Seq2)
   P=Path(Matrix)
   SEQ,SEQ2=NewSeqs(P,Matrix)
   Profil=Creat_Profil(SEQ,SEQ2)
   Seqs.remove(Seq1)
   Seqs.remove(Seq2)
   Seqs.append(Profil)
  print(f"Fin : {Profil}")
  print(SeqsCopy)
  SeqsCopyCopy=copy.deepcopy(SeqsCopy)
  for i in SeqsCopy :
   Matrix=Levenshtein(Profil,i)
   P=Path(Matrix)
   SEQ,SEQ2=NewSeqs(P,Matrix)
   NewSeq = ''.join(SEQ) # convert list to string 
   SeqsCopyCopy.remove(i)
   SeqsCopyCopy.append(NewSeq)
  print(f"{SeqsCopyCopy} ")

Seqs=["TATI","TATO","TATOI","TATAA"]
Main(Seqs)
