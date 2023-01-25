
row = int(input("Please Give an Intiger Row Number: "))
column = int(input("Please Give an Intiger Column Number: "))

for r in range(0,row):
    for col in range(0,column):
        if(((col == 0 or col== column-1) and r !=0) or ((r==0 or r== (row/2)) and (col>0 and col < column-1))):
            print("+ ",end="")
        else:
            print("  ",end="")
    print()