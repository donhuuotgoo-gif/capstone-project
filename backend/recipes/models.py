from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ангиллын нэр")
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Орцны нэр")

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name="Коктейлийн нэр")
    slug = models.SlugField(blank=True, null=True, unique=True)
    instructions = models.TextField(verbose_name="Хийх заавар")
    image = models.ImageField(upload_to='cocktails/', null=True, blank=True, verbose_name="Коктейлийн зураг")
    
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='recipes')
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50, verbose_name="Хэмжээ (жишээ нь: 50ml)")

    def __str__(self):
        return f"{self.amount} of {self.ingredient.name} for {self.recipe.title}"