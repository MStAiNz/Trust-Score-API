from rest_framework import serializers
from .models import TrustScore
from django.contrib.auth.models import User


class TrustScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrustScore
        fields = ['id', 'user', 'score', 'updated_at']
        read_only_fields = ['updated_at']