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


class Reaction(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reactions")
	username = models.CharField(max_length=150)
	value = models.SmallIntegerField(choices=[(-1, "dislike"), (1, "like")])
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=["post", "username"], name="unique_reaction_per_user_post"),
		] 