# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import wildcardmedia.vimeo


class WildcardmediaVimeoLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=wildcardmedia.vimeo)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'wildcardmedia.vimeo:default')


WILDCARDMEDIA_VIMEO_FIXTURE = WildcardmediaVimeoLayer()


WILDCARDMEDIA_VIMEO_INTEGRATION_TESTING = IntegrationTesting(
    bases=(WILDCARDMEDIA_VIMEO_FIXTURE,),
    name='WildcardmediaVimeoLayer:IntegrationTesting'
)


WILDCARDMEDIA_VIMEO_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(WILDCARDMEDIA_VIMEO_FIXTURE,),
    name='WildcardmediaVimeoLayer:FunctionalTesting'
)


WILDCARDMEDIA_VIMEO_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        WILDCARDMEDIA_VIMEO_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='WildcardmediaVimeoLayer:AcceptanceTesting'
)
