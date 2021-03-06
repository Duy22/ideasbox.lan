import datetime

import factory
from factory.fuzzy import FuzzyText

from ideasbox.tests.factories import UserFactory

from ..models import Entry, Inventory, Specimen, StockItem


class EntryFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    module = 'cinema'

    class Meta:
        model = Entry


class InventoryFactory(factory.django.DjangoModelFactory):
    made_at = factory.LazyAttribute(lambda o: datetime.datetime.utcnow())

    class Meta:
        model = Inventory


class StockItemFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "Stock item %03d" % n)
    module = 'cinema'

    class Meta:
        model = StockItem


class SpecimenFactory(factory.django.DjangoModelFactory):
    barcode = FuzzyText(length=6)
    item = factory.SubFactory(StockItemFactory)

    class Meta:
        model = Specimen
