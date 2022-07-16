def main():
    x=input("Enter the name of the file\n").strip().lower()
    decision(x)

def decision(y):
    index=y.rfind(".") + 1 #only extension without the dot
    length=len(y)
    if y[index:(length+1)]=="gif":
        print("image/gif")
    elif y[index:(length+1)]=="jpg" or y[index:(length+1)]=="jpeg":
        print("image/jpeg")
    elif y[index:(length+1)]=="png":
        print("image/png")
    elif y[index:(length+1)]=="pdf":
        print("application/pdf")
    elif y[index:(length+1)]=="txt":
        print("text/plain")
    elif y[index:(length+1)]=="zip":
        print("application/zip")
    else:
        print("application/octet-stream")

main()