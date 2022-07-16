import sys

def main():
    path = sys.argv[1]
    num_of_lines = line_counter(path)
    print(num_of_lines)

def line_counter(path):
    extension=path[path.rfind("."):]
    if extension != ".py":
        sys.exit("Not a Python file")
    try:
        file = open(path,"r")
    except FileNotFoundError:
        sys.exit("File does not exist")
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")

    lines_list = file.readlines()
    num_of_lines=0
    for j in lines_list:
        j=j.replace(" ","")
        if j[0]=="#":
            continue
        elif j=="\n":
            continue
        else:
            num_of_lines+=1
    return num_of_lines

if __name__ == "__main__":
    main()