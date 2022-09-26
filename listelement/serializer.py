from xml.dom.minidom import Element
from rest_framework import serializers

class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        field = '__all__'