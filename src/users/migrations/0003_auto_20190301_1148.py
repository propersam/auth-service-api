# Generated by Django 2.1.5 on 2019-03-01 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190227_1351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organisation',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='organisation',
            name='about_company',
            field=models.TextField(blank=True, null=True, verbose_name='Short Description About Company'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='website',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='website of the Company'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contact_num',
            field=models.CharField(blank=True, max_length=17, null=True, unique=True, verbose_name="User's phone number"),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Role name'),
        ),
    ]
