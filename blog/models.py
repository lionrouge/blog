from django.db import models

# Create your models here.
class User(models.Model):
	nick=models.CharField(max_length=20)
	name = models.CharField(max_length=100)
	last_login = models.DateTimeField('date published')
	register_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.nick

class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.title

#class Comment(models.Model):
#	body = models.TextField()
#	pub_date = models.DateTimeField('date published')
#	post = models.ForeignKey(Post)
#	author = models.ForeignKey(User)
#	def __unicode__(self):
#		return self.body[0:20]
