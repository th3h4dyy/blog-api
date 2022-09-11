from rest_framework.routers import SimpleRouter

from .views import PostViewSet, UserViewSet

app_name = "posts"

router = SimpleRouter()
router.register("users", viewset=UserViewSet, basename="users")
router.register("", viewset=PostViewSet, basename="posts")

urlpatterns = router.urls
