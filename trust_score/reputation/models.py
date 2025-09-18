from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TrustScore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}"
    
class DataSource(models.Model):
    PLATFORM_CHOICES = [
        ('social', 'Social'),
        ('blockchain', 'Blockchain'),
        ('transaction', 'Transaction'),
    ]
    name = models.CharField(max_length=100, choices=PLATFORM_CHOICES)
    api_url = models.URLField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class AggregatedSignal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='signals')
    source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    raw_score = models.FloatField()
    normalized_score = models.FloatField()
    collected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username} - {self.source.name} - {self.normalized_score}"