from django.db import models


class Banner(models.Model):
    """Hero banner images for the home page slider."""
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='banners/')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text='Lower numbers appear first')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.heading


class SchoolInfo(models.Model):
    """Singleton model for school information. Only one record should exist."""
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=300, blank=True)
    address = models.TextField()
    phone1 = models.CharField(max_length=15, verbose_name='Primary Phone')
    phone2 = models.CharField(max_length=15, blank=True, verbose_name='Secondary Phone')
    email = models.EmailField(blank=True)
    about_text = models.TextField(verbose_name='About Us')
    mission = models.TextField(blank=True, verbose_name='Our Mission')
    vision = models.TextField(blank=True, verbose_name='Our Vision')
    logo = models.ImageField(upload_to='school/', blank=True, null=True)
    established_year = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'School Information'
        verbose_name_plural = 'School Information'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and SchoolInfo.objects.exists():
            raise ValueError('Only one SchoolInfo instance is allowed.')
        return super().save(*args, **kwargs)


class Facility(models.Model):
    """Facilities available at the school (hostel, library, labs, etc.)."""
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='facilities/', blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, help_text='Font Awesome icon class (e.g., fa-book)')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Facilities'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
