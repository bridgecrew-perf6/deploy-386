from django.db import models
from problem.models import Created


class Comment(Created):
    comment = models.TextField()
    author = models.ForeignKey(
        'account.User', related_name='comments',
         on_delete=models.DO_NOTHING
    )
    problems = models.ForeignKey(
        'problem.Problem', related_name='comments',
         on_delete=models.CASCADE, null=True, blank=True
    )
    reply = models.ForeignKey(
        'problem.Reply', related_name='comments',
         on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self) -> str:
        return self.comment
    
    class Meta:
        ordering = ('-created', )
