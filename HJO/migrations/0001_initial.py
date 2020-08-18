# Generated by Django 3.1 on 2020-08-16 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='posts/')),
                ('title', models.CharField(blank=True, max_length=250)),
                ('tag', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(blank=True, max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('post', models.TextField(blank=True, max_length=52500)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='posts/')),
                ('title', models.CharField(blank=True, max_length=250)),
                ('name', models.CharField(blank=True, max_length=250)),
                ('testimony', models.TextField(blank=True, max_length=52500)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('name', models.CharField(blank=True, max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='HJO.blog')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
