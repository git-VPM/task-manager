from django.db import models
from user.models import User
from django.contrib.postgres.fields import ArrayField

class Team(models.Model):
    pk_bint_id = models.BigAutoField(primary_key=True, blank=False, null=False)
    vchr_name = models.CharField(max_length=20, blank=False, null=False)
    vchr_description = models.TextField
    dat_created = models.DateTimeField
    fk_created_by = models.ForeignKey(User, models.CASCADE, blank=False, null=False)
    dat_updated = models.DateTimeField
    fk_updated_by = models.ForeignKey(User, models.CASCADE, blank=False, null=False, related_name='team_updated_by')
    int_status = models.IntegerField(default=0) # 0-Active, 1-Inactive, 2-Deleted
    arr_members = ArrayField(models.IntegerField())

class TeamHistory(models.Model):
    pk_bint_id = models.BigAutoField(primary_key=True, blank=False, null=False)
    fk_team_id = models.ForeignKey(Team, models.CASCADE)
    fk_action_user_id = models.ForeignKey(User, models.CASCADE)
    dat_action = models.DateTimeField
    vchr_action = models.TextField