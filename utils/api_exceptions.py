from rest_framework import status
from rest_framework.exceptions import APIException


class UserNotActiveException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = {"status": "error",
                      "message": "User account is not verified"}
    default_code = "101"


class UserPermissionDenied(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = {
        "status": "error",
        "message": "You do not have permission to perform this action.",
    }
    default_code = "403"


class LoginRequiredException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = {
        "status": "error",
        "message": "Login is required to access this view",
    }
    default_code = "102"


class InactiveUserException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = {"status": "error", "message": "Account Not active"}
    default_code = "101"


class AlreadyLoginUserException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = {"status": "error",
                      "message": "You are logged in already"}
    default_code = "403"



class NotAdminException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = {"status": "error",
                      "message": "You Must Be An Admin To Perform User CRUD"}
    default_code = "101"


class NotFoundUserException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = {"status": "error", "message": "User Not Found"}
    default_code = "101"


class InvalidTokenException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = {"status": "error", "message": "Invalid token"}
    default_code = "101"


class InvalidSignatureException(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = {"status": "error", "message": "Invalid signature"}
    default_code = "101"
