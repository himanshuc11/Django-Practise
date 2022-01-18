from django.urls import path, include
from .views import r2

urlpatterns = [
    path('age/', r2),
]

# Make an app of own name
# himanshu/age => Age
# himanshu/fullname => Fullname
# himanshu/birthday => Birthday 
# himanshu/favorite/color => Favorite color
# himanshu/favorite/food => Favorite food