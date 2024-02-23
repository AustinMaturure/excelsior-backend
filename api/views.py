from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from excelsior.models import Articles
from .serializers import ArticleSerializer
from excelsior.models import Category
from .serializers import CategorySerializer

# Create your views here.


@api_view(['GET'])
def getData(request):
    articles = Articles.objects.all().prefetch_related('images', 'author', 'category')
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCategoryData(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def increment_views(request, article_id):
    try:
        article = Articles.objects.get(pk=article_id)
        article.views += 1
        article.save()
        return Response({'message': 'View count updated successfully.'})
    except Articles.DoesNotExist:
        return Response({'error': 'Article not found.'}, status=404)
