from django.shortcuts import render
from rest_framework import permissions, generics 
from .models import TrustScore
from .serializers import TrustScoreSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .tasks import collect_user_signals

# Create your views here.
class TrustScoreDetail(generics.RetrieveAPIView):
    queryset = TrustScore.objects.all()
    serializer_class = TrustScoreSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'user_id'

class CollectSignalsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        collect_user_signals.delay(user_id)
        return Response({"message": "Signal collection initiated."})