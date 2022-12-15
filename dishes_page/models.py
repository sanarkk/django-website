from django.db import models
from django_resized import ResizedImageField


order_status_choices = (
    ("1", "Pending"),
    ("2", "In cart")
)

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    ingredients = models.TextField()
    serving_size = models.IntegerField()
    price = models.IntegerField()
    image = ResizedImageField(
        size=[150, 150],
        upload_to="dishes",
        blank=True,
        null=True,
    )

    objects = models.Manager()

    def __str__(self):
        return f"{self.name}"

