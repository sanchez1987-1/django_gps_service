import json
from datetime import datetime

from django.forms import model_to_dict
from django.utils.dateparse import parse_date, parse_datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DataApi, DataApiSerializer, UserParamsApi

class DataList(APIView):

    def get(self, request):
        id = request.user
        json_data = request.GET
        sdate = parse_date(str(json_data.get('start_date')))
        edate = parse_date(str(json_data.get('end_date')))
        date = parse_date(str(json_data.get('date')))
        print(id)
        if sdate and edate:
            queryset = DataApi.objects.filter(app_id=id, timestamp__range=[sdate, edate]).order_by('-timestamp')
        elif sdate:
            queryset = DataApi.objects.filter(app_id=id, timestamp__gte=sdate).order_by('-timestamp')
        elif date:
            queryset = DataApi.objects.filter(app_id=id, timestamp__date=date).order_by('-timestamp')
        else:
            queryset = DataApi.objects.filter(app_id=id).order_by('-timestamp')

        serializer_for_queryset = DataApiSerializer(
            instance=queryset,  # Передаём набор записей
            many=True  # Указываем, что на вход подаётся именно набор записей
        )
        return Response(
            data=serializer_for_queryset.data,
            status=200,
        )


class UserParamList(APIView):

    def get(self, request):
        id = request.user
        queryset = UserParamsApi.objects.filter(app_id=id).first()
        if queryset:
            context = model_to_dict(queryset)["app_params"]
            return Response(
                data=json.loads(context),
                status=200,
            )
        else:
            return Response(
                status=404,
            )


class DataLoad(APIView):

    def post(self, request):
        try:
            data = dict()
            data['value'] = json.dumps(request.data)
            if(request.data["date"]):
                date = parse_datetime(request.data["date"]).isoformat()
            else:
                date = datetime.now().isoformat()
            data['content_type'] = request.headers['Content-Type']
            data['app_id'] = request.headers['X-App-ID']
            data['timestamp'] = date

            serializer = DataApiSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response('OK', status=status.HTTP_200_OK)
        except Exception as err:
            msg = f"Unexpected {err=}, {type(err)=}"
            print(msg)
            return Response(msg, status=status.HTTP_200_OK)
