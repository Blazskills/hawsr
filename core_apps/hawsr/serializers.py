
from rest_framework import serializers
from core_apps.account.models import USER_TYPE, User
from core_apps.hawsr.models import WORKER_TYPE, Building, Company, Office
from django.contrib.auth import get_user_model


class CompanySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'phone']


class BuildingListSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    company = serializers.CharField(source="company.name", read_only=True)

    class Meta:
        model = Building
        fields = ['id', 'company', 'name', 'floor_count']


class BuildingSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Building
        fields = ['id', 'company', 'name', 'floor_count']
        extra_kwargs = {
            'company': {'required': True},
            'name': {'required': True, 'allow_blank': False},
        }

    def validate_company(self, value):
        if not Company.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Company with this ID does not exist.")
        return value

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        return value



class OfficeListSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    building = serializers.CharField(source="building.name", read_only=True)

    class Meta:
        model = Office
        fields = ['id', 'building', 'floor', 'number']


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ['building', 'floor', 'number']
        extra_kwargs = {
            'building': {'required': True},
        }

    def validate_building(self, value):
        if not Building.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Building with this ID does not exist.")
        return value




class AssignUserOfficeSerializer(serializers.Serializer):
    user_id = serializers.UUIDField()
    office_id = serializers.UUIDField()

    def validate_user_id(self, value):
        if not User.objects.filter(id=value).exists():
            raise serializers.ValidationError("User with this ID does not exist.")
        return value

    def validate_office_id(self, value):
        if not Office.objects.filter(id=value).exists():
            raise serializers.ValidationError("Office with this ID does not exist.")
        return value
