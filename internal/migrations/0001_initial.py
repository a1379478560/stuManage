# Generated by Django 2.0.4 on 2018-05-02 02:18

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import internal.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketerInfo',
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
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=8, verbose_name='性别')),
                ('qq', models.CharField(blank=True, max_length=11, unique=True, verbose_name='QQ')),
                ('phone', models.CharField(blank=True, max_length=11, verbose_name='电话')),
                ('notice', models.CharField(blank=True, max_length=128, verbose_name='备注')),
                ('join_date', models.DateField(verbose_name='入职时间')),
                ('status', models.CharField(choices=[('signed', '在职'), ('resigned', '离职')], default='signed', max_length=32, verbose_name='状态')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '市场人员',
                'verbose_name_plural': '市场人员',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ClassList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='班次')),
                ('course_type', models.CharField(choices=[('in_school', '校内上课'), ('full_time', '全日制'), ('part_tim', '非全日制')], default='in_school', max_length=32, verbose_name='课程类型')),
                ('is_online', models.CharField(choices=[('online', '在线上课'), ('offline', '线下上课')], default='offline', max_length=32, verbose_name='上课方式')),
                ('class_hour', models.IntegerField(default=50, verbose_name='课时')),
                ('capacity', models.IntegerField(default=30, verbose_name='最大班容量')),
                ('semester', models.IntegerField(default=2, verbose_name='学期数')),
                ('start_date', models.DateField(verbose_name='开班日期')),
                ('graduate_date', models.DateField(blank=True, null=True, verbose_name='毕业日期')),
                ('notice', models.CharField(blank=True, max_length=128, verbose_name='备注')),
            ],
            options={
                'verbose_name': '开班列表',
                'verbose_name_plural': '开班列表',
            },
        ),
        migrations.CreateModel(
            name='ClassRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='上课时间')),
                ('address', models.CharField(default='海悦天地', max_length=128, verbose_name='上课地点')),
                ('which_time', models.IntegerField(default=1, verbose_name='第几次课')),
                ('duration', models.IntegerField(default=2, verbose_name='上课时长')),
                ('should_come_num', models.IntegerField(verbose_name='应到人数')),
                ('absentee', models.CharField(blank=True, max_length=128, verbose_name='缺席名单')),
                ('notice', models.CharField(blank=True, max_length=128, verbose_name='备注')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='internal.ClassList', verbose_name='班次')),
            ],
            options={
                'verbose_name': '上课记录',
                'verbose_name_plural': '上课记录',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='课程')),
                ('suit_age', models.CharField(choices=[('elementary', '小学'), ('middle', '初中'), ('high', '高中'), ('college', '大学')], default='elementary', max_length=16, verbose_name='适用阶段')),
                ('brief', models.TextField(blank=True, verbose_name='简介')),
                ('notice', models.CharField(blank=True, max_length=128, verbose_name='备注')),
            ],
            options={
                'verbose_name': '课程介绍',
                'verbose_name_plural': '课程介绍',
            },
        ),
        migrations.CreateModel(
            name='SchoolInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='学校名')),
                ('address', models.CharField(blank=True, max_length=64, verbose_name='地址')),
                ('phone', models.CharField(blank=True, max_length=11, verbose_name='电话')),
                ('notice', models.CharField(blank=True, max_length=128, verbose_name='备注')),
            ],
            options={
                'verbose_name': '学校列表',
                'verbose_name_plural': '学校列表',
            },
        ),
        migrations.CreateModel(
            name='StuInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=8, verbose_name=' 性别')),
                ('qq', models.CharField(max_length=64, null=True, unique=True, verbose_name='QQ')),
                ('parent_phone', models.CharField(blank=True, max_length=11, verbose_name='父母电话')),
                ('stu_id', internal.fields.IdField(default='000000', max_length=6, verbose_name='学号')),
                ('school', models.CharField(blank=True, max_length=128, null=True, verbose_name='学校')),
                ('source', models.CharField(choices=[('qq', 'qq群'), ('school', '学校转化'), ('ads', '广告'), ('agent', '招生代理'), ('others', '其他')], default='agent', max_length=32, verbose_name='来源')),
                ('notice', models.CharField(blank=True, max_length=128, verbose_name='备注')),
                ('status', models.CharField(choices=[('signed', '已报名'), ('unregistered', '未报名'), ('graduated', '已毕业')], max_length=64, verbose_name='状态')),
                ('join_date', models.DateField(verbose_name='入学日期')),
                ('class_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='internal.ClassList', verbose_name='班次')),
                ('referee', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='招生人')),
            ],
            options={
                'verbose_name': '学生信息',
                'verbose_name_plural': '学生信息',
                'permissions': (('simulate_import_stu', '允许模拟导入学生'), ('import_stu', '允许导入学生至商家系统')),
            },
        ),
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=8, verbose_name='性别')),
                ('qq', models.CharField(max_length=64, unique=True, verbose_name='QQ')),
                ('phone', models.CharField(blank=True, max_length=11, verbose_name='电话')),
                ('notice', models.CharField(blank=True, max_length=128, verbose_name='备注')),
                ('join_date', models.DateField(auto_now_add=True, verbose_name='入职时间')),
                ('status', models.CharField(choices=[('signed', '在职'), ('resigned', '离职')], default='signed', max_length=32, verbose_name='状态')),
            ],
            options={
                'verbose_name': '教师信息',
                'verbose_name_plural': '教师信息',
            },
        ),
        migrations.AddField(
            model_name='classrecord',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='internal.TeacherInfo', verbose_name='上课老师'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='internal.Course', verbose_name='科目'),
        ),
        migrations.AddField(
            model_name='classlist',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='internal.TeacherInfo', verbose_name='任课老师'),
        ),
    ]
