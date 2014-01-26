from django.db import models


class Tags(models.Model):
    tag_name = models.TextField()
    tag_description = models.TextField()

    def __str__(self):
        return self.tag_name


class Posts(models.Model):
    post_title = models.CharField(max_length=100)
    post_date = models.DateField(auto_now=True)
    post_body = models.TextField()
    post_tags = models.ManyToManyField(Tags)


class Pages(models.Model):
    page_name = models.CharField(max_length=100, unique=True)
    page_html = models.TextField()

