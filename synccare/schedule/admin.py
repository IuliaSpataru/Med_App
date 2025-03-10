from django.contrib import admin
from synccare.schedule.models import Schedule
from django.utils import timezone
from datetime import timedelta


# Register your models here.

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('name', 'shift', 'ward', 'start_date', 'end_date', 'month')
    list_filter = ('shift', 'ward', 'start_date', 'end_date')
    search_fields = ('name__first_name', 'name__last_name')
    list_per_page = 10

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        current_month = timezone.now().month
        start_date_filter = request.GET.get('start_date')
        end_date_filter = request.GET.get('end_date')

        if start_date_filter and end_date_filter:
            queryset = queryset.filter(start_date__gte=start_date_filter, start_date__lte=end_date_filter)
        elif start_date_filter:
            queryset = queryset.filter(start_date__gte=start_date_filter)
        elif end_date_filter:
            queryset = queryset.filter(start_date__lte=end_date_filter)
        else:
            queryset = queryset.filter(start_date__month=current_month)

        return queryset


    def month(self, obj):
        return obj.start_date.strftime('%B %Y')

    month.short_description = 'Month'