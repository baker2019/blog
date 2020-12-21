from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    STATUS = (
        ('True','True'),
        ('False','False'),
    )
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

    def image_tag(self):
        return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    class meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class House(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    ANSWER = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
   # user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=255)
    keywords = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True, max_length=1000)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(blank=True, upload_to='images/')
    price1 = models.IntegerField(blank=True)
    price2 = models.IntegerField(blank=True)
    basic_amenity = models.TextField(null=True)
    facilities = models.TextField(null=True)
    dinning_amenity = models.TextField(null=True)
    bed_and_bath_amenity = models.TextField(null=True)
    guest_access = models.TextField(null=True)
    status = models.CharField(blank=True, max_length=10, choices=STATUS)
    create_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, auto_now=True)
    number_of_bedrooms = models.IntegerField(blank=True, )
    location = models.CharField(blank=True, max_length=255)
    number_of_Beds = models.IntegerField(blank=True, )
    number_of_bathrooms = models.IntegerField(blank=True, )
    max_guest = models.IntegerField(blank=True, )
    pets = models.CharField(blank=True, max_length=10, choices=ANSWER)
    smoking = models.CharField(blank=True, max_length=10, choices=ANSWER)
    withintheSite = models.CharField(blank=True, max_length=10, choices=STATUS)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('house_detail', kwargs={'slug': self.slug})


class Images(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50" />'.format(self.image.url))
    image_tag.short_description = 'Image'


class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False')
    )
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(blank=True, max_length=50)
    comment = models.CharField(blank=True, max_length=255)
    status = models.CharField(blank=True, max_length=10, choices=STATUS)
    create_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, auto_now=True)

    def __str__(self):
        return self.subject


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment']
