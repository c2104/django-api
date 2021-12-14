# coding: utf-8
from rest_framework import serializers
from .models import AiAnalysisLog

class AiAnalysisLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AiAnalysisLog
        fields = ('image_path',)
