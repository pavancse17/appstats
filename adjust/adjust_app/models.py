from django.db import models


class AppStat(models.Model):
    ANDROID = 1
    IOS = 2

    OS_PLATFORMS = (
        (ANDROID, "android"),
        (IOS, "ios"),
    )

    date = models.DateField()
    channel = models.CharField(max_length=255)
    country = models.CharField(max_length=2)
    os = models.IntegerField(choices=OS_PLATFORMS)
    impressions = models.PositiveIntegerField()
    clicks = models.PositiveIntegerField()
    installs = models.PositiveIntegerField()
    spend = models.FloatField()
    revenue = models.FloatField()
    cpi = models.FloatField()

    class Meta:
        ordering = ['date', ]

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.cpi = float(self.spend)/float(self.installs)
        super(AppStat, self).save(
            force_insert=False, force_update=False, using=None, update_fields=None
        )
