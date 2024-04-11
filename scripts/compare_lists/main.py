import csv


def read_column(csv_file):
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        #grabbing data from first column
        column_values = [row[0] for row in csv_reader]
    return column_values

list1 = read_column('./Data/list1.csv')
list2 = read_column('./Data/list2.csv')

difference = list(set(list1) - set(list2))


with open('./Data/difference.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    for item in difference:
        csv_writer.writerow([item])

print("Delta has been written to ./Data/difference.csv. Bing Bong")
