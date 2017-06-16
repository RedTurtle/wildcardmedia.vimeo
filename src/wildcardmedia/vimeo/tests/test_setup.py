# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from wildcardmedia.vimeo.testing import WILDCARDMEDIA_VIMEO_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that wildcardmedia.vimeo is properly installed."""

    layer = WILDCARDMEDIA_VIMEO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if wildcardmedia.vimeo is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'wildcardmedia.vimeo'))

    def test_browserlayer(self):
        """Test that IWildcardmediaVimeoLayer is registered."""
        from wildcardmedia.vimeo.interfaces import (
            IWildcardmediaVimeoLayer)
        from plone.browserlayer import utils
        self.assertIn(IWildcardmediaVimeoLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = WILDCARDMEDIA_VIMEO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['wildcardmedia.vimeo'])

    def test_product_uninstalled(self):
        """Test if wildcardmedia.vimeo is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'wildcardmedia.vimeo'))

    def test_browserlayer_removed(self):
        """Test that IWildcardmediaVimeoLayer is removed."""
        from wildcardmedia.vimeo.interfaces import \
            IWildcardmediaVimeoLayer
        from plone.browserlayer import utils
        self.assertNotIn(IWildcardmediaVimeoLayer, utils.registered_layers())
