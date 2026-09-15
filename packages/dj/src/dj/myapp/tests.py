import pytest

from dj.myapp import models


@pytest.mark.django_db
def test():
    models.Foo(bar="xxx").save()

