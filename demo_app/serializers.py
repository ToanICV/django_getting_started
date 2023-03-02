from rest_framework import serializers
from .models import Responser

class demo_serializer(serializers.ModelSerializer):
   class Meta:
      model = Responser
      fields = ('context', 'object', 'app_name',)