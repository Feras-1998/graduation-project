# Generated by Django 3.1.6 on 2021-02-06 22:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ManageReview', '0001_initial'),
        ('ManageProduct', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ManageStore', '0001_initial'),
        ('ShoppingCart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreAdminProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(default='Customer default.png', upload_to='StoreAdminProfileImages')),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('join_at', models.DateTimeField(default=datetime.datetime.now)),
                ('country', django_countries.fields.CountryField(default='Jordan', max_length=2)),
                ('store', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ManageStore.store')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Store Admin Profile',
            },
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(default='Customer default.png', upload_to='CustomerProfileImages')),
                ('address', models.CharField(max_length=100)),
                ('join_at', models.DateTimeField(default=datetime.datetime.now)),
                ('country', django_countries.fields.CountryField(default='Jordan', max_length=2)),
                ('cart', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ShoppingCart.shoppingcart')),
                ('favorite', models.ManyToManyField(blank=True, to='ManageProduct.Product')),
                ('review', models.ManyToManyField(blank=True, to='ManageReview.Review')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Customer Profile',
            },
        ),
    ]
