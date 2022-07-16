import sys
import csv

def main():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    filename = sys.argv[1]
    if filename[filename.rfind("."):]!=".csv":
        sys.exit("Not a CSV file")

    convert_before_to_after(filename)

def convert_before_to_after(filename):
    table[]
    headers = {"first", "last", "house"}
    with open(sys.argv[2], 'w') as write_file:
        dw = csv.writer(write_file)
        dw.writerow(headers)
        try:
            with open(filename, 'r') as file:
                table_object=csv.reader(file)
                for row in table_object:
                table.append(row)

                dw.writerows(table)

        except FileNotFoundError:
            sys.exit(f"Could not read {filename}")

if __name__=="__main__":
    main()