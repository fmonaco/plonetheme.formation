import unittest
import doctest

from Testing import ZopeTestCase

from plonetheme.Formation.tests.base import layer, FunctionalTestCase

optionflags = (doctest.NORMALIZE_WHITESPACE|
               doctest.ELLIPSIS|
               doctest.REPORT_NDIFF)

def test_suite():
    suite = ZopeTestCase.FunctionalDocFileSuite(
        'README.txt', package='plonetheme.Formation',
        optionflags=optionflags,
        test_class=FunctionalTestCase)
    suite.layer = layer
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
