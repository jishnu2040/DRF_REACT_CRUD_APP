from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserCreateSerializer, UserSerializer

User = get_user_model()


# register a/c here
class RegisterView(APIView):
    def post(self, request): 
        data = request.data

        # data vaildating here if data is valid it create a new user 
        serializedData = UserCreateSerializer(data= data)

        if not serializedData.is_valid():
            return Response(serializedData.errors, status=status.HTTP_400_BAD_REQUEST)
        

        user = serializedData.create(serializedData.validated_data)
        user = UserSerializer(user)


        return Response(user.data, status=status.HTTP_201_CREATED)

# retrieve authentication data from here
class RetrieveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        user = request.user
        user = UserSerializer(user)

        return Response(user.data,  status=status.HTTP_201_CREATED)