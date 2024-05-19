import numpy as np
import random
import math
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
def Show_LevMatrix(Matrix):
   for i in range(len(Matrix)): 
     for j in range(len(Matrix[0])) :
      print(f" {Matrix[i][j]} \t " , end='')
     print('\n')

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
  
def NewSeqs(Matrix):
 Paths = Path(Matrix)
 Index=len(Paths)-1
 NewSeq1=''
 IndexSeq1=2
 NewSeq2=''
 IndexSeq2=2
 while Index>0 :
  if(Paths[Index]['j'] < Paths[Index-1]['j'] and Paths[Index]['i'] < Paths[Index-1]['i']  ) :
    NewSeq1+=Matrix[0][IndexSeq1]
    NewSeq2+=Matrix[IndexSeq2][0]
    IndexSeq1+=1
    IndexSeq2+=1
  else : 
    if Paths[Index]['j'] < Paths[Index-1]['j'] :
      NewSeq1+=Matrix[0][IndexSeq1]
      NewSeq2+='-'
      IndexSeq1+=1

    else :
      NewSeq2+=Matrix[IndexSeq2][0]
      NewSeq1+='-'
      IndexSeq2+=1

  Index-=1
 return NewSeq1 , NewSeq2

def print_sequence(sequence):
        for seq in sequence:
            print(seq)

def add_gaps(lines):

        for i in range(len(lines)):
            diff = calc_m(lines) - len(lines[i])
            for j in range(diff):
                lines[i] += "-"

        return lines
def calc_m(lines):
        m_aux = 0
        lengths = []

        for line in lines:
            length = len(line)
            lengths.append(length)

            if length >= m_aux:
                m_aux = length

        return m_aux

def get_interval_gaps(lines, cell_i, cell_j):
        aux_cell_j = cell_j
        gaps = []
        symbol_found = False

        # Find gaps after cell_j (inclusive)
        while not symbol_found:
            if cell_j > len(lines[cell_i]) - 1:
                break
            elif lines[cell_i][cell_j] == "-":
                gaps.append(cell_j)
                cell_j += 1
            else:
                symbol_found = True

        # Find gaps before cell_j (exclusive)
        aux_cell_j -= 1
        while not symbol_found:
            if aux_cell_j < 0:
                break
            elif lines[cell_i][aux_cell_j] == "-":
                gaps.insert(0, aux_cell_j)
                aux_cell_j -= 1
            else:
                symbol_found = True

        return gaps
def remove_useless_gaps(lines):
        to_rm = []
        only_gaps = True
        m =  calc_m(lines)

        # Find columns with gaps only
        for i in range(m):
            for j in range(len(lines)):
                if (lines[j][i] != " ") and (lines[j][i] != "-"):
                    only_gaps = False

            if only_gaps:
                to_rm.append(i)
            else:
                only_gaps = True

        # Remove gap-only columns
        to_rm.reverse()
        for i in range(len(lines)):
            line = []
            for j in range(m):
                line.append(lines[i][j])

            for j in to_rm:
                line.pop(j)

            lines[i] = ''.join(line)

        # Return the new matrix
        return lines

class GA:

    def __init__(self, sequencesLength, generations, min_generations, mutation_rate):
        self.sequencesLength = sequencesLength
        self.generations = generations
        self.min_generations = min_generations
        self.mutation_rate = mutation_rate
        
    @staticmethod
    def evaluation_func(lines):
        for i in range(len(lines)):
            sum_score = 0
            for j in range(len(lines)):
                if i != j:
                    Matrix = Levenshtein(lines[i], lines[j])
                    scr= Matrix[len(Matrix)-1][len(Matrix[0])-1]
                    sum_score += scr

            return sum_score * - 1

    def no_change(self, best):
        if len(best) < self.min_generations:
            return False
        else:
            percent = int(0.2 * len(best))
            last = best[-percent:]

            if np.var(last) < 1.05:
                return True

        return False

    def init_pop(self, lines_list):
        pop = []
        for c in range(self.sequencesLength):

            lines_list_aux = []
            for i in range(len(lines_list)):
                alignments = []

                for j in range(len(lines_list)):
                    if i != j:
                        matrix = Levenshtein(lines_list[i], lines_list[j])
                        curr_alignment = NewSeqs(matrix)
                        alignments.append(curr_alignment)

                alignment = random.choice(alignments)
                alignment = alignment[0]
                lines_list_aux.append(alignment)

            lines_list_aux =  add_gaps(lines_list_aux)
            pop.append({"sequence": lines_list_aux, "evaluation": 0})
            print("\sequence " + str(c + 1) + ":")
            print_sequence(lines_list_aux)
        return pop

    @staticmethod
    def select_parents(pop, evaluations):
        pop_sum = sum(evaluations)
        evaluations_aux = []
        for ev in evaluations:
            evaluations_aux.append(ev / pop_sum)

        pool = []
        for i in range(len(pop)):
            prob = math.ceil(evaluations_aux[i] * 100)

            for j in range(prob):
                pool.append(pop[i])
        p1 = random.choice(pool)
        p2 = random.choice(pool)
        return [p1, p2]
    @staticmethod
    def apply_crossover(pop, p1, p2):

        n = len(pop[0]["sequence"])
        rand_h = random.randint(1, n - 1)
        child = p1["sequence"][:rand_h] + p2["sequence"][rand_h:]
        return {"sequence": child, "evaluation": 0}
    def apply_mutation(self, pop, child):

        n = len(pop[0])

        if round(random.uniform(0, 1), 2) < self.mutation_rate:
            rand = round(random.uniform(0, 1), 2)

            if rand < 0.5:
                cell_i = random.randint(1, n - 1)
                cell_j = random.randint(1, len(child[cell_i]) - 1)

                while child[cell_i][cell_j] != "-":
                    cell_i = random.randint(0, n - 1)
                    cell_j = random.randint(0, len(child[cell_i]) - 1)

                gaps =   get_interval_gaps(child, cell_i, cell_j)
                start, end = gaps[0], gaps[len(gaps) - 1]

                child[cell_i] = child[cell_i][:start] + child[cell_i][end + 1:]
            else:
                cell_i = random.randint(1, n - 1)
                cell_j = random.randint(1, len(child[cell_i]) - 1)
                k = random.randint(1, math.ceil(0.1 * calc_m(child)))
                to_add = ""

                for i in range(k):
                    to_add += "-"

                child[cell_i] = child[cell_i][:cell_j] + to_add + child[cell_i][cell_j:]
        return child

    def run_ga(self, lines_list):

        print("Input matrix:")
        print_sequence(lines_list)
        pop = self.init_pop(lines_list)
        best_val = None
        best_chromosome = None
        best_sequences = []
        count = 0
        new_pop = []
        print()

        while count < self.generations:
            evaluations = []
            for i in range(len(pop)):
                pop[i]["evaluation"] = self.evaluation_func(pop[i]["sequence"])
                evaluations.append(pop[i]["evaluation"])
            for w in range(self.sequencesLength):

                p1, p2 = self.select_parents(pop, evaluations)
                rand = round(random.uniform(0, 1), 2)
                if rand < 0.5:
                    child = self.apply_crossover(pop, p1, p2)
                    child["sequence"] = self.apply_mutation(pop, child["sequence"])
                    child["sequence"] =   add_gaps(child["sequence"])
                    child["sequence"] =   remove_useless_gaps(child["sequence"])
                    new_pop.append(child)

            if(len(new_pop)> 0):
                best_val = self.evaluation_func(new_pop[0]["sequence"])
                new_pop[0]["evaluation"] = best_val
                best_chromosome = new_pop[0]["sequence"]
            for i in range(len(new_pop)):
                curr_val = self.evaluation_func(new_pop[i]["sequence"])
                new_pop[i]["evaluation"] = curr_val

                if curr_val >= best_val:
                    best_val = curr_val
                    best_chromosome = new_pop[i]["sequence"]

            print("Generation " + str(count + 1) + ": " + str(best_val))

            best_sequences.append(best_val)

            if self.no_change(best_sequences):
                print("\nAbort: no variation!", end="")
                break
            pop = sorted(pop, key=lambda k: k["evaluation"], reverse=True)
            new_pop = sorted(new_pop, key=lambda k: k["evaluation"], reverse=True)

            for i in range(len(new_pop)):
                pop.pop()
                pop.insert(0, new_pop[i])

            new_pop = []
            count = count + 1

        # Best solution
        print("\nBest solution:")
        print_sequence(best_chromosome)
        print_sequence(str(best_val))
        return best_val


data = [
    "CTATCGAGTCTTCCCTCCCTCCTTCTCTGCCCCCTCCGCTCCCGCTGGAG",
"CCCTCCACCCTACAAGTGGCCTACAGGGCACAGGTGAGGCGGGACTGGAC",
"AGCTCCTGCTTTGATCGCCGGAGATCTGCAAATTCTGCCCATGTCGGGGC",
"TGCAGAGCACTCCGACGTGTCCCATAGTGTTTCCAAACTTGGAAAGGGCG",
"GGGGAGGGCGGGAGGATGCGGAGGGCGGAGGTATGCAGACAACGAGTCAG",
"AGTTTCCCCTTGAAAGCCTCAAAAGTGTCCACGTCCTCAAAAAGAATGGA",
"ACCAATTTAAGAAGCCAGCCCCGTGGCCACGTCCCTTCCCCCATTCGCTC",
"CCTCCTCTGCGCCCCCGCAGGCTCCTCCCAGCTGTGGCTGCCCGGGCCCC",
"CAGCCCCAGCCCTCCCATTGGTGGAGGCCCTTTTGGAGGCACCCTAGGGC",
"CAGGGAAACTTTTGCCGTATAAATAGGGCAGATCCGGGCTTTATTATTTT"
]
genetic_algorithm = GA(len(data),40, 60, 0.3)
genetic_algorithm.run_ga(data)