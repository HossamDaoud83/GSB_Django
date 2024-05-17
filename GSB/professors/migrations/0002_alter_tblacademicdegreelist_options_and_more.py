# Generated by Django 5.0.4 on 2024-05-17 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tblacademicdegreelist',
            options={'managed': False, 'verbose_name': 'Academic_Degree', 'verbose_name_plural': 'Academic_Degrees'},
        ),
        migrations.AlterModelOptions(
            name='tblcategorylist',
            options={'managed': False, 'verbose_name': 'Category List', 'verbose_name_plural': 'Categories List'},
        ),
        migrations.AlterModelOptions(
            name='tblcitylist',
            options={'managed': False, 'verbose_name': 'City List', 'verbose_name_plural': 'Cities List'},
        ),
        migrations.AlterModelOptions(
            name='tblcontacts',
            options={'managed': False, 'verbose_name': 'Professor', 'verbose_name_plural': 'Professors Contacts'},
        ),
        migrations.AlterModelOptions(
            name='tbleducode',
            options={'managed': False, 'verbose_name': 'Education Code', 'verbose_name_plural': 'Education Codes'},
        ),
        migrations.AlterModelOptions(
            name='tblmajorlist',
            options={'managed': False, 'verbose_name': 'Major List', 'verbose_name_plural': 'Majors List'},
        ),
        migrations.AlterModelOptions(
            name='tblprogramlist',
            options={'managed': False, 'verbose_name': 'Program List', 'verbose_name_plural': 'Programs List'},
        ),
        migrations.AlterModelOptions(
            name='tblsemesterlist',
            options={'managed': False, 'verbose_name': 'Semester List', 'verbose_name_plural': 'Semesters List'},
        ),
        migrations.AlterModelOptions(
            name='tblsubjectslist',
            options={'managed': False, 'verbose_name': 'Subject List', 'verbose_name_plural': 'Subjects List'},
        ),
        migrations.AlterModelOptions(
            name='tbltimetabletypelist',
            options={'managed': False, 'verbose_name': 'Timetable Type', 'verbose_name_plural': 'Timetable Types'},
        ),
    ]