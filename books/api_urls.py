from rest_framework_extensions.routers import ExtendedSimpleRouter

from books.api.views import BookViewSet, AuthorViewSet

router = ExtendedSimpleRouter()

router.register('books', BookViewSet)
(router.register('authors', AuthorViewSet, base_name='authors')
       .register('books', BookViewSet,  parents_query_lookups=['authors'], base_name='authors-books'))

urlpatterns = router.urls
