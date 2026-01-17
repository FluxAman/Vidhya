from django.db import models


class Notice(models.Model):
    """School notices and announcements."""
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_important = models.BooleanField(default=False, help_text='Mark as important for highlight')
    attachment = models.FileField(upload_to='notices/', blank=True, null=True, help_text='PDF or document attachment')

    class Meta:
        ordering = ['-is_important', '-date_posted']

    def __str__(self):
        return self.title
