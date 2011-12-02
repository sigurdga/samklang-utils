
class LazySite(object):
    def __get__(self, request, obj_type=None):
        if not hasattr(request, '_cached_site'):
            from site.models import Site
            request._cached_site = Site.objects.get(request.get_host().lower())
        return request._cached_site

class SiteMiddleware(object):
    def process_request(self, request):
        request.__class__.site = LazySite()
        return None

