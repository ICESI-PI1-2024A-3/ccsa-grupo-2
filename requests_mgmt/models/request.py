from django.db import models


class Request(models.Model):
    type = models.CharField(max_length=100)
    status = models.ForeignKey("RequestStatus", on_delete=models.CASCADE, default=1)
    comments = models.TextField(null=True, blank=True)
    requester = models.ForeignKey(
        "users_mgmt.CustomUser",
        on_delete=models.CASCADE,
        related_name="requested_requests",
    )
    manager = models.ForeignKey(
        "users_mgmt.CustomUser",
        on_delete=models.CASCADE,
        related_name="managed_requests",
        null=True,
        blank=True,
    )
    reviewer = models.ForeignKey(
        "users_mgmt.CustomUser",
        on_delete=models.CASCADE,
        related_name="reviewed_requests",
        null=True,
        blank=True,
    )
    approver = models.ForeignKey(
        "users_mgmt.CustomUser",
        on_delete=models.CASCADE,
        related_name="approved_requests",
        null=True,
        blank=True,
    )
    initial_date = models.DateTimeField(auto_now_add=True)
    closing_date = models.DateTimeField(null=True, blank=True)

    def update_status(self, new_status):
        self.status = new_status
        self.save()