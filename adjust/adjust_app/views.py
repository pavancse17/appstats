from rest_framework.generics import ListAPIView

from adjust_app.serializers import AppStatSerializer
from adjust_app.models import AppStat
from adjust_app.filters import AppStatFilter


class AppStatsListView(ListAPIView):
    serializer_class = AppStatSerializer
    filterset_class = AppStatFilter

    def get_queryset(self):
        return AppStat.objects.all()
