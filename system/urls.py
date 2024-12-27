from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cost/accounts/', include('user.urls')),
    path('cost/', include('CostData.cost_base.urls')),
    path('cost/report/', include('CostData.report.urls')),
    path('quality/', include('CostData.quality.urls')),
]
