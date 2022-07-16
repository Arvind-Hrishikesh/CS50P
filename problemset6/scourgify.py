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
    table=[]
    headers = {"first" : None, "last" : None, "house" : None}
    with open(sys.argv[2], 'w') as write_file:
        dw = csv.DictWriter(write_file, delimiter=',', fieldnames=headers)
        dw.writeheader()
        try:
            with open(filename, 'r') as file:
                csv_file = csv.DictReader(file)
                for row in csv_file:
                    each_row=dict(row)
                    last_name,first_name=each_row["name"].split(", ")
                    house=each_row["house"]
                    dw.writerow({'first':first_name,'last':last_name,'house':house})

        except FileNotFoundError:
            sys.exit(f"Could not read {filename}")

if __name__=="__main__":
    main()