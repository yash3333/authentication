import employe
from rest_framework import serializers
from.models import*

class EmployeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Worker
        fields='__all__'