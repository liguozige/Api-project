# Generated by Django 2.2 on 2022-08-02 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DB_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user_id', models.IntegerField(default=0)),
                ('to_user_id', models.IntegerField(default=0)),
                ('content', models.CharField(blank=True, default='-', max_length=500, null=True)),
            ],
        ),
    ]
