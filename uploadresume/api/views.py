from rest_framework.response import Response
from api.serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status
from api.models import Profile

# Create your views here.
class ProfileView(APIView):
    def post(self,request,format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Resume Upload Successfully','status':'success',
                             'canidate':serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def get(self,request,format=None):
        candidates = Profile.objects.all()
        serializer = ProfileSerializer(candidates,many=True)
        return Response({'status':'success','candidates':serializer.data},status=status.HTTP_200_OK)
    
    def delete(self,request,format=None):
        candidates = Profile.objects.all()
        return Response({'status':'success'})