from django.db import models
from rest_framework import serializers


class DataApi(models.Model):
    content_type = models.CharField(max_length=100)
    value = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    app_id = models.CharField(max_length=100)

    class Meta:
        db_table = "data"
        managed = False


class DataApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataApi
        fields = '__all__'


class UserParamsApi(models.Model):
    param_id = models.AutoField(primary_key=True)
    app_id = models.CharField(max_length=100)
    app_params = models.TextField
    app_pass = models.CharField(max_length=200)
    app_api_key = models.CharField(max_length=100)

    class Meta:
        db_table = "user_params"
        managed = False
