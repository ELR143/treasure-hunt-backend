# Generated by Django 5.0.1 on 2024-01-02 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasure_hunt_backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treasure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='treasures',
            field=models.ManyToManyField(blank=True, related_name='owners', to='treasure_hunt_backend.treasure'),
        ),
    ]