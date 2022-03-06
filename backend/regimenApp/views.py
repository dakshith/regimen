from itertools import count
from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import QuestionSerializer, ResponseDataSerializer, OptionSerializer
from .models import *
from django.core import serializers
from django.http import JsonResponse
from rest_framework import viewsets




def index(request):
    return render(request, 'build/index.html')

@api_view(['GET'])
def getQuestionOptions(request):
    try: 
        queryset = QuestionMaster.objects.all()
        serializer_class = QuestionSerializer(queryset, many=True)
        data = {"status":"sucess", "rquestonaries":serializer_class.data}
        return Response(data)
    except Exception as e:
        data = {"status":"Failed", "error":e}
        return Response(data)

@api_view(['POST'])
def IiefQuestionnaire(request):
    try:
        requestData = request.data
        if requestData['type'] == 'IiefQuestionnaire':
            requestData.pop("type") 
            scoreList = requestData.values()
            iiefScore = sum(scoreList)
            netDataSet = {}
            for key, item in requestData.items():
                question = QuestionMaster.objects.filter(shortName = key).last()
                option = OptionMaster.objects.filter(questionId = question, optionWeight = item).last()
                netDataSet[key] = option.option
            netDataSet['score'] = iiefScore
            netDataSet['avgScore'] = iiefScore/len(scoreList)
            serializer = ResponseDataSerializer(data=netDataSet)
            if serializer.is_valid():
                serializer.save()
                data = {"data":{"type":"IiefQuestionnaire","id":serializer['id'].value,"attributes":{"score":iiefScore}}}
            else:
                data = {"data":{"type":"IiefQuestionnaire","error":"Something went wrong !"}}
        else:
            data = {"data":{"type":requestData['type'],"error":"Invalid type"}}
        return Response(data)
    except Exception as e:
        data = {"data":{"type":"IiefQuestionnaire","error":e.text}}
        return Response(data)