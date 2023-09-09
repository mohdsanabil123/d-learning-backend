from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .serializer import UserSerializer, NewsSerializer, UserAccountSerializer
from .models import News, UserAccount
from django.contrib.auth import get_user_model

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
        
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


# Getting user details by token.

@csrf_exempt
def user_login(request):
    if request.method == 'GET':
        try:
            token = request.headers['Token']
            user = Token.objects.get(key=token).user
            # print(user)

            return JsonResponse(
            {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone_number": user.phone_number,
                "email": user.email,
                "address": user.address,
                "school_name": user.school_name,
                "std": user.std
            }, safe=False)
        except:
            return JsonResponse( {"error": "Invalid or missing token"}, safe=False )

# Getting Account of student by student id.

@csrf_exempt
def user_account(request):
    if request.method == 'GET':
        try:
            token = request.headers['Token']
            user = Token.objects.get(key=token).user
            
            user_account = UserAccount.objects.filter(user=user.id)
            user_account_serializer = UserAccountSerializer(user_account, many=True)
            
            return JsonResponse(user_account_serializer.data, safe=False)

        except:
            return JsonResponse({'error': 'no authorization token'}, safe=False)