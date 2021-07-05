# Generated by Django 3.2.3 on 2021-06-29 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('detail', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(max_length=25)),
                ('category', models.CharField(max_length=10)),
                ('image', models.ImageField(default='article/default.jpg', upload_to='articles')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]