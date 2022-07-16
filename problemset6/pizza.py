from tabulate import tabulate
import sys
import csv

def main():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    filename = sys.argv[1]
    if filename[filename.rfind("."):]!=".csv":
        sys.exit("Not a CSV file")

    csv_to_table(filename)

def csv_to_table(filename):
    table=[]
    try:
        with open(filename,'r') as file:
            table_object=csv.reader(file)
            for row in table_object:
                table.append(row)

    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        print(tabulate(table, headers="firstrow",tablefmt="grid"))

if __name__=="__main__":
    main()