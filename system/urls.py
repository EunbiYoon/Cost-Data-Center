from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cost/', include('cost_base.urls')),
    path('cost/report/', include('report.urls')),
    path('cost/accounts/', include('member.urls')),
    path('quality/', include('quality.urls')),
]
