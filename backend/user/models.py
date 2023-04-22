from django.db import models

class User(models.Model):
    pk_bint_id = models.BigAutoField(primary_key=True, blank=False, null=False)
    vchr_first_name = models.CharField(max_length=50, blank=False, null=False)
    vchr_last_name = models.CharField(max_length=50)
    vchr_user_name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    vchr_email = models.CharField(max_length=50, unique=True, blank=False, null=False)
    bln_activated_email = models.BooleanField(default=False)
    vchr_password_hash = models.CharField(max_length=50, blank=False, null=False)
    dat_created = models.DateTimeField
    dat_updated = models.DateTimeField
    vchr_user_type = models.CharField(max_length=50)  # admin, tester, consumer
    vchr_role = models.CharField(max_length=50) # admin, team leader, team member
    txt_remarks = models.TextField
    int_status = models.IntegerField(default=0) # 0-Active, 1-Inactive, 2-Deleted

class UserHistory(models.Model):
    pk_bint_id = models.BigAutoField(primary_key=True, blank=False, null=False)
    fk_user_id = models.ForeignKey('User', models.CASCADE)
    dat_action = models.DateTimeField
    vchr_action = models.TextField