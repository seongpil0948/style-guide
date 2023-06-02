import cProfile
from django.contrib.auth.models import User

from app.serializers import serialize_user, UserModelSerializer, \
  UserReadOnlyModelSerializer, UserSerializer, UserReadOnlySerializer

""" 
Summary


SERIALIZER	                SECONDS
UserModelSerializer	        12.818
UserReadOnlyModelSerializer	7.407
UserSerializer	            2.101
UserReadOnlySerializer	    2.254
serialize_user	            0.034
"""

u = User.objects.first()

cProfile.run('for i in range(5000): UserModelSerializer(u).data', sort='tottime')

# Only 7.4 seconds. A 40% improvement compared to the writable ModelSerializer.
cProfile.run('for i in range(5000): UserReadOnlyModelSerializer(u).data', sort='tottime')

# light 
cProfile.run('for i in range(5000): serialize_user(u)', sort='tottime')

"""
regular
That's 60% faster than the read only ModelSerializer, and a whooping 85% faster than the writable ModelSerializer.
"""
cProfile.run('for i in range(5000): UserSerializer(u).data', sort='tottime')

"""
regular ReadOnly
This reaffirms(다시 강조) that the time was spent on validations derived
from the model's field definitions.
"""
cProfile.run('for i in range(5000): UserReadOnlySerializer(u).data', sort='tottime')