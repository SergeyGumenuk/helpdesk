# Generated by Django 4.1.5 on 2023-01-24 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='tickets.ticket')),
                ('user', models.ForeignKey(default='Deleted user', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='answers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]