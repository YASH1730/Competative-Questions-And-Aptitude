# code for the hollow pyramid 

num = int(input("Enter the number :: "))

for i in range(num):
    
    for j in range(num):

        if((i - j) == i or (j - i) == j ):
            print(f"[{i},{j}]",end ="\t")

        elif (j == num-1 or i == num-1):
            print(f"[{i},{j}]",end ="\t")

        else :
            print(" ",end ="\t")

    print('\n')

