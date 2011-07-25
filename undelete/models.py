from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

from undelete.managers import TrashedManager, NonTrashedManager

class TrashableMixin(models.Model):
    trashed_at = models.DateTimeField(_('Trashed'), editable=False, blank=True, null=True)

    objects = NonTrashedManager()
    trash = TrashedManager()

    # delete() method for object is not necessarily called when deleting
    # objects in bulk using a QuerySet. In future we should probably use 
    # pre_delete signal.
    def delete(self, *args, **kwargs):
        # keyword argument trash has default value True
        trash=kwargs.get('trash', True)
        if not self.trashed_at and trash:
            self.trashed_at = datetime.now()
            self.save()
        else:
            super(SomeModel, self).delete(*args, **kwargs)

    def restore(self, commit=True):
        self.trashed_at = None
        if commit:
            self.save()
