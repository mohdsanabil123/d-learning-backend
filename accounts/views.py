from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .serializer import UserSerializer, NewsSerializer, UserAccountSerializer, NotesSerializer, ContactSerializer
from .models import News, UserAccount, Notes, Contact
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
    
class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# Getting user details by token.

@csrf_exempt
def user_profile(request):
    if request.method == 'GET':
        try:
            token = request.headers['Authorization']
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
                "std": user.std,
                "date_joined": user.date_joined
            }, safe=False)
        except:
            return JsonResponse( {"error": "Invalid or missing token"}, safe=False )

# Getting Account of student by student id.

@csrf_exempt
def user_account(request):
    if request.method == 'GET':
        try:
            token = request.headers['Authorization']
            user = Token.objects.get(key=token).user
            
            user_account = UserAccount.objects.filter(user=user.id)
            user_account_serializer = UserAccountSerializer(user_account, many=True)
            
            return JsonResponse(user_account_serializer.data, safe=False)
        except:
            return JsonResponse({'error': 'no authorization token or invalid token'}, safe=False)

    
# Getting Account of student by student id.
@csrf_exempt
def get_notes( request, subject, s_class ):
    # print(f"subject{subject} {s_class}")
    if request.method == 'GET':
        try:
            notes = Notes.objects.filter(subject_name=subject, subject_class=s_class)
            notes_serializer = NotesSerializer(notes, many=True)
            
            return JsonResponse(notes_serializer.data, safe=False)
        except:
            return JsonResponse({'error': 'No data found'}, safe=False)
       

# View for homepage

def homepage( request ):
    return render( request, 'index.html' )