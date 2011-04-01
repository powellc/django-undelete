django-undelete
================

UnDelete is a simple project that gives you access to a TrashableMixin meta model and some useful managers as well.

Much of the work is heavily derivative of Simon Willison's [post on the same topic](http://ltslashgt.com/2007/07/18/undelete-in-django/).

Installation
-------------

1. Place 'undelete' in your installed apps.
2. Add:

   `from undelete.models import TrashableMixin

    from undelete.managers import TrashableManager`

3. Make sure your model inherits the mixin: 

   `class YourMode(TrashabeMixin): ...`

4. Add a "trashed_at" datetime field to your model
5. Finally, add the TrashableManager() to your model 

   (And don't forget to explicitly define your original objects manager!)

   `objects = models.Manager()

    trash = TrashableManager()`

