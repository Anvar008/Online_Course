# Generated by Django 5.1.2 on 2024-12-02 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog_image/')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('author_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.register')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.category')),
            ],
        ),
    ]
