# django-monorepo-with-hatch

An exploration of Hatch in a monorepo-style setup, with Django and non-Django dependencies.

```
hatch run pytest
```

```
hatch run dj:django-admin migrate
hatch run dj:django-admin runserver
```

```
hatch run dj:django-admin startapp myapp packages/dj/src/dj/myapp
$EDITOR packages/dj/src/dj/myapp/apps.py  # fix name to be dj.myapp
$EDITOR packages/dj/src/dj/settings.py    # add dj.myapp to INSTALLED_APPS
```
