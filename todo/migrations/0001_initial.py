# Generated by Django 5.0.1 on 2024-02-13 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('priority', models.IntegerField(default=1)),
                ('is_done', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'todos',
            },
        ),
    ]
