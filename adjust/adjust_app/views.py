from rest_framework.generics import ListAPIView

from .serializers import AppStatSerializer
from .models import AppStat
from .filters import AppStatFilter


class AppStatsListView(ListAPIView):
    serializer_class = AppStatSerializer
    filterset_class = AppStatFilter

    def get_queryset(self):
        return AppStat.objects.all()
