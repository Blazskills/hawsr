from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate

from core_apps.account.forms import User
from core_apps.account.serializers import UserCreateSerializer
from core_apps.account.tokens import create_jwt_pair_for_user


from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import AuthenticationFailed

from rest_framework.decorators import APIView
from rest_framework.response import Response


from rest_framework import permissions, status

from utils.decorators import DisallowedNotAdminManagementPermission, DisallowedUserPermission


# Create your views here.

class testaccount(APIView):
    authentication_classes = []

    def get(self, request):
        data = {
            "status": "Account okay",
            "code": 200,
        }
        return Response(data)


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


class CreateUserView(APIView):
    permission_classes = [permissions.IsAuthenticated, DisallowedUserPermission, DisallowedNotAdminManagementPermission]

    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                data = serializer.validated_data
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


class UpdateUserView(APIView):
    pass


class DeleteUserView(APIView):
    pass


class UserProfileView(APIView):
    pass
