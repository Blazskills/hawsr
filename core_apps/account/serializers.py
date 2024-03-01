
from rest_framework import serializers
from core_apps.account.models import USER_TYPE, User
from core_apps.hawsr.models import WORKER_TYPE
from django.contrib.auth import get_user_model


class UserCreateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=25)
    password = serializers.CharField(min_length=7, max_length=12)
    email = serializers.EmailField()
    role = serializers.ChoiceField(choices=USER_TYPE.choices, required=False)
    worker_type = serializers.ChoiceField(choices=WORKER_TYPE.choices, required=False)

    def validate_email(self, value):
        if User.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def validate_phone(self, value):
        if User.objects.filter(phone=value).exists():
            raise serializers.ValidationError("A user with this phone number already exists.")
        return value


class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'password']
        read_only_fields = ['role']

    def validate_email(self, value):
        if User.objects.filter(email=value.lower()).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            instance.set_password(password)
        return super().update(instance, validated_data)


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='get_role_display', read_only=True)
    worker_type = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'role', 'worker_type']

    def get_worker_type(self, obj):
        if hasattr(obj, 'worker'):
            return obj.worker.get_worker_type_display()
        return None