import pytest
import os


@pytest.fixture(scope='function')
def remove_csv():
    yield

    os.remove(os.path.join(os.path.abspath('tests/resources'), 'new_csv.csv'))


@pytest.fixture(scope='function')
def remove_img():
    yield

    os.remove(os.path.abspath('0Im1.png'))
