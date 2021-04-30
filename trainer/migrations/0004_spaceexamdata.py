# Generated by Django 2.2.4 on 2019-09-06 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
        ('trainer', '0003_examdata_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='spaceexamdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=40, null=True)),
                ('answer1', models.CharField(max_length=40)),
                ('answer2', models.CharField(max_length=40)),
                ('answer3', models.CharField(max_length=40)),
                ('answer4', models.CharField(max_length=40)),
                ('answer5', models.CharField(max_length=40)),
                ('answer6', models.CharField(max_length=40)),
                ('answer7', models.CharField(max_length=40)),
                ('answer8', models.CharField(max_length=40)),
                ('answer9', models.CharField(max_length=40)),
                ('answer10', models.CharField(max_length=40)),
                ('cosmonaut', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.CosmoUser')),
                ('trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.CosmoTrainerdata')),
            ],
        ),
    ]
