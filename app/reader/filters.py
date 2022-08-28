import django_filters
from django_filters import filters

from reader.models import Reader


class ReaderFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Reader
        fields = ['title', 'language', 'company']
