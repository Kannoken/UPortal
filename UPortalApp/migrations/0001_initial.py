# Generated by Django 2.0 on 2017-12-21 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameRus', models.CharField(max_length=200)),
                ('nameEng', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Files_of_place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Files_of_publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Place_of_publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type_of_place', models.CharField(max_length=255)),
                ('publishing_house', models.CharField(max_length=255)),
                ('place_of_publish', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('list_of_links', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date_of_publication', models.DateField()),
                ('language_of_publication', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('type_of_publication', models.CharField(max_length=255)),
                ('type_of_index', models.CharField(max_length=255)),
                ('place_of_publication', models.CharField(max_length=255)),
                ('pages', models.CharField(max_length=255)),
                ('links', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='files_of_publication',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_pub', to='UPortalApp.Publication'),
        ),
        migrations.AddField(
            model_name='files_of_place',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_place', to='UPortalApp.Place_of_publication'),
        ),
    ]