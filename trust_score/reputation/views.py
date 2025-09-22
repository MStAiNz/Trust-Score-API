from django.shortcuts import render
from rest_framework import permissions, generics 
from .models import TrustScore, DataSource, AggregatedSignal, Reputation
from .serializers import TrustScoreSerializer, ReputationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .tasks import collect_user_signals
from rest_framework import viewsets
from .permissions import IsReputationAdmin

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
    
class ReputationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reputation.objects.all()
    serializer_class = ReputationSerializer
    
class ReputationAdminViewSet(viewsets.ModelViewSet):
    queryset = Reputation.objects.all()
    serializer_class = ReputationSerializer
    permission_classes = [IsAuthenticated, IsReputationAdmin]