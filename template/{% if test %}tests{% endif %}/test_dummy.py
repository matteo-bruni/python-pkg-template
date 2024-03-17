import os

import pytest


def capital_case(x):
    return x.capitalize()


def test_capital_case():
    assert capital_case("semaphore") == "Semaphore"


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(AttributeError):
        capital_case(9)


FIXTURE_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), "fixtures"))


@pytest.mark.parametrize(
    "file",
    ("a.txt", "b.txt"),
)
@pytest.mark.datafiles(FIXTURE_DIR)
def test_fixture_files(datafiles, file):
    file_path = os.path.join(datafiles, file)
    filename, ext = os.path.splitext(file)

    assert os.path.exists(file_path)

    with open(file_path) as f:
        assert f.read().strip() == filename.capitalize()
