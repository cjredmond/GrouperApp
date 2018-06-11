# Generated by Django 2.0.5 on 2018-06-07 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0002_auto_20180607_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('headline', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField()),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.Entity')),
            ],
        ),
    ]