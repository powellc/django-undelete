from django.db import models

class NonTrashedManager(models.Manager):
    ''' Query only objects which have not been trashed. '''
    def get_query_set(self):
        query_set = super(NonTrashedManager, self).get_query_set()
        return query_set.filter(trashed_at__isnull=True)

class TrashedManager(models.Manager):
    ''' Query only objects which have been trashed. '''
    def get_query_set(self):
        query_set = super(TrashedManager, self).get_query_set()
        return query_set.filter(trashed_at__isnull=False)
