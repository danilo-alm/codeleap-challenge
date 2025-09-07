from django.db import models


class Post(models.Model):
	username = models.CharField(max_length=150)
	title = models.CharField(max_length=255)
	content = models.TextField()
	created_datetime = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["-created_datetime", "-id"]

	def __str__(self) -> str:
		return f"{self.username}: {self.title}" 