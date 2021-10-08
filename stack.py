A=[]
while True:
    
    insert=input("If you want to add element press A or you want to delete element press D")
    if insert=='A' or insert=='a':  
        add=int(input("How many element you want to insert")) 
        for i in range(add):
            arr=int(input("enter element"))
            A.append(arr)
            print(A)
    elif insert=='D' or insert=='d':
        # print('if you want to delete the elemet please press y')
        # while len(A)>0:
        if len(A)==0:
            print("All element are deleted")
        else:
            A.pop()
            print(A)
        
    
            
    