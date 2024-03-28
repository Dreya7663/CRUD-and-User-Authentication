# Generated by Django 5.0.1 on 2024-03-28 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('USN', models.CharField(max_length=50)),
                ('Program', models.CharField(max_length=50)),
                ('Course_code', models.CharField(max_length=15)),
                ('To_do', models.CharField(max_length=100)),
                ('Deadline', models.CharField(max_length=50)),
                ('Status', models.CharField(max_length=50)),
            ],
        ),
    ]