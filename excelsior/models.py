from django.db import models
from django.utils.text import slugify


class Staff(models.Model):
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField(
        upload_to="staff_images")  # Adjust the upload_to path
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, default="Top")
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    description = models.TextField(
        blank=True, null=True)  # Add a description field
    image = models.ImageField(
        upload_to='category_images',  blank=True, null=True)  # Image file

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()  # Changed to TextField for article content
    date = models.DateField(auto_now_add=True)
    # Ensure slugs are unique
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(
        Staff, related_name="author", on_delete=models.CASCADE)
    # Adjust the upload_to path
    thumbnail = models.ImageField(upload_to='article_thumbnails')
    category = models.ForeignKey(
        Category, related_name="category", on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def increment_views(self):
        self.views += 1
        self.save()

    def snippet(self):
        return self.body[:290] + '...'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Images(models.Model):
    # Article to which the image is related
    article = models.ForeignKey(
        Articles, related_name="images", on_delete=models.CASCADE)
    description = models.CharField(max_length=100)  # Description of the image
    image = models.ImageField(
        upload_to='article_images_additional')  # Image file

    def __str__(self):
        return self.description  # Return the image's description as a string

