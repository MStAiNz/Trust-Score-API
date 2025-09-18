from celery import shared_task
from .models import TrustScore, AggregatedSignal, DataSource
from django.contrib.auth.models import User
from .utilis.normalizer import normalize_score
from .services import fetchers

FETCHER_APPS = {
    'social': fetchers.fetch_social_data,
    'blockchain': fetchers.fetch_blockchain_data,
    'transaction': fetchers.fetch_transaction_data,
}

@shared_task
def collect_user_signals(user_id: int):
    user = User.objects.get(id=user_id) 
    sources = DataSource.objects.filter(active=True)

    for source in sources:
        raw_value = FETCHER_APPS[source.name](user_id)
        norm_value = normalize_score(source.name, raw_value)
        
        AggregatedSignal.objects.create(
            user=user,
            source=source,
            raw_score=raw_value,
            normalized_score=norm_value
        )

    return f"Collected signals for user {user.username}"

