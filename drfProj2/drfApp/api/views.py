from drfApp.models import Show,Platform
from rest_framework.response import Response
from rest_framework import status
from drfApp.api.serializers import ShowSerializer, PlatformSerializer
from rest_framework.views import APIView

class ShowListAV(APIView):
    def get(self,request):
        shows=Show.objects.all()
        serializer=ShowSerializer(shows, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=ShowSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class ShowAV(APIView):
    def get(self,request,pk):
        show=Show.objects.get(pk=pk)
        print(show.released_on)
        print(type(show.released_on))
        serializer=ShowSerializer(show)
        return Response(serializer.data)
    
    def post(self,request,pk):
        show=Show.objects.get(pk=pk)
        serializer=ShowSerializer(show,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,pk):
        show=Show.objects.get(pk=pk)
        show.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class PlatformListAV(APIView):
    def get(self,request):
        platforms=Platform.objects.all()
        serializer=PlatformSerializer(platforms, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=PlatformSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class PlatformAV(APIView):
    def get(self,request,pk):
        platform=Platform.objects.get(pk=pk)
        serializer=PlatformSerializer(platform)
        return Response(serializer.data)
    
    def post(self,request,pk):
        platform=Platform.objects.get(pk=pk)
        serializer=PlatformSerializer(platform,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        platform=Platform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    