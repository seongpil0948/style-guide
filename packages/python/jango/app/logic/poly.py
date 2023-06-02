from app.models import *
from app.utils.printing import only_print_info
from django.contrib.contenttypes.models import ContentType

@only_print_info(repeat_time=1000, print_queries=True)
def bad(): # queries = 3000
    result = []
    queries = Project.objects.all()
    result += [i.get_real_instance() for i in queries]
    return result

@only_print_info(repeat_time=1000, print_queries=True)
def better(): # queries = 1000
    return list(Project.objects.all())

@only_print_info(repeat_time=1000, print_queries=True)
def hmm(): # queries = 1000
    return list(ArtProject.objects.all())

@only_print_info(repeat_time=1000, print_queries=True)
def a(): # queries = 1000
    return list(Library.objects.all())

@only_print_info(repeat_time=1000, print_queries=False)
def b(): # queries = 1000
    return Library.objects.all()

ctype = ContentType.objects.get_for_id(object.polymorphic_ctype_id)