from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="Home"),
    path('update/<int:id>',views.update,name='updateName'),
    path('delete/<int:id>',views.deletefunc2,name="Del_btn"),
    path('add_blog',views.addb,name="Add")
]
