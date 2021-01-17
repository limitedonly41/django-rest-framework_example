from django.db import models


class ToDoItem(models.Model):
    text = models.CharField(max_length=256)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"To Do: {self.text} ({' ' if self.done else 'not '} done)"