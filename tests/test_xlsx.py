import os
from openpyxl import load_workbook

# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_open_xlsx():
    workbook = load_workbook('resources/file_example_XLSX_50.xlsx')
    sheet = workbook.active
    print(workbook.sheetnames)

    assert sheet.cell(row=3, column=2).value == 'Mara'
    assert sheet.max_row == 51
    assert sheet.max_column == 8
    assert workbook.sheetnames[0] == 'Sheet1'
