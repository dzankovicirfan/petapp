# Generated by Django 2.0.1 on 2018-01-25 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('birthday', models.DateField(verbose_name='Birthday')),
                ('pet_type', models.IntegerField(choices=[(1, 'Dog'), (2, 'Cat')])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'pet',
                'verbose_name_plural': 'pets',
            },
        ),
    ]