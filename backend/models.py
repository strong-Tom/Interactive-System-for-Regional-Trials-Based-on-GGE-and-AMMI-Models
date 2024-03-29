# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Blog(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=500)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'blog'


class DecisiontreeImg(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'decisiontree_img'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Forset(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    tree_species = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'forset'


class Linechart(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'linechart'


class Piechart(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'piechart'


class Poplar(models.Model):
    id = models.BigAutoField(primary_key=True)
    place = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    clone = models.CharField(max_length=100)
    rep = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    diameter = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'poplar'


class Qx(models.Model):
    fy_tem = models.FloatField(blank=True, null=True)
    qq_tem = models.FloatField(blank=True, null=True)
    lj_tem = models.FloatField(blank=True, null=True)
    dq_tem = models.FloatField(blank=True, null=True)
    hr_tem = models.FloatField(blank=True, null=True)
    nh_tem = models.FloatField(blank=True, null=True)
    gn_tem = models.FloatField(blank=True, null=True)
    fy_hum = models.FloatField(blank=True, null=True)
    qq_hum = models.FloatField(blank=True, null=True)
    lj_hum = models.FloatField(blank=True, null=True)
    dq_hum = models.FloatField(blank=True, null=True)
    hr_hum = models.FloatField(blank=True, null=True)
    nh_hum = models.FloatField(blank=True, null=True)
    gn_hum = models.FloatField(blank=True, null=True)
    fy_sum = models.FloatField(blank=True, null=True)
    qq_sum = models.FloatField(blank=True, null=True)
    lj_sum = models.FloatField(blank=True, null=True)
    dq_sum = models.FloatField(blank=True, null=True)
    hr_sum = models.FloatField(blank=True, null=True)
    nh_sum = models.FloatField(blank=True, null=True)
    gn_sum = models.FloatField(blank=True, null=True)
    fy_rai = models.FloatField(blank=True, null=True)
    qq_rai = models.FloatField(blank=True, null=True)
    lj_rai = models.FloatField(blank=True, null=True)
    dq_rai = models.FloatField(blank=True, null=True)
    hr_rai = models.FloatField(blank=True, null=True)
    nh_rai = models.FloatField(blank=True, null=True)
    gn_rai = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qx'


class RegionalSample(models.Model):
    id = models.BigAutoField(primary_key=True)
    tree = models.CharField(max_length=100)
    size = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'regional_sample'


class RuleTable(models.Model):
    id = models.BigAutoField(primary_key=True)
    file = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'rule_table'


class Savefile(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    create_time = models.DateTimeField()
    file_url = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'savefile'


class Treetmp(models.Model):
    id = models.BigAutoField(primary_key=True)
    place = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    clone = models.CharField(max_length=100)
    rep = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    diameter = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'treetmp'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'user'


class Video(models.Model):
    id = models.BigAutoField(primary_key=True)
    video = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'video'
