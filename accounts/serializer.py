from rest_framework import serializers
from .models import News, UserAccount, Notes, Contact

from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'password', 'email', 'address', 'school_name', 'std']
        

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class NotesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'subject_name', 'subject_class', 'pdf_file']
        
class UserAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAccount
        # fields = '__all__'
        fields = ['id', 'fee_rate', 'total_amount', 'due_months', 'is_submitted']

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'