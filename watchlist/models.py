from django.db import models
from django.conf import settings
from movies.models import Movie
from django.utils.text import slugify

# Create your models here.


class Watchlist(models.Model):
    """
    Represents a user's custom watchlist of movies
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='watchlists'
    )

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='in_watchlists',
    )

    # Timestamp when added to the watchlist
    created_at = models.DateTimeField(auto_now_add=True)
    # Optional unique slug for sharing
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        # Ensures no duplicate movies in the watchlist for the same user
        unique_together = ('user', 'movie')
        verbose_name = "Watchlist Entry"
        verbose_name_plural = "Watchlist Entries"

    def __str__(self):
        return f"{
            self.user.username}'s Watchlist: {
            self.movie.title if self.movie else 'No Movie'}"

    def get_absolute_url(self):
        """
        Returns the URL for this specific watchlist entry
        """
        return f"/watchlist/{self.slug}/"

    def save(self, *args, **kwargs):
        if not self.slug and self.movie:
            # Generate a unique slug dynamically
            base_slug = slugify(f"{self.user.username}-{self.movie.title}")
            slug = base_slug

            counter = 1
            while Watchlist.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug
        super().save(*args, **kwargs)
