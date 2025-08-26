from django.shortcuts import render
from .models import Contact

# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = contacts.filter(full_name__icontains=search_input)
    else:
        contacts = contacts.all()
        search_input = ''
    return render(request, 'index.html', {'contacts': contacts, 'search_input': search_input})

def add_contact(request):
    if request.method == 'POST':
        new_contact = Contact(
            full_name=request.POST.get('full_name'),
            relationship=request.POST.get('relationship'),
            phone_number=request.POST.get('phone_number'),
            email=request.POST.get('email'),
            address=request.POST.get('address')
        )
        new_contact.save()
    return render(request, 'new.html')

def contact_profile(request, pk):
    contact = Contact.objects.get(id=pk)
    return  render(request, 'contact_profile.html', {'contact': contact})

def edit_contact(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact.full_name = request.POST['full_name']
        contact.relationship = request.POST['relationship']
        contact.phone_number = request.POST['phone_number']
        contact.email = request.POST['email']
        contact.address = request.POST['address']
        contact.save()
    return render(request, 'edit.html', {'contact': contact})

def delete_contact(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('index')
    return render(request, 'delete.html', {'contact': contact})