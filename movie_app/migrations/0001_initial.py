# Generated by Django 4.2.6 on 2023-11-01 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('director', models.CharField(max_length=255)),
                ('release_year', models.IntegerField()),
                ('photo', models.ImageField(upload_to='movie_photos/')),
                ('plot', models.TextField()),
                ('viewing_date', models.DateField()),
                ('rating', models.FloatField()),
            ],
        ),
    ]