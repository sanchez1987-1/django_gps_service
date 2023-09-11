from django.db import models


from rest_framework import serializers


class Data(models.Model):
    content_type = models.CharField(max_length=100)
    value = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    app_id = models.CharField(max_length=100)

    class Meta:
        db_table = "data"
        managed = False


class DataSerializer(serializers.Serializer):
    # initialize fields
    content_type = serializers.CharField()
    value = serializers.CharField()
    timestamp = serializers.DateTimeField()
    app_id = serializers.CharField()
