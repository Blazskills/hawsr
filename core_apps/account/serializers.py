
from rest_framework import serializers
from core_apps.account.models import USER_TYPE, User


class UserCreateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=25)
    email = serializers.EmailField()
    role = serializers.ChoiceField(
        required=True,
        choices=USER_TYPE.choices,
    )

    def validate_email(self, value):
        if User.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value
