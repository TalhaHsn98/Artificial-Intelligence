# Generated by Django 2.2.4 on 2019-09-02 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cosmoresults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cosmonaut', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.CosmoUser')),
                ('trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.CosmoTrainerdata')),
            ],
        ),
        migrations.CreateModel(
            name='CosmoFinalReports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cosmonaut', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.CosmoUser')),
            ],
        ),
        migrations.CreateModel(
            name='CosmoFinalReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cosmonaut', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.CosmoUser')),
            ],
        ),
    ]
