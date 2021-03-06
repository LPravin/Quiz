# Generated by Django 3.2.6 on 2021-09-08 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0003_auto_20210908_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerEntries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whether_answered_right', models.BooleanField()),
                ('ques_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ques_reference', to='Task.question')),
                ('user_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reference', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
