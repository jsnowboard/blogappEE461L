import datetime
from django.db import models
from django.utils import timezone

class Post(models.Model):
	post_title = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published', default=timezone.now)
	active_revision_id = models.IntegerField(default=0)
	def __str__(self):
		return self.post_title
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description= 'Published Recently?'
	
class PostContent(models.Model):
	post = models.ForeignKey(Post)
	post_content = models.TextField()
	revision_date = models.DateTimeField('Revision Date', default=timezone.now)
	revision_number = models.IntegerField(default=0)
	is_active_revision = models.BooleanField(default=False)
	def __str__(self):
		return 'Revision # ' + str(self.revision_number)
			
class BlogTitleContent(models.Model):
	post = models.ForeignKey(Post)
	post_title = models.CharField(max_length=200)
	post_content = models.TextField()
	pub_date = models.DateTimeField('date published', default=timezone.now)
	revision_date = models.DateTimeField('date published', default=timezone.now)
	def __str__(self):
		return self.post_title + ' Published on: ' + str(self.pub_date) + ' Revised on: ' +str(revision_date)