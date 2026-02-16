from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from decimal import Decimal


class User(AbstractUser):
    """
    Gateway User model - Aggregates user information from auth service
    """
    ROLES = (
        ("admin", "Admin"),
        ("student", "Student"),
        ("teacher", "Teacher"),
        ("parent", "Parent"),
        ("staff", "Staff"),
        ("ministry", "Ministry")
    )
    role = models.CharField(max_length=20, choices=ROLES)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_active_in_system = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Gateway User"
        verbose_name_plural = "Gateway Users"
    
    def __str__(self):
        return f"{self.get_full_name()} - {self.role}"


class StudentProfile(models.Model):
    """
    Aggregated student profile combining data from student service
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    admission_number = models.CharField(max_length=20, unique=True)
    grade = models.CharField(max_length=10)
    curriculum = models.CharField(
        max_length=100, 
        choices=[("CBC", "CBC"), ("British", "British"), ("8-4-4", "8-4-4")]
    )
    parent = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='children'
    )
    enrollment_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Student Profile"
        verbose_name_plural = "Student Profiles"
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.admission_number}"


class StaffProfile(models.Model):
    """
    Aggregated staff profile combining data from staff service
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile')
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    employment_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Staff Profile"
        verbose_name_plural = "Staff Profiles"
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.position}"


class Subject(models.Model):
    """
    Subject model aggregated from curriculum service
    """
    name = models.CharField(max_length=100)
    curriculum = models.CharField(
        max_length=30, 
        choices=[("CBC", "CBC"), ("8-4-4", "8-4-4"), ("British", "British Curriculum")]
    )
    code = models.CharField(max_length=20, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
    
    def __str__(self):
        return f"{self.name} ({self.curriculum})"


class Assessment(models.Model):
    """
    Assessment model aggregated from curriculum service
    """
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='assessments')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='assessments')
    score = models.FloatField()
    competency = models.CharField(max_length=100, blank=True, null=True)  # CBC-specific
    term = models.CharField(max_length=20)
    date_assessed = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name = "Assessment"
        verbose_name_plural = "Assessments"
        ordering = ['-date_assessed']
    
    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.subject.name} ({self.term})"


class Transaction(models.Model):
    """
    Financial transaction model aggregated from finance service
    """
    TRANSACTION_TYPES = (
        ('fee_payment', 'Fee Payment'),
        ('refund', 'Refund'),
        ('salary', 'Salary'),
        ('expense', 'Expense'),
        ('other', 'Other')
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    description = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    reference_number = models.CharField(max_length=50, unique=True, blank=True, null=True)
    
    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.amount} ({self.transaction_type})"


class Fee(models.Model):
    """
    Fee model aggregated from finance service
    """
    STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('balance', 'Balance'),
        ('pending', 'Pending'),
        ('overdue', 'Overdue')
    )
    
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='fees')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateTimeField()
    paid_date = models.DateTimeField(null=True, blank=True)
    term = models.CharField(max_length=20, blank=True, null=True)
    
    class Meta:
        verbose_name = "Fee"
        verbose_name_plural = "Fees"
        ordering = ['due_date']
    
    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.amount} ({self.status})"


class Notification(models.Model):
    """
    Notification model aggregated from notification service
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Notification for {self.user.get_full_name()}"


class Message(models.Model):
    """
    Message model aggregated from notification service
    """
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"Message from {self.sender.get_full_name()} to {self.recipient.get_full_name()}"


class Announcement(models.Model):
    """
    Announcement model aggregated from notification service
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='announcements')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class Alert(models.Model):
    """
    Alert model aggregated from notification service
    """
    SEVERITY_CHOICES = (
        ('info', 'Info'),
        ('warning', 'Warning'),
        ('critical', 'Critical')
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alerts')
    message = models.CharField(max_length=255)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Alert"
        verbose_name_plural = "Alerts"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.severity.upper()} - {self.message}"


class ServiceRegistry(models.Model):
    """
    Registry for microservices to enable service discovery
    """
    SERVICE_STATUS = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Maintenance')
    )
    
    service_name = models.CharField(max_length=100, unique=True)
    base_url = models.URLField()
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=SERVICE_STATUS, default='active')
    last_health_check = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Service Registry"
        verbose_name_plural = "Service Registries"
    
    def __str__(self):
        return f"{self.service_name} - {self.status}"


class ApiKey(models.Model):
    """
    API keys for service-to-service authentication
    """
    service = models.ForeignKey(ServiceRegistry, on_delete=models.CASCADE, related_name='api_keys')
    key = models.CharField(max_length=128, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    last_used = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = "API Key"
        verbose_name_plural = "API Keys"
    
    def __str__(self):
        return f"Key for {self.service.service_name}"


class ServiceLog(models.Model):
    """
    Logs for inter-service communication and requests
    """
    LOG_TYPES = (
        ('request', 'Request'),
        ('response', 'Response'),
        ('error', 'Error')
    )
    
    source_service = models.CharField(max_length=100)
    target_service = models.ForeignKey(ServiceRegistry, on_delete=models.SET_NULL, null=True)
    endpoint = models.CharField(max_length=255)
    method = models.CharField(max_length=10)  # GET, POST, PUT, DELETE, etc.
    log_type = models.CharField(max_length=20, choices=LOG_TYPES)
    status_code = models.IntegerField(null=True, blank=True)
    request_data = models.JSONField(null=True, blank=True)
    response_data = models.JSONField(null=True, blank=True)
    error_message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    duration_ms = models.IntegerField(null=True, blank=True)  # Response time in milliseconds
    
    class Meta:
        verbose_name = "Service Log"
        verbose_name_plural = "Service Logs"
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['timestamp']),
            models.Index(fields=['target_service']),
        ]
    
    def __str__(self):
        return f"{self.source_service} -> {self.target_service} [{self.method} {self.endpoint}]"


class RouteConfig(models.Model):
    """
    Configuration for routing requests to appropriate services
    """
    METHODS = (
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE'),
        ('PATCH', 'PATCH'),
        ('ALL', 'ALL')
    )
    
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10, choices=METHODS)
    target_service = models.ForeignKey(ServiceRegistry, on_delete=models.CASCADE)
    is_public = models.BooleanField(default=False)
    requires_auth = models.BooleanField(default=True)
    allowed_roles = models.TextField(blank=True, null=True)  # Comma-separated roles
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Route Config"
        verbose_name_plural = "Route Configs"
        unique_together = ('path', 'method')
    
    def __str__(self):
        return f"{self.method} {self.path} -> {self.target_service.service_name}"
