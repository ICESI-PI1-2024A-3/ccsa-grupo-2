from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
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
    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
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
    username = None
    date_joined = None
