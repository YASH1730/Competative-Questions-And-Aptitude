import math

num = int(input("Enter the number :: "))

def triangle(num):

    spaces = num - 1

    for i in range(num):
        

        for j in range(0,spaces):
            print(end = ' ')

        spaces -= 1
        
        for j in range(0,i+1):
            print('* ',end = "")
        
        print("\r")

triangle(num)

# this one is working perfect for odd 

# mid = math.floor(num/2)+1

# even is not working good

# mid = math.floor(num/2)

# print(mid)
# for i in range(mid):
#     mid -= 1
#     for j in range(num-mid):
#         if(j >= mid):
#             print(f"[{i},{j}]",end = '\t')
#         else: 
#             print(f" ",end = '\t')
#     print('\n')

