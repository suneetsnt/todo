from django.urls import path
from . import views 

urlpatterns= [
    path('',views.index,name="list"),
    path('update_task/<str:pk>/',views.updateTask,name="update_task"),
    path('delete_task/<str:pk>/',views.deleteTask,name="delete_task"),
    path('login',views.userLogin,name="login"),
    path('register',views.userRegister,name="register"),
    path('items',views.viewItems,name="items"),
    path('itemDetail/<str:pk>/',views.viewItemInfo,name="itemInfo"),
    path('mycart',views.userCart,name="user_cart"),
]