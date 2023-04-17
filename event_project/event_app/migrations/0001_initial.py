# Generated by Django 4.2 on 2023-04-13 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('venue', models.CharField()),
                ('starts_at', models.DateTimeField()),
                ('ends_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_registered', models.BooleanField(default=False)),
                ('event_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_app.events')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
    ]
