from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import re

"""
https://docs.djangoproject.com/en/3.1/howto/custom-model-fields/

1. first give some thought to which existing Field class your new field is most similar to
    subclass an existing Django field and save yourself some work
2. Put a __str__() method on the class you’re wrapping up as a field. 
    There are a lot of places where the default behavior of the field code is to call str() on the value.
    (In our examples in this document, value would be a Hand instance, not a HandField). 
    So if your __str__() method automatically converts to the string form of your Python object, 
    you can save yourself a lot of work.
"""

class Hand:
    "A hand of cards (bridge style)"
    def __init__(self, north, east, south, west):
        # Input parameters are lists of cards ('Ah', '9s', etc.)
        self.north = north
        self.east = east
        self.south = south
        self.west = west


"""
Python object that your users will manipulate.
Our HandField accepts most of the standard field options (see the list below), 
104 characters in total.
"""

class HandField(models.Field):
    " Doc string "
    description = "A hand of cards (bridge style)"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 104
        self.separator = kwargs.pop('separator', None)
        super().__init__(*args, **kwargs)

    # 해체하다
    def deconstruct(self): 
        """
        name, path, args, kwargs = my_field_instance.deconstruct()
        new_instance = MyField(*args, **kwargs)
        self.assertEqual(my_field_instance.some_attribute, new_instance.some_attribute)
        """      
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]

        if self.separator != ",":
          kwargs['separator'] = self.separator
        return name, path, args, kwargs
    




class MytypeField(models.Field):
    """
    Say you’ve created a PostgreSQL custom type called mytype
    when the framework constructs the CREATE TABLE statements for your application 
    that is, when you first create your tables. 
    """
    def db_type(self, connection):
        if connection.settings_dict['ENGINE'] == 'django.db.backends.mysql':
            return 'datetime'
        else:
            return 'my_type'

class BetterCharField(models.Field):
    def __init__(self, *args, **kwargs):
        max_length = kwargs.pop("max_length", None)
        if max_length is not None:
            self.max_length = max_length
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'char(%s)' % self.max_length


class Person(models.Model):
    name = models.CharField(max_length=80)
    something_else = MytypeField()
    haha = BetterCharField(max_length=255)

"""
The rel_db_type() method is called by fields such as ForeignKey and OneToOneField
that point to another field to determine their database column data types. For example,
if you have an UnsignedAutoField, you also need the foreign keys that point to
that field to use the same data type
"""

class UnsignedAutoField(models.AutoField):
    def db_type(self, connection):
        return 'integer UNSIGNED AUTO_INCREMENT'

    def rel_db_type(self, connection):
        return 'integer UNSIGNED'


"""
from_db_value() will be called in all circumstances when the data is loaded from the database
ex) https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.values

to_python() is called by deserialization and during the clean() method used from forms.
https://docs.djangoproject.com/en/3.1/ref/models/instances/#django.db.models.Model.clean

in the from_db_value(). 
we need to be able to process strings and None 
In to_python(), 
we need to also handle Hand instances:

"""


def parse_hand(hand_string):
    """Takes a string of cards and splits into a full hand."""
    p1 = re.compile('.{26}')
    p2 = re.compile('..')
    args = [p2.findall(x) for x in p1.findall(hand_string)]
    if len(args) != 4:
        raise ValidationError(_("Invalid input for a Hand instance"))
    return Hand(*args)

class HandField2(HandField):

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return parse_hand(value)

    def to_python(self, value):
        if isinstance(value, Hand):
            return value

        if value is None:
            return value

        return parse_hand(value)

"Converting field data for serialization"
class HandField3(HandField2):
    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)    