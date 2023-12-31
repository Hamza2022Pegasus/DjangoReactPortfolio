# Generated by Django 4.2.5 on 2023-09-08 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMeSeciton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Title for About me Section')),
                ('subTitle', models.CharField(blank=True, max_length=200, null=True, verbose_name='Subtitle')),
                ('desctiprion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'About me Section Text',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(blank=True, max_length=100, null=True, verbose_name='Icon eg:fa fa-light')),
                ('info', models.CharField(blank=True, max_length=100, null=True, verbose_name='Contact Info (eg: johndoe2@gmail.com)')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Contact Name ( this whole section is flawed)')),
            ],
            options={
                'verbose_name': 'Contact Me section',
            },
        ),
        migrations.CreateModel(
            name='IntroBannerHero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welcomeText', models.CharField(blank=True, max_length=50, null=True, verbose_name='Text to welcome users')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Your Full Name')),
                ('job_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Job Title')),
                ('introPara', models.CharField(blank=True, max_length=500, null=True, verbose_name='Introduction Paragraph')),
                ('image', models.CharField(blank=True, max_length=30, null=True, verbose_name='Google Drive id only for image')),
                ('emailAddress', models.CharField(blank=True, max_length=50, null=True, verbose_name='Your personal email to recieve emails on')),
                ('linkToCV', models.CharField(blank=True, max_length=50, null=True, verbose_name='URL link for CV')),
            ],
            options={
                'verbose_name': 'Intro Banner Text',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technology', models.CharField(blank=True, max_length=50, null=True, verbose_name='Language used for this project')),
                ('image', models.CharField(blank=True, max_length=50, null=True, verbose_name='GDrive image id for logo')),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name of Project')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description of Job')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Github URL of the Project')),
                ('demo', models.URLField(blank=True, null=True, verbose_name='Demo Link of the Project')),
            ],
            options={
                'verbose_name': 'Completed jobs',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, max_length=100, null=True, verbose_name='Google drive image id')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name of offered Service')),
                ('backgroundIcon', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description for the service')),
            ],
            options={
                'verbose_name': 'Services by You',
            },
        ),
        migrations.CreateModel(
            name='SMLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.URLField(blank=True, max_length=100, null=True)),
                ('icon', models.CharField(blank=True, max_length=50, null=True, verbose_name='Icon eg: fa fa-light')),
            ],
            options={
                'verbose_name': 'Social Media Links Section',
            },
        ),
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Technology Icon Image:(icons8.com)')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name of programming language')),
                ('experience', models.CharField(blank=True, choices=[('Beginner', 'Beginner'), ('Junior', 'Junior'), ('Intermediate', 'Intermediate'), ('Experienced', 'Experienced')], max_length=100, verbose_name='Experience Level')),
            ],
            options={
                'verbose_name': 'Technologies',
            },
        ),
    ]
