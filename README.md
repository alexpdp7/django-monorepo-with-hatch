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

## Caveats

pytest is configured so that all tests in the workspace run with `hatch run pytest`.
This would not account for multiple Django projects, this command uses a single `DJANGO_SETTINGS_MODULE` variable.

[Basedpyright does not autodetect the Hatch environments, so code completion and others do not work. A workaround is to create a plain virtualenv at `.venv` that basedpyright will use.](https://github.com/DetachHead/basedpyright/issues/1889)
