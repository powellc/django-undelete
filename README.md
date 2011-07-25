django-undelete
================

UnDelete is a simple project that gives you access to a TrashableMixin meta model and some useful managers as well.

Much of the work is heavily derivative of Simon Willison's [post on the same topic](http://ltslashgt.com/2007/07/18/undelete-in-django/).

Installation
-------------

In three easy steps!

1. Place 'undelete' in your installed apps.
2. Add:

        from undelete.models import TrashableMixin

3. Make sure your model inherits the mixin: 

        class YourMode(TrashabeMixin): ...`   

And you're done. You should now be able to query trashed items with the "trash" manager and non-trashed items with the usual objects manager.

You can now install django-undelete using pip, for example:
    pip install git+https://github.com/cpbotha/django-undelete.git

See the section below for a more through explanation.

Usage
------

With the steps above taken, managing trashed items is fairly straightforward:

    >>> YourModel.objects.count()
    10
    >>> YourModel.trash.count()
    0
    >>> obj = YourModel.objects.get(pk=1)
    >>> obj
    < YourModel: u'Test object' >
    >>> obj.delete()
    >>> obj
    < YourModel: u'Test object (trashed)' >
    >>> YourModel.objects.count()
    9
    >>> YourModel.trash.count()
    1
    >>> obj.restore()
    >>> obj
    < YourModel: u'Test object' >
    # Call delete twice and she's gone...
    >>> obj.delete()
    >>> obj.delete()
    # You can also skip the trash entierely
    >>> obj = YourModel.objects.get(pk=1)
    >>> obj.delete(trash=False)

Future plans also call for a management command to delete everything trashed a certain period of time ago. Stay tuned!

Caveats
-------
* delete() method is currently overridden. The [the django documentation](https://docs.djangoproject.com/en/dev/topics/db/models/#overriding-model-methods) states that the delete() method is not always called for bulk deletes based on a QuerySet. In future, django-undelete should make use of the pre_delete signal.

