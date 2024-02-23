from rest_framework import serializers
from excelsior.models import Articles, Images, Category, Staff


class CategorySerializer(serializers.ModelSerializer):
    parent_category = serializers.StringRelatedField(
        source='parent', read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    shortened_body = serializers.SerializerMethodField()
    images = ImageSerializer(many=True)
    category = CategorySerializer()
    parent_category = serializers.CharField(
        source='category.parent_category', read_only=True)
    author = StaffSerializer()

    class Meta:
        model = Articles
        fields = '__all__'

    def get_shortened_body(self, obj):
        return obj.snippet()

