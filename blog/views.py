from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Article, Category
from .serializers import ArticleSerializer, CategorySerializer

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all().order_by('-published_at')
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.request.query_params.get('category', None)
        search_query = self.request.query_params.get('search', None)
        featured = self.request.query_params.get('featured', None)

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        
        if search_query:
            queryset = queryset.filter(title__icontains=search_query) | \
                       queryset.filter(excerpt__icontains=search_query) | \
                       queryset.filter(tags__icontains=search_query)

        if featured == 'true':
            queryset = queryset.filter(featured=True)

        return queryset

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
