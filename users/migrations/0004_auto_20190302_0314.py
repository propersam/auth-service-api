# Generated by Django 2.1.5 on 2019-03-02 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190301_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pics',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/%Y/%m/%d', verbose_name="Upload User's Profile Picture"),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='logo',
            field=models.ImageField(null=True, upload_to='logos', verbose_name='Upload Organisation Logo'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='size',
            field=models.IntegerField(choices=[(1, '1 to 10'), (2, '11 to 50'), (3, '50 and Above')], verbose_name='Organisation Size'),
        ),
    ]
