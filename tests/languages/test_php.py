from pycin.languages.PHP import PHP

php = PHP()


class TestPHP(object):
    def test_name(self):
        """
        Tests the name attribute of the PHP class
        """
        assert php.name == 'php'

    def test_pretty_name(self):
        """
        Tests the pretty_name attribute of the PHP class
        """
        assert php.pretty_name == 'PHP'

    def test_supportest_tools(self):
        """
        Tests the get_supported_tools method of the PHP class
        """
        assert len(php.get_supported_tools()) == 0

    def test_str(self):
        """
        Tests the string representation of the PHP class
        """
        assert str(php) == 'PHP: []'
