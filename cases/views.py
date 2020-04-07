from django.shortcuts import render, redirect

from cases.forms import CaseForm
from cases.models import Case


def home(request):
    cases = Case.objects.all()
    context = {'cases': cases}
    return render(request, 'cases/index.html', context)


def create(request):
    form = CaseForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('cases-home')
    context = {'form': form}
    return render(request, 'cases/case_form.html', context)


def update(request, case_id):
    if request.POST:
        form = CaseForm(request.POST)
        if form.is_valid():
            case = form.save(commit=False)
            case.id = case_id
            case.save()
            return redirect('cases-home')
    else:
        form = CaseForm(initial=Case.objects.get(pk=case_id).__dict__)
    context = {'form': form}
    return render(request, 'cases/case_form.html', context)


def delete(request, case_id):
    Case.objects.get(pk=case_id).delete()
    return redirect('cases-home')
