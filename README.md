# wagtail-neuralyzer

Pairs with [django-neuralyzer](https://github.com/webu/django-neuralyzer/), with wagtail support.

## Install

```
pip install wagtail-neuralyzer
```

## Register a model to have neuralyze action

Add `wagtail_neuralyzer` to your `INSTALLED_APP`:

```py
INSTALLED_APP = [
    ...
    "django_neuralyzer",
    "wagtail_neuralyzer",
    ...
]
```

```py

```

Add the `NeuralyzeSnippetViewSetMixin` to your snippet class:

```py

from wagtail_neuralyzer.views import NeuralyzeSnippetViewSetMixin
from wagtail_neuralyzer.views import NeuralyzeView

from my_app.neuralyzers import PersonNeuralyzer

# Create a new view that handle url and action as well as neuralyzer class
class OperatorNeuralyzeView(NeuralyzeView):
    neuralyzer_class = OperatorNeuralyzer


# inherit NeuralyzeSnippetViewSetMixin to register new url and neuralyze view
class PersonSnippetViewSet(NeuralyzeSnippetViewSetMixin, SnippetViewSet):
    model = Person
    neuralyze_view_class = OperatorNeuralyzeView
    ...
```

And _Tada_, your model should have an "Anonymize" action together with save/delete/publish/...
