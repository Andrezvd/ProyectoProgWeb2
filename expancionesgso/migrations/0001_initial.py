# Generated by Django 4.2.1 on 2023-07-14 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=300)),
                ('precio', models.IntegerField()),
                ('imagen', models.FileField(upload_to='expanciones/')),
            ],
        ),
    ]
