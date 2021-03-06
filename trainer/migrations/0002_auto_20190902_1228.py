# Generated by Django 2.2.4 on 2019-09-02 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createexam',
            name='subjectname',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='createexam',
            name='typeofexam',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='createexam',
            name='title',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='createexam',
            name='trainername',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.CosmoTrainerdata'),
        ),
    ]
