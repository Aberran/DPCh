# Generated by Django 4.2.7 on 2024-01-11 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_user_cur_proj_user_cur_proj_desc_user_cur_proj_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='cur_proj_desc',
            new_name='cur_project_desc',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='cur_proj',
            new_name='cur_project_link',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='cur_proj_name',
            new_name='cur_project_name',
        ),
    ]