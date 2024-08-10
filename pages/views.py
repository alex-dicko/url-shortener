from django.shortcuts import render
from django.contrib import messages
from . forms import LinkForm
from . models import link


def url(request, id):
    try:
        redirect = link.objects.get(id=id)
    except:
        return render(
        request,
        'error.html',
        {
            
        }
    )
    
    return render(
    request,
    'redirect.html',
    {
        'url': redirect.redirect_link,
    }
)
    
        

        
    
# Create your views here.
def index(request):
    form = LinkForm()
    link_instance = False

    if request.POST:
        form = LinkForm(request.POST)

        if form.is_valid():
            link_instance = form.save(commit=False)  # Get the unsaved model instance
            link_instance.identifier = hash(link_instance.redirect_link)  # Set the identifier on the model instance
            link_instance.save() 
            messages.error(request,'Successfully Created Short Url')
        else:
            messages.error(request,'Error!')
            
            
            
        
            

    return render(
        request,
        'home.html',
        {
            'form': form,
            'link': link_instance, 


        },
    )