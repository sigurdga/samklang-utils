from urllib import quote
from samklang_menu.widgets import Widget
from django.template.loader import render_to_string
from django.template.context import RequestContext

class SiteShare(Widget):
    """Buttons for sharing the site on social media services."""

    def render(self, request):
        """Function to be called to be printed"""


        return render_to_string('samklang_utils/site_share.html', {
            "site_name_encoded": quote(request.site.name),
            "site_url_encoded": quote("http://" + request.site.domain + "/"),
            }, context_instance=RequestContext(request))
