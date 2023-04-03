from django.contrib import admin
from django.urls import path
from posts.views import *

urlpatterns = [
    path('', MainPage.as_view()),
    path('filter/', Filter.as_view(), name='filter'),
    path('category/<category>/', CategoryPage.as_view(), name='category_list'),
    path('<int:post_id>/', NewsPage.as_view(), name="post_show"),
    path('admin/', admin.site.urls),
]
