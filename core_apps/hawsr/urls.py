from django.urls import path
from . import views

urlpatterns = [
    # Company Urls
    path('company/new/', views.CompanyCreateAPIView.as_view(), name='company_new'),
    path('company/list/', views.CompanyListAPIView.as_view(), name='company_list'),
    path('company/update/<uuid:pk>/', views.CompanyUpdateAPIView.as_view(), name='company_update'),
    path('company/delete/<uuid:pk>/', views.CompanyDeleteAPIView.as_view(), name='company_delete'),

    # Building urls
    path('building/new/', views.BuildingCreateAPIView.as_view(), name='building_new'),
    path('building/list/', views.BuildingListView.as_view(), name='building_list'),
    path('building/update/<uuid:pk>/', views.BuildingUpdateView.as_view(), name='building_update'),
    path('building/delete/<uuid:pk>/', views.BuildingDeleteView.as_view(), name='building_delete'),


    # Office Urls
    path('office/new/', views.OfficeCreateAPIView.as_view(), name='office_new'),
    path('office/list/', views.OfficeListView.as_view(), name='office_list'),
    path('office/update/<uuid:pk>/', views.OfficeUpdateView.as_view(), name='office_update'),
    path('office/delete/<uuid:pk>/', views.OfficeDeleteView.as_view(), name='office_delete'),

    path('assign/office/user/', views.AssignUserToOfficeView.as_view(), name='assign_User_to_office'),

]
