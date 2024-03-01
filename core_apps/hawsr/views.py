from django.shortcuts import render
from core_apps.account.forms import User
from core_apps.hawsr.models import Office, UserOffice
from core_apps.hawsr.serializers import AssignUserOfficeSerializer, BuildingListSerializer, BuildingSerializer, CompanySerializer, OfficeListSerializer, OfficeSerializer
from utils.decorators import DisallowedNotAdminManagementPermission, DisallowedUserPermission
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework import generics, permissions
from .models import Company, Building, Office
# Create your views here.

# /*INFO: Company Module Start Here*/

# Create company data


class CompanyCreateAPIView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated, DisallowedUserPermission, DisallowedNotAdminManagementPermission]

# TODO:PENDING

# All Company Created


class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated, DisallowedUserPermission, DisallowedNotAdminManagementPermission]


# Update company data
class CompanyUpdateAPIView(generics.UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated, DisallowedUserPermission, DisallowedNotAdminManagementPermission]


# Delete a company

class CompanyDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, DisallowedUserPermission, DisallowedNotAdminManagementPermission]
    queryset = Company.objects.all()

    def delete(self, request, *args, **kwargs):
        company = self.get_object()
        company.delete()
        return Response({"status": "success", "message": "Company deleted successfully."}, status=status.HTTP_200_OK)


# Building Module Start Here
class BuildingCreateAPIView(generics.CreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [permissions.IsAuthenticated, DisallowedUserPermission, DisallowedNotAdminManagementPermission]


class BuildingListView(generics.ListAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingListSerializer
    permission_classes = [permissions.IsAuthenticated, DisallowedUserPermission, DisallowedNotAdminManagementPermission]


class BuildingUpdateView(generics.UpdateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [permissions.IsAuthenticated, DisallowedUserPermission, DisallowedNotAdminManagementPermission]


class BuildingDeleteView(generics.DestroyAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [permissions.IsAuthenticated, DisallowedUserPermission, DisallowedNotAdminManagementPermission]


class OfficeCreateAPIView(generics.CreateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = [permissions.IsAuthenticated, DisallowedUserPermission, DisallowedNotAdminManagementPermission]


class OfficeListView(generics.ListAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeListSerializer
    permission_classes = [permissions.IsAuthenticated, DisallowedUserPermission, DisallowedNotAdminManagementPermission]


class OfficeUpdateView(generics.UpdateAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = [permissions.IsAuthenticated, DisallowedUserPermission, DisallowedNotAdminManagementPermission]


class OfficeDeleteView(generics.DestroyAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    permission_classes = [permissions.IsAuthenticated, DisallowedUserPermission, DisallowedNotAdminManagementPermission]


class AssignUserToOfficeView(APIView):
    permission_classes = [permissions.IsAuthenticated, DisallowedUserPermission, DisallowedNotAdminManagementPermission]

    def post(self, request, format=None):
        serializer = AssignUserOfficeSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(id=serializer.validated_data['user_id'])
            office = Office.objects.get(id=serializer.validated_data['office_id'])
            user_office, created = UserOffice.objects.get_or_create(user=user, office=office)
            if created:
                return Response({"status": "success", "message": "User assigned to office successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "success", "message": "User is already assigned to this office."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
