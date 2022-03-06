from dataclasses import fields
from rest_framework import serializers
from .models import *


class ResponseDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseData
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    # questionId = QuestionSerializer(required=True)
    class Meta:
        model = OptionMaster
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    optons = OptionSerializer(many=True, read_only=True)
    class Meta:
        model = QuestionMaster
        fields = ('id', 'question', 'shortName', 'optons')

    

