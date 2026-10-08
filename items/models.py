from django.db import models
from django.contrib.auth.models import User


class LostItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()

    date_lost = models.DateField()
    location_lost = models.CharField(max_length=150)

    image = models.ImageField(
        upload_to='lost_items/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name