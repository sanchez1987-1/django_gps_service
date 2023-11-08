import json
from datetime import datetime

from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DataApi, DataApiSerializer, UserParamsApi


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


class UserParamList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

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
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        content_type = request.headers['Content-Type']
        app_id = request.headers.get('X-App-ID')
        data = request.data
        print(data)

        serializer = DataApiSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, status=DataApi.SENT)
        return Response(status=status.HTTP_201_CREATED)

    # def post(self, request):
    #     content_type = request.headers['Content-Type']
    #     app_id = request.headers.get('X-App-ID')
    #     msg = ""
    #
    #     serializer = DataApiSerializer(data=request.data)
    #
    #     date = ""
    #     # print(request.data)
    #     data = request.POST
    #
    #     try:
    #         if 'application/json' in content_type:
    #             if data.get('value'):
    #                 value = str(data.get('value'))
    #                 date = str(data.get('date'))
    #             else:
    #                 value = json.dumps(data)
    #                 date = str(data.get('date'))
    #         else:
    #             value = data.get('value')
    #
    #         print(serializer)
    #
    #         if value is None or not app_id:
    #             return Response(status=status.HTTP_400_BAD_REQUEST)
    #
    #         if date:
    #             timestamp = date
    #         else:
    #             timestamp = datetime.utcnow().isoformat()
    #
    #         # conn = connect_to_database()
    #         # cursor = conn.cursor()
    #         # cursor.execute("SELECT * FROM data WHERE (content_type, value, timestamp, app_id) in ((%s, %s, %s, %s))", (content_type, value, timestamp, app_id))
    #         # data = cursor.fetchall()
    #         # if not data:
    #         #     cursor.execute('INSERT INTO data (content_type, value, timestamp, app_id) VALUES (%s, %s, %s, %s)', (content_type, value, timestamp, app_id))
    #         #     conn.commit()
    #         #     msg = jsonify({'message': 'Data saved successfully'})
    #         # else:
    #         #     msg = jsonify({'message': 'Double data'})
    #         # conn.close()
    #     except Exception as err:
    #         msg = f"Unexpected {err=}, {type(err)=}"
    #         print(msg)
    #     return JsonResponse(msg, safe=False, status=status.HTTP_400_BAD_REQUEST)
