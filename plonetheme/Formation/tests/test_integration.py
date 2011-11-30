from plonetheme.Formation.tests.base import ThemeFormationTestCase as TestCase


class ThemeFormationTestCase(TestCase):

    def test_Formation_layers_available(self):
        self.failUnless('Formation_images' in self.portal.portal_skins)
        self.failUnless('Formation_styles' in self.portal.portal_skins)
        self.failUnless('Formation_templates' in self.portal.portal_skins)

    def test_Formation_skin_installed(self):
        self.skins = self.portal.portal_skins
        theme = self.skins.getDefaultSkin()
        self.failUnless(theme == 'Formation Theme', 'Default theme is %s' % theme)


def test_suite():
    from unittest import defaultTestLoader
    return defaultTestLoader.loadTestsFromName(__name__)
