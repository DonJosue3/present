# Generated by Django 5.0.4 on 2024-04-06 14:46

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=31)),
                ('prenom', models.CharField(max_length=31)),
                ('salaire', models.IntegerField()),
                ('date_adhesion', models.DateField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('salaire', models.IntegerField()),
                ('present', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('personne', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='urusoro.personne')),
            ],
        ),
    ]
