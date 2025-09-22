from rest_framework import serializers
from .models import TrustScore, Reputation
from django.contrib.auth.models import User
from .scoring import TrustScorer



class TrustScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrustScore
        fields = ['id', 'user', 'score', 'updated_at']
        read_only_fields = ['updated_at']

class ReputationSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField()
    explanation = serializers.SerializerMethodField()

    class Meta:
        model = Reputation
        fields = ["id", "user", "transaction", "social_signals", "blockchain", "score", "explanation"]

    def get_score(self, obj):
        scorer = TrustScorer()
        return scorer.score(obj.get_signals())

    def get_explanation(self, obj):
        scorer = TrustScorer()
        return scorer.explain(obj.get_signals())