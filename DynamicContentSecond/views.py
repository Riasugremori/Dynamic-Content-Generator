from django.shortcuts import render, redirect

def generator_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('name')
        return redirect('Generated', word=user_input)
    return render(request, 'generator.html')

def generated_view(request, word):
    context = {'word': word}
    return render(request, 'GeneratedPage.html', context)


           