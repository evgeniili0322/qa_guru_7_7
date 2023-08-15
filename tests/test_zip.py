import os
import zipfile

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

ZIP_PATH = os.path.join(os.path.abspath('resources'), 'zip_example.zip')


def test_zip(remove_extracted_files):
    with zipfile.ZipFile(ZIP_PATH) as zip_example:
        zip_example.extractall()
        zip_names = zip_example.namelist()
        zip_file_text = zip_example.read('zip_text_test')

    assert zip_file_text == b'test text'
    assert zip_names[0] == 'docs-pytest-org-en-latest.pdf'
    assert os.path.exists(os.path.join(os.path.dirname(__file__), 'file_example_XLS_10.xls'))
    assert os.path.exists(os.path.join(os.path.dirname(__file__), 'file_example_XLSX_50.xlsx'))
    assert os.path.exists(os.path.join(os.path.dirname(__file__), 'docs-pytest-org-en-latest.pdf'))
    assert os.path.exists(os.path.join(os.path.dirname(__file__), 'zip_text_test'))
