
class LazySite(object):
    def __get__(self, request, obj_type=None):
        if not hasattr(request, '_cached_site'):
            from django.contrib.sites.models import Site
            request._cached_site = Site.objects.get(domain=request.get_host().split(":")[0].lower())
        return request._cached_site

class SiteMiddleware(object):
    def process_request(self, request):
        request.__class__.site = LazySite()
        return None

