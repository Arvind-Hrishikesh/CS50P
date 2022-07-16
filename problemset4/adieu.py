def main():
    list_of_names=[]
    i=0
    while 1>0:
        try:
            x=input("Name: ")
        except EOFError:
            break
        else:
            list_of_names.insert(i,x)
            i+=1

    print("Adieu, adieu, to",end="")
    j=0

    if len(list_of_names)==1:
        print(f" {list_of_names[0]}")
    elif len(list_of_names)==2:
        print(f" {list_of_names[0]} and {list_of_names[1]}")
    else:
        for name in list_of_names:
            j+=1
            if j==i:
                print(f" and {name}")
            else:
                print(f" {name},",end="")



if __name__=="__main__":
    main()






