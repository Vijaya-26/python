nums=input("Enter 5 numbers: ")
L=nums.split(' ')
print("list : ",L)
S = L[0:3]
print("sliced list: ",S)
L[0]="0"
L[4]="0"
print("replaced_list: ",L)
L[0]=0
L[2]=0
R = L[0:3]
print("replaced_list_2: ",R)
