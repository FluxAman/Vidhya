from django.db import models
from django.utils import timezone


class Notice(models.Model):
    """School notices and announcements."""
    title = models.CharField(max_length=200, help_text='Notice title')
    content = models.TextField(help_text='Detailed notice content')
    date_posted = models.DateTimeField(default=timezone.now, help_text='Notice date (editable)')
    is_active = models.BooleanField(default=True, help_text='Show on website')
    is_important = models.BooleanField(default=False, help_text='Highlight this notice')
    attachment = models.FileField(
        upload_to='notices/', 
        blank=True, 
        null=True, 
        help_text='PDF or document (optional)'
    )

    class Meta:
        ordering = ['-is_important', '-date_posted']
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'

    def __str__(self):
        return self.title
