from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PocketItem(models.Model):

    STATUS_CHOICE = (
        (0, 'not archived'),
        (1, 'archived'),
        (2, 'shoule be deleted')
    )
    item_id = models.BigIntegerField(primary_key=True)
    resolve_id = models.BigIntegerField(null=True, blank=True)
    given_url = models.URLField()
    given_title = models.CharField(max_length=200)
    resolved_title = models.CharField(max_length=200, null=True, blank=True)
    favorite = models.BooleanField(default=0)
    status = models.IntegerField(choices=STATUS_CHOICE, default=0)
    excerpt = models.CharField(max_length=500, null=True, blank=True)
    is_article = models.BooleanField(default=1)
    has_image = models.BooleanField(default=0)
    has_video = models.BooleanField(default=0)
    word_count = models.IntegerField(default=0)
    time_added = models.DateTimeField()
    time_favorited = models.DateTimeField(null=True)
    time_updated = models.DateTimeField(null=True)
    time_read = models.DateTimeField(null=True)

    class Meta:
        app_label = 'pocketapp'
        db_table = 'pocket_item'
        verbose_name = u'pocket_item'
        verbose_name_plural = u'pocket_item'

    def __unicode__(self):
        return '%s - %s' % (self.item_id, self.given_title)

class PocketTag(models.Model):

    item_id = models.BigIntegerField()
    tag = models.CharField(max_length=100)

    class Meta:
        app_label = 'pocketapp'
        db_table = 'pocket_tag'
        verbose_name = u'pocket_tag'
        verbose_name_plural = u'pocket_tags'

    def __unicode__(self):
        return "%s-%s" % (self.item_id, self.tag)

class PocketImage(models.Model):

    item_id = models.BigIntegerField()
    image_id = models.IntegerField()
    src = models.CharField(max_length=200)
    credit = models.CharField(max_length=200, null=True)
    caption = models.CharField(max_length=100, null=True)
    height = models.IntegerField(null=True)
    width = models.IntegerField(null=True)

    class Meta:
        app_label = 'pocketapp'
        db_table = 'pocket_image'
        verbose_name = u'pocket_image'
        verbose_name_plural = u'pocket_images'

    def __unicode__(self):
        return "image:%s-%s" % (self.item_id, self.src)


class PocketVideo(models.Model):

    item_id = models.BigIntegerField()
    video_id = models.IntegerField()
    src = models.CharField(max_length=200)
    credit = models.CharField(max_length=200, null=True)
    captions = models.CharField(max_length=100, null=True)
    height = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    vid = models.CharField(max_length=100, null=True)


    class Meta:
        app_label = 'pocketapp'
        db_table = 'pocket_video'
        verbose_name = u'pocket_video'
        verbose_name_plural = u'pocket_videos'

    def __unicode__(self):
        return "video:%s-%s" % (self.item_id, self.src)