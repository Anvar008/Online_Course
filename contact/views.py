from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from contact.forms import ContactForm

@login_required(login_url='login')
def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)
