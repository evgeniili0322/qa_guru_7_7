import csv
import os

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

NEW_CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'new_csv.csv')


def test_write_csv(remove_csv):
    with open(NEW_CSV_PATH, 'w') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=';')
        csvwriter.writerow(['Bonny', 'Born', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(NEW_CSV_PATH) as csv_file:
        csvreader = csv.reader(csv_file, delimiter=';')
        csv_text = [row for row in csvreader]

    assert csv_text == [['Bonny', 'Born', 'Peter'], ['Alex', 'Serj', 'Yana']]