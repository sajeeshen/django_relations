# Generated by Django 3.0 on 2019-12-13 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.Place')),
                ('name', models.CharField(max_length=50)),
                ('food_choices', models.CharField(choices=[('Fast Food', 'Fast Food'), ('Bar Attached', 'Bar Attached'), ('Bakery', 'Bakery'), ('Normal', 'Normal')], default='Normal', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
