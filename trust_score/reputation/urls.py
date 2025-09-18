from django.urls import path
from .views import TrustScoreDetail, CollectSignalsView

urlpatterns = [
    path('<int:user_id>/', TrustScoreDetail.as_view(), name='trust_score_detail'),
    path('collect/<int:user_id>/', CollectSignalsView.as_view(), name='collect_signals'),
]