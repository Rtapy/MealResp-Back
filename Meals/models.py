from django.db import models 


class Meal(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    prep_time = models.IntegerField() 
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='meal_images/', blank=True, null=True)
    author = models.ForeignKey('author', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self):
        return self.name