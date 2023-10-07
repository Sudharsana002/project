def pattern(str,len):
    for i in range(len):
        for j in range(len):
            if((i==0) or (i==len-1) or (i+j==len-1)):
                print(str[j],end=" ")
            else:
                print(" ",end=" ")
        print()
str=input()
len=len(str)
pattern(str,len)
