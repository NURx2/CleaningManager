import openpyxl

telegram_ids = {
    'ЯН': '1',
    'ЗАХАР': '2',
    'КИРИЛЛ': '3',
    'ДАНИИЛ': '4',
    'АЙНУР': '5',
}


def parse():
    table = openpyxl.load_workbook(filename='table.xlsx')
    main_sheet = table['Лист1']
    names = [value.value for value in main_sheet['A'][1:]]
    print(names)
