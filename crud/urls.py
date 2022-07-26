from django.urls import path

from .views import*
 
# define here urls

urlpatterns = [
    path('',employee_view),
    path("add/", employee_create, name="add"),
    path('update/<int:eid>/',employee_update,name='update'),
    path("delete/<int:eid>/", employee_delete, name="delete"),
    path("showview/<int:eid>/", employee_show, name="show"),
]

