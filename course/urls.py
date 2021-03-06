from django.urls import path
from . import views

urlpatterns = [
    path('course_create/', views.course_create, name='course_create'),
    path('courseitem_create/', views.courseitem_create, name='courseitem_create'),
    path('course_list/', views.course_list, name='course_list'),
    path('course_detail/<int:id>', views.course_detail, name='course_detail'),
    path('course_delete/<int:id>', views.course_delete, name='course_delete'),
    path('review_create/<int:id>', views.review_create, name='review_create'),
    # path('review_update/<int:id>', views.review_update, name='review_update'),
    path('review_delete/<int:id>', views.review_delete, name='review_delete'),
]
