import pypdf
import os

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

PDF_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'docs-pytest-org-en-latest.pdf')


def test_read_pdf(remove_img):
    reader = pypdf.PdfReader(PDF_PATH)
    number_of_pages = len(reader.pages)
    first_page = reader.pages[0]
    text = first_page.extract_text()
    count = 0
    for image_file in first_page.images:
        with open(str(count) + image_file.name, 'wb') as fp:
            fp.write(image_file.data)
            count += 1

    assert number_of_pages == 412
    assert text == ('pytest Documentation\nRelease 0.1\nholger krekel, trainer and consultant, '
                    'https://merlinux.eu/\nJul 14, 2022')
    assert os.path.exists(os.path.abspath('0Im1.png'))
