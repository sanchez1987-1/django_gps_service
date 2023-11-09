import hashlib

from django.db import models
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class DataApi(models.Model):
    content_type = models.CharField(max_length=100)
    value = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    app_id = models.CharField(max_length=100)

    class Meta:
        db_table = "data"
        managed = False

    def __str__(self):
        return self.app_id

class DataApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataApi
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=DataApi.objects.all(),
                fields=['content_type', 'value', 'app_id']
            )
        ]

class UserParamsApi(models.Model):
    param_id = models.AutoField(primary_key=True)
    app_id = models.CharField(max_length=100)
    app_params = models.TextField()
    app_pass = models.CharField(max_length=200)
    app_api_key = models.CharField(max_length=100)

    class Meta:
        db_table = "user_params"
        managed = False

    def save(self, *args, **kwargs):
        md5 = hashlib.md5()
        md5.update(self.app_pass.encode('utf-8'))
        self.app_pass = md5.hexdigest()
        super(UserParamsApi, self).save(*args, **kwargs)

    def __str__(self):
        return self.app_params


