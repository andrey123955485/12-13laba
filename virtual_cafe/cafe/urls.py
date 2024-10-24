from django.urls import path
from .views import home, login_view, register_view, order_coffee, drink_coffee, enter_cafe, exit_cafe

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('order-coffee/', order_coffee, name='order_coffee'),
    path('drink-coffee/', drink_coffee, name='drink_coffee'),
    path('enter-cafe/', enter_cafe, name='enter_cafe'),
    path('exit-cafe/', exit_cafe, name='exit_cafe'),
]
