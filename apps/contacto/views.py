from django.shortcuts import render, redirect
from .forms import ContactoForm

# Create your views here.
def contact(request):
    return render(request, 'pages/contact.html')

def formulario(request):
    # print('form')
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
        return redirect('formulario')
    else:
        form = ContactoForm()

    return render(request, 'pages/form.html', {'form': form})