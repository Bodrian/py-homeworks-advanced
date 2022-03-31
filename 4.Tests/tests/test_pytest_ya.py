import pytest
import src.yandex

class TestFunctionsPytest:
    def setup(self):
        print('setup')

    def teardown(self):
        print('teardown')

    def test_make_dir(self):
        dir_name = 'Boris'
        assert src.yandex.make_dir(dir_name) == (409 or 201)