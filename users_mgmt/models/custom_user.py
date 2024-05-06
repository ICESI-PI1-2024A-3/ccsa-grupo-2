from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    
    needs_approval = models.BooleanField(default=True)
    
    ADMIN = "admin"
    PROCESS_LEADER = "process_leader"
    ACCOUNTING_MANAGER = "accounting_manager"
    REQUESTER = "requester"
    REVIEWER = "reviewer"
    APPROVER = "approver"

    ROLES_CHOICES = [
        (ADMIN, "Admin"),
        (PROCESS_LEADER, "Process Leader"),
        (ACCOUNTING_MANAGER, "Accounting Manager"),
        (REQUESTER, "Requester"),
        (REVIEWER, "Reviewer"),
        (APPROVER, "Approver"),
    ]
    id_type = models.CharField(max_length=20, null=True, blank=True)
    id_number = models.CharField(max_length=20, null=True, blank=True)
    username = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=20, choices=ROLES_CHOICES, default=REQUESTER)
    process_leader = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )
    phone = models.CharField(max_length=20, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    groups = None
    user_permissions = None
    is_superuser = None
    is_staff = None
    date_joined = None

    def check_password(self, password):
        return self.password == password

    def __str__(self):
        return self.first_name + " " + self.last_name
