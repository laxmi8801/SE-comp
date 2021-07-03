inputFile = open(input("Enter File Name : "), "r")
M, T2, T3, T4 = [int(x) for x in inputFile.readline().split()]
print(M, T2, T3, T4)
def team_select():
    if(M < (T2*2)):
        N = M - 3
    elif (N > (T2 * 2)):
        N = M - 3
    else:
        N = M
pizzas = list()
for i in range(M):
    details = inputFile.readline()[:-1].split(" ")
    pizzas.append(Pizza(i, details[1:]))
for pizza in pizzas:
    print(pizza.ID, pizza.Ingredients)








f = open("demofile.txt", "r")
lst = []
for line in f:
    lst.append(f.read(0))
lst.sort(reverse = True)  
def ingredients():
    #arr consisting of different ingredients for every grp
    #diff_ing = []
    #return diff_ing

def tot_score():
    score = sum(map(lambda i : i * i, diff_ing))
    return score 
