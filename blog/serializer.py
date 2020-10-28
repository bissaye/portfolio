from .models import Messages
from rest_framework import serializers


class Email(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = [
            'subject',
            'email',
            'message',
            'name',
        ]
