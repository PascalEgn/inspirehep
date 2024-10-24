from backoffice.workflows.api.views import WorkflowDocumentView
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter() if settings.DEBUG else SimpleRouter()


# Workflow
router.register("workflows/search", WorkflowDocumentView, basename="workflow")

app_name = "search"
urlpatterns = router.urls
