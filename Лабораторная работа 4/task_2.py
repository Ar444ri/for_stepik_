# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(delimiter=',', line_terminator='\n') -> None:
    with open(INPUT_FILENAME, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=delimiter)
        data = []
        for row in csvreader:
            data.append(row)
            with open(OUTPUT_FILENAME, 'w') as jsonfile:
                json.dump(data, jsonfile, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
