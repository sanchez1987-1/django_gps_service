from django.core.serializers import serialize
from django.shortcuts import render
from django.views.generic import ListView
import json
from geopy.distance import geodesic as GD
from dateutil import parser

from .models import Data


class DataListView(ListView):
    model = Data
    template_name = 'map.html'
    # context_object_name = 'data'


def gps_view(request):
    data = list(Data.objects.filter(app_id="rav4").order_by('-id'))
    # data = list(Data.objects.filter(app_id="rav4").order_by('-id').values()[:2])
    # data = list(Data.objects.filter(app_id="rav4").order_by('-id')[:2])
    data_json = json.loads(serialize("json", data))
    # print(speed_from_gps(data_json))
    # return render(request, "map.html", context={'data': json.dumps(speed_from_gps(data_json))})
    return render(request, "map.html", context={'data': json.dumps(data_json)})


def speed_from_gps(coord_array):
    dist = 0
    arr = []
    for i in range(len(coord_array) - 1):
        d1 = coord_array[i]['fields']
        p1 = json.loads(d1['value'])
        t1 = parser.parse(d1['timestamp'])
        d2 = coord_array[i + 1]['fields']
        p2 = json.loads(d2['value'])
        t2 = parser.parse(d2['timestamp'])
        p1.pop(2)
        p2.pop(2)
        t = ((t1 - t2).total_seconds())
        dist = dist + GD(p1, p2).km
        speed = round(GD(p1, p2).km * 3600 / t)
        coord_array[i]["calc_speed"] = speed
        arr.append(coord_array[i])
        # print("Speed: ", round(GD(p1, p2).km * 3600 / t))
    return arr
