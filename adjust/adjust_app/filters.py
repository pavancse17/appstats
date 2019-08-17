from django.db import models

import django_filters
from django_filters import filters

from .models import AppStat

GROUP_BY_CHOICES = (
    ('date', 'date'),
    ('channel', 'channel'),
    ('country', 'country'),
    ('os', 'os'),
)


class AppStatFilter(django_filters.FilterSet):
    date_from = filters.DateFilter(field_name='date', lookup_expr='gte')
    date_to = filters.DateFilter(field_name='date', lookup_expr='lte')
    os = filters.CharFilter(method="filter_os")
    channel = filters.CharFilter(lookup_expr='iexact')
    country = filters.CharFilter(lookup_expr='iexact')
    group_by = filters.MultipleChoiceFilter(choices=GROUP_BY_CHOICES, method='group_the_query')
    o = filters.OrderingFilter(
        fields=(
            'date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue', 'cpi'
        ),
    )

    @staticmethod
    def filter_os(qs, field_name, value):
        if value.lower() == 'android':
            value = AppStat.ANDROID
        elif value.lower() == 'ios':
            value = AppStat.IOS
        else:
            value = None

        return qs.filter(os=value)

    def group_the_query(self, qs, field_name, group_by_fields):
        can_display_fields = list(set(self.data) & set(['date', 'os', 'channel', 'country']))
        group_by_fields = group_by_fields + can_display_fields

        return qs.values(*group_by_fields).annotate(
            impressions=models.Sum('impressions'), clicks=models.Sum('clicks'), installs=models.Sum('installs'),
            spend=models.Sum('spend'), revenue=models.Sum('revenue'),
            cpi=models.ExpressionWrapper(models.F('spend') / models.F('installs'), output_field=models.FloatField())
        ).order_by(*group_by_fields)

    class Meta:
        model = AppStat
        fields = '__all__'
