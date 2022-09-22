import django_filters
from.models import Product ,MEMORY
from django import forms
from django_filters import NumberFilter,BooleanFilter



class ProductFilter(django_filters.FilterSet) :
    name = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    Memory = django_filters.ChoiceFilter(choices=MEMORY)


class Meta :
        model =Product
        fields = ['name', 'price','is_garanted','is_promo','color','brand','Memory']


        def author_sort_books(self, queryset, name, value):
            return queryset







