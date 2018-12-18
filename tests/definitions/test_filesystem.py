from unittest import mock

from pycin.definitions.FileSystem import FileSystem


class TestFileSystem(object):
    @mock.patch('os.listdir')
    def test_get_directories(self, mocked_listdir):
        FileSystem.get_directories('.')
        mocked_listdir.assert_called_once_with('./')
