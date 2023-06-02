from django.db import models
from polymorphic.models import PolymorphicModel
from django.contrib.contenttypes.models import ContentType

__all__ = [
    'Project',
    'ArtProject',
    'ResearchProject'
]

class Project(PolymorphicModel):
    topic = models.CharField(max_length=30)

class ArtProject(Project):
    artist = models.CharField(max_length=30)

class ResearchProject(Project):
    supervisor = models.CharField(max_length=30)

# Project.objects.create(topic="Department Party")
# ArtProject.objects.create(topic="Painting with Tim", artist="T. Turner")
# ResearchProject.objects.create(topic="Swallow Aerodynamics", supervisor="Dr. Winter")
# Project.objects.all()
# Project.objects.instance_of(ArtProject)
# Project.objects.instance_of(ArtProject) | Project.objects.instance_of(ResearchProject)
# ctype = ContentType.objects.get_for_id(object.polymorphic_ctype_id)