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
```
