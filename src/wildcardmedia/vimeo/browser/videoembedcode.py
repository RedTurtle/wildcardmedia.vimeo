# -*- coding: utf-8 -*-

from zope.interface import implements
from wildcard.media.adapter import IVideoEmbedCode
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
from urlparse import urlparse


class VimeoEmbedCode(object):
    """ Wildcard.media - Vimeo support
    """

    implements(IVideoEmbedCode)
    template = ViewPageTemplateFile('templates/vimeoembedcode_template.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return self.template()

    def getVideoURL(self):
        return self.context.video_url

    def getVideoLink(self):
        video_id = urlparse(self.context.video_url)[2].split('/')[-1]
        video_url = "https://player.vimeo.com/video/%s" % video_id
        return self.check_autoplay(video_url)

    def check_autoplay(self, url):
        """Check if the we need to add the autoplay parameter, and add it to the URL"""
        if self.context.video_url.lower().find('autoplay=1')>-1 or \
                self.request.QUERY_STRING.lower().find('autoplay=1')>-1:
            url += '?autoplay=1'
        return url
