# Generated by Django 2.1rc1 on 2018-07-24 14:06

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('subject_theory', models.FloatField(blank=True, null=True, verbose_name='Theory')),
                ('subject_mcq', models.FloatField(blank=True, null=True, verbose_name='MCQ')),
                ('subject_practical', models.FloatField(blank=True, null=True, verbose_name='Practical')),
                ('subject_total_marks', models.FloatField(blank=True, null=True, verbose_name='Total Marks')),
                ('subject_gpa_sub', models.CharField(blank=True, help_text='Please keep blank', max_length=5, null=True, verbose_name='Subject GPA Sub')),
                ('subject_marks', models.DecimalField(blank=True, decimal_places=2, help_text='Please give proper number', max_digits=5, null=True)),
                ('subject_gradepoint', models.DecimalField(blank=True, decimal_places=1, help_text='Please keep blank', max_digits=3, null=True, verbose_name='Grade Point')),
                ('subject_gpa', models.CharField(blank=True, help_text='Please keep blank', max_length=5, null=True, verbose_name='Subject GPA')),
            ],
            options={
                'verbose_name': 'Mark Details',
                'verbose_name_plural': 'Result Sheet Details',
                'ordering': ['subject_name'],
            },
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_marks', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Please give proper number', max_digits=5, null=True)),
                ('total_gpa', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Please give proper number', max_digits=5, null=True)),
                ('class_rank', models.IntegerField(blank=True, default=0, null=True)),
                ('school_rank', models.IntegerField(blank=True, default=0, null=True, verbose_name='All School Rank')),
            ],
            options={
                'verbose_name': 'Rank',
                'verbose_name_plural': 'Rank',
                'ordering': ['class_rank'],
            },
        ),
        migrations.CreateModel(
            name='StdSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('subject_name', models.CharField(max_length=100, verbose_name='Subject Name')),
                ('subject_group', models.CharField(choices=[('S', 'Science'), ('B', 'Business Studies'), ('H', 'Humatics'), ('G', 'General')], default='G', max_length=10, verbose_name='Subject Group')),
                ('subject_code', models.CharField(max_length=10, verbose_name='Subject Code')),
                ('subjet_class', models.CharField(choices=[('6', 'Six'), ('7', 'Seven'), ('8', 'Eight'), ('9', 'Nine'), ('10', 'Ten')], default='6', max_length=2, verbose_name='Subject Class')),
                ('subject_type', models.CharField(choices=[('R', 'REGULAR'), ('O', 'OPTIONAL')], default='R', max_length=1, verbose_name='Subject Type')),
                ('subject_full_marks', models.DecimalField(blank=True, decimal_places=2, default=100, max_digits=5, null=True, verbose_name='Full Marks')),
                ('subject_theory_full_marks', models.FloatField(blank=True, null=True, verbose_name='Theory Marks')),
                ('subject_mcq_full_marks', models.FloatField(blank=True, null=True, verbose_name='MCQ')),
                ('subject_practical_marks', models.FloatField(blank=True, null=True, verbose_name='Practical')),
                ('subject_total_marks', models.FloatField(blank=True, help_text='Plz dont input any number', null=True, verbose_name='Total Marks')),
                ('subject_form_searh_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Subject Search Form name')),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subject',
                'ordering': ['subject_code'],
            },
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('std_name', models.CharField(blank=True, help_text='Type only student Full Name like as Nazmul Islam or Nazrul Islam', max_length=100, null=True, verbose_name='Student Name')),
                ('std_class', models.CharField(choices=[('6', 'Six'), ('7', 'Seven'), ('8', 'Eight'), ('9', 'Nine'), ('10', 'Ten')], default=6, help_text='Select a class', max_length=2, verbose_name='Student Class')),
                ('std_roll', models.IntegerField(help_text='Type Student Roll Number (Only Number)', verbose_name='Roll Number')),
                ('std_group', models.CharField(choices=[('S', 'Science'), ('B', 'Business Studies'), ('H', 'Humatics'), ('G', 'General')], default='G', max_length=1, verbose_name='Group')),
                ('std_gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='MALE', max_length=10, verbose_name='Gender')),
                ('std_total_marks', models.FloatField(blank=True, default=0, null=True, verbose_name='Total Marks')),
                ('std_gpa', models.CharField(blank=True, default='F', max_length=50, null=True, verbose_name='GPA')),
                ('std_grade_point_total_sum', models.FloatField(blank=True, null=True, verbose_name='Total Avg Number per Subject')),
                ('std_grade_point_total_subject_avg', models.FloatField(blank=True, null=True, verbose_name='Total GPA')),
                ('std_fail_subject', models.IntegerField(blank=True, null=True, verbose_name='Fail Subject')),
                ('school_rank', models.IntegerField(blank=True, default=0, null=True, verbose_name='Student Rank in School')),
                ('class_rank', models.IntegerField(blank=True, default=0, null=True, verbose_name='Student Rank in Class')),
            ],
            options={
                'verbose_name': 'Student Detail',
                'verbose_name_plural': "Student Detail's",
                'ordering': ['std_roll'],
            },
        ),
        migrations.CreateModel(
            name='SubjectTecher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('teacher_name', models.CharField(max_length=100, verbose_name='Teacher Name')),
                ('teach_phone_number', models.IntegerField(verbose_name='Mobile Number')),
                ('teach_major_subject', models.CharField(max_length=100, verbose_name='Subject Name: ')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='stdsubject',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='results.SubjectTecher'),
        ),
        migrations.AddField(
            model_name='rank',
            name='std',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='std', to='results.StudentInfo'),
        ),
        migrations.AddField(
            model_name='marks',
            name='std_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.StudentInfo'),
        ),
        migrations.AddField(
            model_name='marks',
            name='subject_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.StdSubject'),
        ),
    ]