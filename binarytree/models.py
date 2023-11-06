from django.db import models


class BinaryTree(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_left = models.BooleanField(default=False)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.name
