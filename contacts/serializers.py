from django.db.models.fields import Field
from rest_framework import serializers
from .models import Contact

class ContactListSerializer(serializers.ModelSerializer):

    class Meta:
        model=Contact
        fields = ['id', 'country_code', 'first_name','last_name','phone_number','contact_pic','is_favorite']

    def validate(self, attrs):
        phone_number = attrs.get('phone_number', '')
        if Contact.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError({'phone_number':'phone_number is already saved'})

        return super().validate(attrs)

