from django.db import models


class Format(models.Model):
    type = models.CharField(max_length=100)
    file = models.FileField(upload_to="formats/")


class RequestStatus(models.Model):
    status = models.CharField(max_length=100)


class RequestType(models.Model):
    type = models.CharField(max_length=100)


class Request(models.Model):
    type = models.ForeignKey(RequestType, on_delete=models.CASCADE)
    status = models.ForeignKey(RequestStatus, on_delete=models.CASCADE)
    requester = models.ForeignKey(
        "users_mgmt.CustomUser", on_delete=models.CASCADE, related_name="requested_requests"
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
    format = models.ForeignKey(Format, on_delete=models.CASCADE)
    initial_date = models.DateTimeField(auto_now_add=True)
    closing_date = models.DateTimeField(null=True, blank=True)


class Documents(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    file = models.FileField(upload_to="documents/")
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
