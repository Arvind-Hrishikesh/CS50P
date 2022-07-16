def main():
    groceries={}
    while 1>0:
        try:
            x=input()
        except EOFError:
            for i in sorted(groceries.keys()):
                print(f"{groceries[i]} {i.upper()}")
            break
        else:
            if x in groceries:
                groceries[x]+=1
            else:
                groceries[x]=1

if __name__=="__main__":
    main()



