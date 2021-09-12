# Generated by Django 3.2.6 on 2021-09-08 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_question_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='is_ans_option_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_reference', to='Task.quiz'),
        ),
    ]