# Generated by Django 5.0.2 on 2024-02-28 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book_DB',
            fields=[
                ('bookno', models.IntegerField(primary_key='bookno', serialize=False)),
                ('bookname', models.CharField(max_length=20)),
                ('authorname', models.CharField(max_length=20)),
                ('year', models.DateField()),
                ('price', models.IntegerField()),
                ('pages', models.IntegerField()),
            ],
        ),
    ]