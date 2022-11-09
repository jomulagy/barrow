# Generated by Django 4.1.3 on 2022-11-09 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('area', models.CharField(default='', max_length=100, verbose_name='거래 장소')),
                ('type', models.CharField(choices=[('01', '직거래만'), ('10', '택배거래만'), ('11', '택배/직거래')], max_length=2)),
                ('price', models.IntegerField()),
                ('price_per', models.CharField(choices=[('PER_DAY', 'DAY'), ('PER_WEEK', 'WEEK'), ('PER_MONTH', 'MONTH')], max_length=20)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('category', models.CharField(choices=[('CLOTHES', '의류'), ('SHOES', '신발'), ('TRAVELS', '여행용품'), ('BAGS', '가방'), ('CARRIERS', '캐리어'), ('SPORTS', '스포츠'), ('LEISURES', '레저'), ('HOMES', '가전제품'), ('FURNITURES', '가구'), ('ELECTROMICS', '전자제품'), ('CASUALS', '캐주얼'), ('OTHERS', '기타')], max_length=20)),
                ('memo', models.TextField(default='', max_length=200, null=True)),
                ('views', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('productor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='static/img/product_default.png', null=True, upload_to='product')),
                ('index', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='_product.product')),
            ],
        ),
    ]
