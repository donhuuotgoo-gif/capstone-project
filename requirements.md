# [Cocktail Recipes] — Requirements

## 1. Төслийн Тойм
Өөрт байгаа орцуудаа ашиглаж cocktail хийхэд туслах, дуртай cocktail-оо хадгалаж авах

## 2. Хэрэглэгчид
- Админ: Жор нийтлэх, засах, устгах, ангилах
- Хэрэглэгч: Жор хайх, дуртай жороо тэмдэглэх

## 3. Core Features (MVP)
- Admin authentication: register, login, logout
- Post: Create Recipe, read, update, delete 
- Add: Ingredients
- Favorite Recipe toggle
- Cocktail type
- Search Recipe, Ingredient

## 4. Tech Stack
- Backend: Django 5, Django Templates
- Interactivity: HTMX
- Styling: Pico CSS
- Database: PostgreSQL (Docker)
- Auth: Django built-in authentication

## 5. Хязгаарлалт
- Хугацаа: 4 долоо хоног
- Баг: Ганцаарчилсан

## 6. Амжилтын Шалгуур
- [ ] Admin auth ажиллаж байгаа
- [ ] Recipe, ingredient CRUD бүрэн ажиллана
- [ ] Дуртай жороо favorite toggle хийж тэмдэглэх болох
- [ ] Төрлөөр ангилагдсан байх
- [ ] Search recipe, ingredient ажиллаж байх
- [ ] Tests бичсэн
- [ ] Deploy хийсэн

## 7. User Stories
- US-001: As a visitor, I want to save favorite recipes to my browser session, so that I can see them during my current visit without creating an account.
- US-002, Admin, "Create, edit, and delete recipes", 
I can keep the cocktail database up to date with new and correct information.
- US-003, User, Search for recipes by name or ingredient, 
I can find cocktails that I can make with the ingredients I already have at home.
- US-004, User, "Toggle the ""Favorite"" button on a recipe", 
I can quickly build a personal collection of cocktails I enjoy.
- US-005, Visitor, "Filter cocktails by type (e.g., Mocktail, Classic, Strong)", 
I can find a drink that suits the specific occasion or my mood.
- US-006, User, See real-time search results using HTMX, 
I can find recipes instantly without the whole page reloading.
- US-007, Admin, Add and categorize new ingredients,
I can ensure that recipes are linked to a standardized list of ingredients.
- US-008, User, "View a ""My Favorites"" list",I can have a curated menu of my top-rated cocktails in one place.