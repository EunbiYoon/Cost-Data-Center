from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('report/', include('report.urls')),
    path('accounts/', include('member.urls')),
    path('quality/', include('quality.urls')),
]
