from django.shortcuts import render
from .models import scheme_details
from .forms import checkform
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,'schemes/home.html')
def businessloans(request):
    context = {
        'schemes': scheme_details.objects.filter(department='Business Loans')
    }
    return render(request,'schemes/businessloans.html',context)
def education(request):
    context = {
        'schemes': scheme_details.objects.filter(department='Education')
    }
    return render(request,'schemes/education.html',context)
def pension(request):
    context={
        'schemes':scheme_details.objects.filter(department='Pension')
    }
    return render(request,'schemes/pension.html',context)
def housing(request):
    context = {
        'schemes': scheme_details.objects.filter(department='Housing')
    }
    return render(request,'schemes/housing.html',context)
def health(request):
    context = {
        'schemes': scheme_details.objects.filter(department='Health')
    }
    return render(request,'schemes/health.html',context)
def training_and_employment(request):
    context = {
        'schemes': scheme_details.objects.filter(department='Training and Employment')
    }
    return render(request,'schemes/training_and_employment.html',context)
def insurance(request):
    context = {
        'schemes': scheme_details.objects.filter(department='Insurance')
    }
    return render(request,'schemes/insurance.html',context)
def financial_accounts(request):
    context = {
        'schemes': scheme_details.objects.filter(department='Financial Accounts')
    }
    return render(request,'schemes/financial_accounts.html',context)
def eligible(request):
    return render(request,'schemes/eligible.html')
def noteligible(request):
    return render(request,'schemes/noteligible.html')
def gen_criteria(sequence):
    for index in range(len(sequence)-1, -1, -1):
        yield sequence[index]
def split_criteria(required):
    criteria=(required.eligibility_criteria).split(',')
    return gen_criteria(criteria)
pmvvy_required = scheme_details.objects.filter(name='Pradhan Mantri Vaya Vandana Yojana').first()
pmvvy_result=split_criteria(pmvvy_required)
def PMVVY(request):
    if request.method=="POST":
        form = checkform(request.POST)
        if form.is_valid():
            if request.POST['options'] == 'yes':
                try:
                    x = next(pmvvy_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html', {'a': pmvvy_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(pmvvy_result)
    return render(request, 'schemes/PMVVY.html',{'form':form,'c':x})
apy_required = scheme_details.objects.filter(name='Atal Pension Yojana').first()
apy_result=split_criteria(apy_required)
def APY(request):
    if request.method=="POST":
        form = checkform(request.POST)
        if form.is_valid():
            if request.POST['options'] == 'yes':
                try:
                    x = next(apy_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html', {'a': apy_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(apy_result)
    return render(request, 'schemes/APY.html',{'form':form,'c':x})
suils_required = scheme_details.objects.filter(name='Stand Up India Loan Scheme').first()
suils_result=split_criteria(suils_required)
def SUILS(request):
    if request.method=="POST":
        form=checkform(request.POST)
        if form.is_valid():
            if request.POST['options']=='yes':
                try:
                    x=next(suils_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html',{'a':suils_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(suils_result)
    return render(request, 'schemes/SUILS.html',{'form':form,'c':x})
scm_required = scheme_details.objects.filter(name='Solar Charkha Mission').first()
scm_result=split_criteria(scm_required)
def SCM(request):
    if request.method=="POST":
        form=checkform(request.POST)
        if form.is_valid():
            if request.POST['options']=='yes':
                try:
                    x=next(scm_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html',{'a':scm_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(scm_result)
    return render(request, 'schemes/SCM.html',{'form':form,'c':x})
pmmy_required = scheme_details.objects.filter(name='Pradhan Mantri Mudra Yojana').first()
pmmy_result=split_criteria(pmmy_required)
def PMMY(request):
    if request.method=="POST":
        form=checkform(request.POST)
        if form.is_valid():
            if request.POST['options']=='yes':
                try:
                    x=next(pmmy_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html',{'a':pmmy_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(pmmy_result)
    return render(request, 'schemes/PMMY.html',{'form':form,'c':x})
rsbmy_required = scheme_details.objects.filter(name='Rashtriya Swasthya Bima Yojana').first()
rsbmy_result=split_criteria(rsbmy_required)
def RSBMY(request):
    if request.method=="POST":
        form=checkform(request.POST)
        if form.is_valid():
            if request.POST['options']=='yes':
                try:
                    x=next(rsbmy_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html',{'a':rsbmy_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(rsbmy_result)
    return render(request, 'schemes/RSBMY.html',{'form':form,'c':x})
pmsmy_required = scheme_details.objects.filter(name='Pradhan Mantri Surakshit Matritva Yojana').first()
pmsmy_result=split_criteria(pmsmy_required)
def PMSMY(request):
    if request.method=="POST":
        form=checkform(request.POST)
        if form.is_valid():
            if request.POST['options']=='yes':
                try:
                    x=next(pmsmy_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html',{'a':pmsmy_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(pmsmy_result)
    return render(request, 'schemes/PMSMY.html',{'form':form,'c':x})
pmjaya_required = scheme_details.objects.filter(name='Pradhan Mantri Jan Arogya Yojana Abhiyan').first()
pmjaya_result=split_criteria(pmjaya_required)
def PMJAYA(request):
    if request.method=="POST":
        form = checkform(request.POST)
        if form.is_valid():
            if request.POST['options'] == 'yes':
                try:
                    x = next(pmjaya_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html', {'a': pmjaya_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(pmjaya_result)
    return render(request, 'schemes/PMJAYA.html',{'form':form,'c':x})
pmjdy_required = scheme_details.objects.filter(name='Pradhan Mantri Jan Dhan Yojana').first()
pmjdy_result=split_criteria(pmjdy_required)
def PMJDY(request):
    if request.method=="POST":
        form = checkform(request.POST)
        if form.is_valid():
            if request.POST['options'] == 'yes':
                try:
                    x = next(pmjdy_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html', {'a': pmjdy_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(pmjdy_result)
    return render(request, 'schemes/PMJDY.html',{'form':form,'c':x})
pmssy_required = scheme_details.objects.filter(name='Pradhan Mantri Sukanya Samriddhi Yojana').first()
pmssy_result=split_criteria(pmssy_required)
def PMSSY(request):
    if request.method=="POST":
        form = checkform(request.POST)
        if form.is_valid():
            if request.POST['options'] == 'yes':
                try:
                    x = next(pmssy_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html', {'a': pmssy_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(pmssy_result)
    return render(request, 'schemes/PMSSY.html',{'form':form,'c':x})
aay_required = scheme_details.objects.filter(name='Antyodaya Anna Yojana').first()
aay_result=split_criteria(aay_required)
def AAY(request):
    if request.method=="POST":
        form = checkform(request.POST)
        if form.is_valid():
            if request.POST['options'] == 'yes':
                try:
                    x = next(aay_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html', {'a': aay_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(aay_result)
    return render(request, 'schemes/AAY.html',{'form':form,'c':x})
pmuy_required = scheme_details.objects.filter(name='Pradhan Mantri Ujjwala Yojana').first()
pmuy_result=split_criteria(pmuy_required)
def PMUY(request):
    if request.method=="POST":
        form = checkform(request.POST)
        if form.is_valid():
            if request.POST['options'] == 'yes':
                try:
                    x = next(pmuy_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html', {'a': pmuy_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(pmuy_result)
    return render(request, 'schemes/PMUY.html',{'form':form,'c':x})
pmay_required = scheme_details.objects.filter(name='Pradhan Mantri Awas Yojana').first()
pmay_result=split_criteria(pmay_required)
def PMAY(request):
    if request.method=="POST":
        form = checkform(request.POST)
        if form.is_valid():
            if request.POST['options'] == 'yes':
                try:
                    x = next(pmay_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html', {'a': pmay_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(pmay_result)
    return render(request, 'schemes/PMAY.html',{'form':form,'c':x})
pmsy_required = scheme_details.objects.filter(name='Pradhan Mantri Saubhagya Yojana').first()
pmsy_result=split_criteria(pmsy_required)
def PMSY(request):
    if request.method=="POST":
        form = checkform(request.POST)
        if form.is_valid():
            if request.POST['options'] == 'yes':
                try:
                    x = next(pmsy_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html', {'a': pmsy_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(pmsy_result)
    return render(request, 'schemes/PMSY.html',{'form':form,'c':x})
ujala_required = scheme_details.objects.filter(name='Ujala').first()
ujala_result=split_criteria(ujala_required)
def Ujala(request):
    if request.method=="POST":
        form = checkform(request.POST)
        if form.is_valid():
            if request.POST['options'] == 'yes':
                try:
                    x = next(ujala_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html', {'a': ujala_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(ujala_result)
    return render(request, 'schemes/Ujala.html',{'form':form,'c':x})
nrega_required = scheme_details.objects.filter(name='National Rural Employment Guarantee Act').first()
nrega_result=split_criteria(nrega_required)
def NREGA(request):
    if request.method=="POST":
        form = checkform(request.POST)
        if form.is_valid():
            if request.POST['options'] == 'yes':
                try:
                    x = next(nrega_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html', {'a': nrega_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(nrega_result)
    return render(request, 'schemes/NREGA.html',{'form':form,'c':x})
pmkvy_required = scheme_details.objects.filter(name='Pradhan Mantri Kaushal Vikas Yojana').first()
pmkvy_result=split_criteria(pmkvy_required)
def PMKVY(request):
    if request.method=="POST":
        form = checkform(request.POST)
        if form.is_valid():
            if request.POST['options'] == 'yes':
                try:
                    x = next(pmkvy_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html', {'a': pmkvy_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(pmkvy_result)
    return render(request, 'schemes/PMKVY.html',{'form':form,'c':x})
pmfby_required = scheme_details.objects.filter(name='Pradhan Mantri Fasal Bima Yojana').first()
pmfby_result=split_criteria(pmfby_required)
def PMFBY(request):
    if request.method=="POST":
        form = checkform(request.POST)
        if form.is_valid():
            if request.POST['options'] == 'yes':
                try:
                    x = next(pmfby_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html', {'a': pmfby_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(pmfby_result)
    return render(request, 'schemes/PMFBY.html',{'form':form,'c':x})
pmsby_required = scheme_details.objects.filter(name='Pradhan Mantri Suraksha Bima Yojana').first()
pmsby_result=split_criteria(pmsby_required)
def PMSBY(request):
    if request.method=="POST":
        form = checkform(request.POST)
        if form.is_valid():
            if request.POST['options'] == 'yes':
                try:
                    x = next(pmsby_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html', {'a': pmsby_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(pmsby_result)
    return render(request, 'schemes/PMSBY.html',{'form':form,'c':x})
pmjjby_required = scheme_details.objects.filter(name='Pradhan Mantri Jeevan Jyoti Bima Yojana').first()
pmjjby_result=split_criteria(pmjjby_required)
def PMJJBY(request):
    if request.method=="POST":
        form = checkform(request.POST)
        if form.is_valid():
            if request.POST['options'] == 'yes':
                try:
                    x = next(pmjjby_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html', {'a': pmjjby_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(pmjjby_result)
    return render(request, 'schemes/PMJJBY.html',{'form':form,'c':x})
pmss_required = scheme_details.objects.filter(name='Pradhan Mantri Jeevan Jyoti Bima Yojana').first()
pmss_result=split_criteria(pmss_required)
def PMSS(request):
    if request.method=="POST":
        form = checkform(request.POST)
        if form.is_valid():
            if request.POST['options'] == 'yes':
                try:
                    x = next(pmss_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html', {'a': pmss_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(pmss_result)
    return render(request, 'schemes/PMSS.html',{'form':form,'c':x})
pmvlk_required = scheme_details.objects.filter(name='Pradhan Mantri Vidya Lakshmi Karyakram').first()
pmvlk_result=split_criteria(pmvlk_required)
def PMVLK(request):
    if request.method=="POST":
        form = checkform(request.POST)
        if form.is_valid():
            if request.POST['options'] == 'yes':
                try:
                    x = next(pmvlk_result)
                except StopIteration:
                    return render(request, 'schemes/eligible.html', {'a': pmvlk_required.apply_link})
            else:
                return HttpResponseRedirect('/noteligible/')
    else:
        form=checkform()
        x=next(pmvlk_result)
    return render(request, 'schemes/PMVLK.html',{'form':form,'c':x})