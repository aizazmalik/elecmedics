import django_filters
from .models import Prescription

class PrescriptionFilterSet(django_filters.FilterSet):
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None, strict=None, form=None, **kwargs):
        super().__init__(data=data, queryset=queryset, request=request, prefix=prefix, strict=strict, **kwargs)
        self.form = form or self.form

    class Meta:
        model = Prescription
        fields = {
            'created_at': ['gte', 'lte'],
        }