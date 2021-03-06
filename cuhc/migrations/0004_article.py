# Generated by Django 3.2.5 on 2021-08-30 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuhc', '0003_etudiant'),
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uploded_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
