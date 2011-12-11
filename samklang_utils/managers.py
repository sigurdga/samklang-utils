from django.db.models import Manager
from django.db.models.query_utils import Q

class PermissionManager(Manager):

    def for_user(self, user=None):
        if user and user.is_authenticated():
            return self.get_query_set().filter(Q(group=None) | Q(group__user=user))
        else:
            return self.get_query_set().filter(group=None)
