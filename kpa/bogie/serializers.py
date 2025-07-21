from rest_framework import serializers
from .models import BogieChecksheet,WheelSpecification

class Bogie_Checksheet(serializers.ModelSerializer):
    class Meta:
        model = BogieChecksheet
        fields ='__all__'
        
class Wheel_Specification(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecification
        fields ='__all__'        