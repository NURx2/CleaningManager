import openpyxl

from src.database.additions import update_executors
from src.static.constants import cnt_weeks


def colored(cell):
    return True


def parse():
    table = openpyxl.load_workbook(filename='table.xlsx')
    main_sheet = table['Лист1']
    names = [value.value for value in main_sheet['A'][1:]]
    update_executors(names)

    n = len(names)
    start_row = 2
    start_col = ord('B')
    for i in range(start_col, start_col + cnt_weeks):
        for j in range(start_row, start_row + n):
            if colored(main_sheet[j][i]):
                date_of_the_duty = main_sheet[j][1]
