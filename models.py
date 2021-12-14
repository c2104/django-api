from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class AiAnalysisLog(models.Model):
    id = models.AutoField(primary_key = True)
    image_path = models.CharField(
        blank = True,
        null = True,
        max_length = 255,
    )
    success = models.CharField(
        blank = True,
        null = True,
        max_length = 255,
    )
    message = models.CharField(
        blank = True,
        null = True,
        max_length = 255,
    )
    classes = models.IntegerField(
        blank = True,
        null = True,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(11)
        ]
    )
    confidence = models.DecimalField(
        max_digits=5,
        decimal_places=4,
        blank=True,
        null=True,
    )
    request_timestamp = models.PositiveIntegerField(
        blank = True,
        null = True,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )
    response_timestamp = models.PositiveIntegerField(
        blank = True,
        null = True,
        validators = [
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )

    class Meta:
        db_table = 'ai_analysis_log'
        ordering = ['id']