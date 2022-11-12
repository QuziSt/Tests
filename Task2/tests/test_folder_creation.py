import pytest
from Task2.main import create_folder, authorization, delete_folder


def test_create_folder():
    assert create_folder(authorization()).status_code == 201
    delete_folder()

