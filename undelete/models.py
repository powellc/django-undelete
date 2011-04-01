from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

from undelete.managers import TrashedManager, NonTrashedManager

class TrashableMixin(models.Model):
	trashed_at = models.DateTimeField(_('Trashed'), editable=False, blank=True, null=True)

	objects = NonTrashedManager()
	trash = TrashedManager()

	def delete(self, *args, **kwargs, trash=True):
	    if not self.trashed_at and trash:
	        self.trashed_at = datetime.now()
	        self.save()
	    else:
			super(SomeModel, self).delete(*args, **kwargs)

	def restore(self, commit=True):
		self.trashed_at = None
		if commit:
			self.save()