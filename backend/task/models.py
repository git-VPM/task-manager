from django.db import models
from user.models import User
from team.models import Team
from django.contrib.postgres.fields import ArrayField

class Task(models.Model):
    pk_bint_id = models.BigAutoField(primary_key=True, blank=False, null=False)
    vchr_name = models.CharField(max_length=20, blank=False, null=False)
    vchr_description = models.TextField
    dat_created = models.DateTimeField
    fk_created_by = models.ForeignKey(User, models.CASCADE, blank=False, null=False)
    dat_updated = models.DateTimeField
    fk_updated_by = models.ForeignKey(User, models.CASCADE, blank=False, null=False, related_name='task_updated_by')
    int_status = models.IntegerField(default=0) # 0-Open, 1-In progress, 2-Completed
    fk_responsible_id = models.ForeignKey(User, models.CASCADE, blank=False, null=False, related_name='task_fk_responsible_id')
    arr_assigned = ArrayField(models.IntegerField())

class TaskHistory(models.Model):
    pk_bint_id = models.BigAutoField(primary_key=True, blank=False, null=False)
    fk_team_id = models.ForeignKey(Team, models.CASCADE)
    fk_action_user_id = models.ForeignKey(User, models.CASCADE)
    dat_action = models.DateTimeField
    vchr_action = models.TextField