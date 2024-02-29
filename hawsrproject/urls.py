from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path(
        "api/v1/",
        include(
            [
                path("account/", include("core_apps.account.urls")),

            ]
        ),
    ),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Hawsr API Admin"

admin.site.site_title = "Hawsr Hawsr API Admin Portal"

admin.site.index_title = "Welcome to Hawsr API Portal"
