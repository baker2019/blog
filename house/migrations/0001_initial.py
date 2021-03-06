# Generated by Django 3.1.4 on 2020-12-21 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('slug', models.SlugField(unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='house.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('keywords', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('price1', models.IntegerField(blank=True)),
                ('price2', models.IntegerField(blank=True)),
                ('basic_amenity', models.TextField(null=True)),
                ('facilities', models.TextField(null=True)),
                ('dinning_amenity', models.TextField(null=True)),
                ('bed_and_bath_amenity', models.TextField(null=True)),
                ('guest_access', models.TextField(null=True)),
                ('status', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('number_of_bedrooms', models.IntegerField(blank=True)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('number_of_Beds', models.IntegerField(blank=True)),
                ('number_of_bathrooms', models.IntegerField(blank=True)),
                ('max_guest', models.IntegerField(blank=True)),
                ('pets', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('smoking', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('withintheSite', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.category')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.house')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('comment', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(blank=True, choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.house')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
