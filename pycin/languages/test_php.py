from pycin.languages.PHP import PHP

php = PHP()


class TestPHP(object):
    def test_name(self):
        assert php.name == 'php'

    def test_pretty_name(self):
        assert php.pretty_name == 'PHP'

    def test_supportest_tools(self):
        assert len(php.get_supported_tools()) == 0
