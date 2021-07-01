from rest_framework import serializers
import enum
from rest_enumfield import EnumField


class CustomMetaClass(serializers.SerializerMetaclass):
    def __new__(cls, name, bases, attrs):
        custom_fields_mapping = attrs.get('custom_fields_mapping')

        if custom_fields_mapping:
            for label, value in custom_fields_mapping.items():
                if attrs.get(label):
                    attrs[value] = attrs.pop(label)
        return super().__new__(cls, name, bases, attrs)

class PowerPlantType(enum.Enum):
    GASFIRED = "gasfired"
    TURBOJET = "turbojet"
    WINDTURBINE = "windturbine"

class FuelsSerializer(serializers.Serializer, metaclass=CustomMetaClass):
    custom_fields_mapping = {
        "gas": "gas(euro/MWh)", 
        "kerosine": "kerosine(euro/MWh)", 
        "co2": "co2(euro/ton)", 
        "wind": "wind(%)"
    }

    gas = serializers.FloatField()
    kerosine = serializers.FloatField()
    co2 = serializers.FloatField()
    wind = serializers.FloatField()

class PowerPlantSerializer(serializers.Serializer):
    name: serializers.CharField()
    type = EnumField(choices=PowerPlantType)
    efficiency: serializers.FloatField()
    pmin: serializers.IntegerField()
    pmax: serializers.IntegerField()
    
class ProductionplanSerializer(serializers.Serializer):

    def validate(self, data):
            """
            Check that start is before finish.
            """
            if data['load'] == 0:
                raise serializers.ValidationError("the load must be declared with a value greater than zero")
            return data


    load = serializers.IntegerField(initial=0, default=0)
    fuels = FuelsSerializer()
    powerplants = serializers.ListField(child=PowerPlantSerializer())