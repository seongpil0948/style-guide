from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User


class Outfit(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField() 
    content_object = GenericForeignKey('content_type', 'object_id')
    garment = models.UUIDField()

class UserOutfit(models.Model):
    outfit = GenericRelation('Outfit', related_query_name='users')
    user = GenericRelation('User', related_query_name='Outfit')
    

class LikeLog(models.Model):
    # 생략
     = GenericRelation('Like', related_query_name='post')
    
    
class FashionLog(models.Model):
    # 생략
    like = GenericRelation('Like', related_query_name='comment')
    