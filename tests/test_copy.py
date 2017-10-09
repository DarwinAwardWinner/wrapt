from __future__ import print_function

import unittest
import copy
import wrapt

class TestCopy(unittest.TestCase):

    def test_copy(self):
        orig = {'a': 1, 'b': {'x': 10, 'y': 11}}
        # Make a circular reference
        orig['c'] = orig
        wrapper = wrapt.ObjectProxy(orig)
        copied = copy.copy(orig)
        copied_wrapper = copy.copy(wrapper)
        # We can't compare the whole dicts because of the circular
        # reference
        self.assertEqual(wrapper['a'], copied_wrapper['a'])
        self.assertEqual(copied['a'], copied_wrapper['a'])
        self.assertIs(wrapper['b'], copied_wrapper['b'])

    def test_deepcopy(self):
        orig = {'a': 1, 'b': {'x': 10, 'y': 11}}
        # Make a circular reference
        orig['c'] = orig
        wrapper = wrapt.ObjectProxy(orig)
        deepcopied = copy.deepcopy(orig)
        deepcopied_wrapper = copy.deepcopy(wrapper)
        self.assertEqual(wrapper['a'], deepcopied_wrapper['a'])
        self.assertEqual(deepcopied['a'], deepcopied_wrapper['a'])
        self.assertIsNot(wrapper['b'], deepcopied_wrapper['b'])
        # Ensure deep-copied structure is still circular
        self.assertIs(deepcopied_wrapper.__wrapped__, deepcopied_wrapper['c'])
