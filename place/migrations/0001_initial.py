# Generated by Django 3.2.9 on 2021-11-13 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RegionFestival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=20)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('period', models.CharField(max_length=20)),
                ('host_info', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('kakao_place_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=20)),
                ('category', models.CharField(blank=True, max_length=20)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('businessHours', models.CharField(blank=True, max_length=100)),
                ('place_type', models.IntegerField(choices=[(0, '식당'), (1, '관광지')], null=True)),
                ('region_money', models.IntegerField(choices=[(0, '불가능'), (1, '가능')], null=True)),
                ('menu', models.ManyToManyField(blank=True, related_name='menu', to='place.Menu')),
            ],
        ),
    ]
