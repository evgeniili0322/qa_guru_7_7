import pytest
import os


@pytest.fixture(scope='function')
def remove_csv():
    yield

    os.remove(os.path.join(os.path.abspath('resources'), 'new_csv.csv'))


@pytest.fixture(scope='function')
def remove_img():
    yield

    os.remove(os.path.abspath('0Im1.png'))


@pytest.fixture(scope='function')
def remove_extracted_files():
    yield

    os.remove(os.path.join(os.path.dirname(__file__), 'file_example_XLS_10.xls'))
    os.remove(os.path.join(os.path.dirname(__file__), 'file_example_XLSX_50.xlsx'))
    os.remove(os.path.join(os.path.dirname(__file__), 'docs-pytest-org-en-latest.pdf'))
    os.remove(os.path.join(os.path.dirname(__file__), 'zip_text_test'))
