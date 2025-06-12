from django.shortcuts import render

# Create your views here.

def index(request):
    text = "xui"

    context = {

        'all_text': text
    }
    return render(
        request,
        context=context,
        template_name="booking/index.html"

    )