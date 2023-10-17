import json

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DataApi, DataApiSerializer


class DataList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        json_data = request.data
        sdate = json_data.get('start_date')
        edate = json_data.get('end_date')
        date = json_data.get('date')
        if sdate and edate:
            queryset = DataApi.objects.filter(app_id="rav4", timestamp__range=[sdate, edate]).order_by('-timestamp')
        elif sdate:
            queryset = DataApi.objects.filter(app_id="rav4", timestamp__gte=sdate).order_by('-timestamp')
        elif date:
            queryset = DataApi.objects.filter(app_id="rav4", timestamp__date=date).order_by('-timestamp')
        else:
            queryset = DataApi.objects.filter(app_id="rav4").order_by('-id')
        serializer_for_queryset = DataApiSerializer(
            instance=queryset,  # Передаём набор записей
            many=True  # Указываем, что на вход подаётся именно набор записей
        )
        return Response(
            data=serializer_for_queryset.data,
            status=200,
        )

