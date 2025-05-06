from django.http import JsonResponse
from store.models import Product, Sale

def chatbot_view(request):
    if request.method == "POST":
        user_input = request.POST.get("message", "").lower()

        # Simple example logic
        if "list products" in user_input:
            products = Product.objects.all().values("name", "price")
            response = [f"{p['name']} - ${p['price']}" for p in products]
        elif "total sales" in user_input:
            total = Sale.objects.all().count()
            response = [f"Total number of sales: {total}"]
        else:
            response = ["Sorry, I didn't understand that. Try 'list products' or 'total sales'."]

        return JsonResponse({"response": response})
