import  csv

with open("\PYTHON - DE - 0 - 10000\Modulo 3 - File Handling\FIL0E.csv",newline='') as newCsvFile:
    spamReader = csv.reader(newCsvFile, delimeter = '',quotechar='|')
    for row in spamReader:
        print(", ".join(row))
