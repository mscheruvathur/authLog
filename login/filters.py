from django.contrib.auth.models import User,auth
import django_filters

class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='username',lookup_expr='icontains',label='search')

    class Meta:
        model = User
        fields = ['name']