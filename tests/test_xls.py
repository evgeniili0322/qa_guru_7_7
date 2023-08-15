import xlrd
import os

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

XLS_PATH = os.path.join(os.path.abspath('resources'), 'file_example_XLS_10.xls')


def test_open_xsl():
    book = xlrd.open_workbook(XLS_PATH)
    sheet = book.sheet_by_index(0)
    rows = []

    for rx in range(sheet.nrows):
        rows.append(sheet.row(rx))

    assert book.nsheets == 1
    assert book.sheet_names()[0] == 'Sheet1'
    assert sheet.ncols == 8
    assert sheet.nrows == 10
    assert sheet.cell_value(rowx=3, colx=2) == 'Gent'
    assert str(rows[-1]) == ("[number:9.0, text:'Vincenza', text:'Weiland', text:'Female', text:'United States', "
                             "number:40.0, text:'21/05/2015', number:6548.0]")
