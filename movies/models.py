from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


# Create your models here.

class Review(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=False, null=False)
    rating = models.FloatField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    created_date = models.DateField(default=timezone.now)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.comment

class Movie(models.Model):
    title = models.CharField(max_length=140)
    summary_text = models.TextField()
    poster = models.ImageField(upload_to="posters")
    director = models.CharField(max_length=140)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(default=timezone.now)
    slug = models.SlugField(max_length=140)
    review = GenericRelation('Review')

    class Meta:
        ordering = ["-created_by"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

