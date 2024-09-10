from rest_framework import serializers
from drfApp.models import Show,Platform
from datetime import date

class ShowSerializer(serializers.ModelSerializer):

    class Meta:
        model=Show
        fields="__all__"

    #custom field
    age=serializers.SerializerMethodField()

    def get_age(self,object):
        today = date.today()
        obj_date=object.released_on
        return str(today.year - obj_date.year - ((today.month, today.day) < (obj_date.month, obj_date.day)))+" years old"


    def validate_rating(self,value):
        if value>10 or value<0:
            raise serializers.ValidationError("Rating can be 0-10")
        return value

class PlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model=Platform
        fields="__all__"
    
    shows_available=ShowSerializer(many=True, read_only=True)

    # For only showing the name(__str__()) of the objects
    # shows_available=serializers.StringRelatedField(many=True)