from math import factorial


#Choisir le type de Denombrement
def main():
    R = int(input("Avec Remise (1) ou Sans Remise (0)? : "))
    while R != 0 and R != 1:
        print("Veuillez entrer 0 ou 1 svp!")
        R = int(input("Avec Remise (1) ou Sans Remise (0)? : "))
    n = int(input("Entrer le nombre d'elements : "))
    p = int(input("Entrer le nombre d'elements a choisir : "))
    type = input("Arrangement (A), Combinaison (C) ou Permutation (P)? : ")
    if type == "A":
        print("A(",n,",",p,") = ", Arrangement(n, p, R))
    elif type == "C":
        print("C(",n,",",p,") = ", Combinaison(n, p, R))
    elif type == "P":
        print("P(",n,",",p,") = ", Permutation(n, p, R))


#Denombrement
def Arrangement(n, p, R):
    if R == 0:
        return n**p
    else:
        return factorial(n) / factorial(n - p)
    
def Combinaison(n, p, R):
    if R == 0:
        return factorial(n) / (factorial(p) * factorial(n - p))
    else:
        return factorial(n + p - 1) / (factorial(p) * factorial(n - 1))
    
def Permutation(n, p, R):
    if R == 0:
        return factorial(n)
    else:
        return factorial(n) / factorial(n - p)
    
#Execution 
main()