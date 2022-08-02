from django.shortcuts import redirect, render

from .models import Trans

from languages.translator_function import translate_letters
# Create your views here.




def home(request):
    if request.method == 'POST':
        # get noun from request 
        noun=request.POST['noun']
        return redirect(f'/result/{noun}')
        
    return render(request,'home.html')


def translate(request , noun):

    # search about the noun
    data=Trans.objects.filter(noun__icontains=noun)

    list_of_results = []

    if data is not None:

        for result in data:


            list_of_results.append(
                {
                    'noun' : translate_letters(result.noun),
                    # if u want to return only the noun delete this three lines ⬇⬇
                    'date_of_birth' : result.datebirth,
                    'address' : translate_letters(result.address),
                    'nationality' : translate_letters(result.nationality)
                }
            )
        
        
        
     
    return render(request,'result.html',{'results':list_of_results})