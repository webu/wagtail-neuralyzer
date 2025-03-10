from django_neuralyzer.base import BaseNeuralizer

from .models import Person


class PersonNeuralizer(BaseNeuralizer):
    first_name = "toto"
    last_name = "tutu"

    class Meta:
        model = Person
