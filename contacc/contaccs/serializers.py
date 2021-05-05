from .models import Contact
from rest_framework import serializers
from .phonenumber_serializer import CustomPhoneNumberField

class ContactSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)    
    name = serializers.CharField()
    lastname = serializers.CharField()
    company = serializers.CharField()
    phone_number = CustomPhoneNumberField()
    email = serializers.EmailField()
    
    def create(self, validated_data):
        return Contact.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.company = validated_data.get('company', instance.created)
        instance.phone_number = validated_data.get('phone_number', instance.company)
        instance.email = validated_data.get('email', instance.phone_number)
        instance.save()
        return instance
