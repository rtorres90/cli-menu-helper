from random import randint
import re
import unittest

from CliMenuHelper import CliMenuHelper


class TestCliMenuHelper(unittest.TestCase):
    def test_menu_title(self):
        test_title = 'test %s' % randint(10, 99)
        cmh = CliMenuHelper(title=test_title, options=['opt'])
        self.assertEqual(test_title, cmh.title)

    def test_title_equals_separators(self):
        test_title = 'test %s' % randint(100, 999)
        cmh = CliMenuHelper(title=test_title, options=['opt'])
        self.assertEqual(len(cmh.create_menu_title()), len(cmh.separator))

    def test_exit_line_equals_separator(self):
        test_title = 'test %s' % randint(100, 999)
        test_option = 'option %s' % randint(100, 999)
        cmh = CliMenuHelper(title=test_title, options=[test_option])
        self.assertEqual(len(cmh.exit_line), len(cmh.separator))

    def test_options_consistency(self):
        test_title = 'test %s' % randint(100, 999)
        test_options = ['option %s' % randint(100, 999) for _ in xrange(randint(5, 10))]
        cmh = CliMenuHelper(title=test_title, options=test_options)
        options = cmh.create_options_panel().splitlines()
        self.assertEqual(1, len(set([len(option) for option in options])))

    def test_menu_consistency(self):
        test_title = 'test %s' % randint(100, 999)
        test_options = ['option %s' % randint(100, 999) for _ in xrange(randint(5, 10))]
        cmh = CliMenuHelper(title=test_title, options=test_options)
        test_items = cmh.create_options_panel().splitlines()
        test_items.append(cmh.separator)
        test_items.append(cmh.create_menu_title())
        test_items.append(cmh.exit_line)
        self.assertEqual(1, len(set([len(item) for item in test_items])))
