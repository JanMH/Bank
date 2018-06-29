import csv
from datetime import datetime


# format: "Auftragskonto";"Buchungstag";"Buchungstext";"Verwendungszweck";"Beguenstigter/Zahlungspflichtiger";"Betrag";"Waehrung"


def parse_german_date(to_parse):
    return datetime.strptime(to_parse, '%d.%m.%y').date()


def parse_full_german_date(to_parse):
    return datetime.strptime(to_parse, '%d.%m.%Y').date()


def parse_german_number(to_parse):
    to_parse = to_parse.replace('.', '')
    return float(to_parse.replace(',', '.'))


def __convert_sparkasse_row(row):
    result = "sparkasse " + row[0], parse_german_date(row[1]), \
             row[3], row[4], row[5], parse_german_number(row[8]), row[9]
    return result


def __convert_ing_diba_row(row):
    result = "ING DiBa", parse_full_german_date(row[0]), row[3], row[4], row[2], parse_german_number(row[5]), row[6]
    return result


def parse_sparkasse_file(file_name):
    with open(file_name, 'rt', encoding='latin_1') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
        next(spamreader)
        return list(map(__convert_sparkasse_row, spamreader))


def parse_ing_diba_file(file_name):
    with open(file_name, 'rt', encoding='latin_1') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for x in range(0, 7):
            next(spamreader)
        return list(map(__convert_ing_diba_row, spamreader))
