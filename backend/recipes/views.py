from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category  # Category моделыг нэмж импортлоно

def recipe_list(request):
    # 1. URL-аас сонгогдсон ангиллын slug-ийг авна
    category_slug = request.GET.get('category')
    
    # 2. Бүх ангиллыг авна 
    categories = Category.objects.all()
    
    # 3. Жоруудаа анхны байдлаар бүгдийг нь авна
    recipes = Recipe.objects.all().order_by('-created_at')

    # 4. Хэрэв хэрэглэгч ангилал сонгосон бол шүүлтүүр хийнэ
    if category_slug:
        recipes = recipes.filter(category__slug=category_slug)
    
    context = {
        'recipes': recipes,
        'categories': categories,
        'selected_category': category_slug,
    }
    
    return render(request, 'recipes/recipe_list.html', context)

def recipe_detail(request, slug):
    recipe = get_object_or_404(
        Recipe.objects.prefetch_related('recipeingredient_set__ingredient'), 
        slug=slug
    )
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})