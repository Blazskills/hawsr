from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate

from core_apps.account.forms import User
from core_apps.account.models import USER_TYPE
from core_apps.account.serializers import UserCreateSerializer, UserSerializer, UserUpdateSerializer
from core_apps.account.tokens import create_jwt_pair_for_user
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from core_apps.hawsr.models import Worker
from utils.decorators import DisallowedNotAdminManagementPermission, DisallowedUserPermission
from django.contrib.auth import password_validation
from rest_framework import generics
from django.contrib.auth import get_user_model

# Create your views here.


class testaccount(APIView):
    authentication_classes = []

    def get(self, request):
        data = {
            "status": "Account okay",
            "code": 200,
        }
        return Response(data)

# Login view to have p


class LoginView(APIView):
    authentication_classes = []

    def post(self, request,):

        def create_response(status, message, status_code):
            response = {"status": status, "message": message}
            return Response(data=response, status=status_code)

        try:
            if (
                request.data.get("email") == None
                or request.data.get("email") == ""
            ) and (
                request.data.get("password") == ""
                or request.data.get("password") == None
            ):
                return create_response(
                    "error",
                    "email and Password can not be empty",
                    status.HTTP_400_BAD_REQUEST,
                )
            check_email = None
            password = request.data.get("password")
            email = request.data.get("email").replace(" ", "")
            check_email = User.objects.get(email=email)
            if User.objects.filter(
                is_active=False, email=check_email.email
            ).first():
                return create_response(
                    "error", "User not active", status.HTTP_400_BAD_REQUEST
                )
            user = authenticate(
                email=check_email.email, password=password
            )
            if not user:
                return create_response(
                    "error",
                    "Invalid email or password",
                    status.HTTP_400_BAD_REQUEST,
                )
            tokens = create_jwt_pair_for_user(user)

            response = {
                "message": "Login successful",
                "userType": user.role,
                "token": tokens,
            }
            return Response(data=response, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return create_response(
                "error", "User Not Found", status.HTTP_400_BAD_REQUEST
            )
        except AuthenticationFailed:
            return create_response(
                "error",
                "Invalid email or  password",
                status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return create_response(
                "error",
                str(e),
                status.HTTP_400_BAD_REQUEST,
            )

# Create any type of user without authenticating


class CreateUserView(APIView):
    # permission_classes = [permissions.IsAuthenticated, DisallowedUserPermission, DisallowedNotAdminManagementPermission]

    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                data = serializer.validated_data
                user_role = data.get("role")
                worker_type = data.get("worker_type")
                if user_role == USER_TYPE.WORKER and worker_type is None:
                    return Response({"error": "Worker type cannot be null for a user who is a worker."}, status=status.HTTP_400_BAD_REQUEST)
                user_created = User(
                    email=data.get("email").lower().replace(" ", ""),
                    first_name=data.get("first_name"),
                    last_name=data.get("last_name"),
                    phone=data.get("phone"),
                    role=data.get("role"),
                    is_active=True,
                )
                user_password = data.get('password')
                password_validation.validate_password(
                    user_password, user_created
                )
                user_created.set_password(user_password)
                user_created.save()
                if user_created.role == USER_TYPE.WORKER:
                    Worker.objects.create(user=user_created, worker_type=data.get("worker_type"))
                response = {
                    "status": "success",
                    "message": "User created successfully.",
                }
                return Response(data=response, status=status.HTTP_200_OK)
            except Exception as e:
                response = {
                    "error": str(e),
                }
                return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Can only update current login user or active user


class UpdateCurrentUserView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, DisallowedUserPermission, DisallowedNotAdminManagementPermission]

    def get_object(self):
        return self.request.user

# Update any user using user ID


class UpdateAnyUserView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, DisallowedUserPermission, DisallowedNotAdminManagementPermission]

    def get_queryset(self):
        return get_user_model().objects.all()

# Delete any user using user ID


class DeleteAnyUserView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, DisallowedUserPermission, DisallowedNotAdminManagementPermission]
    queryset = get_user_model().objects.all()

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response({"status": "success", "message": "User deleted successfully."}, status=status.HTTP_200_OK)


# You can view any user, also current user can view profile
class ViewAnyUserView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, DisallowedUserPermission, DisallowedNotAdminManagementPermission]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
