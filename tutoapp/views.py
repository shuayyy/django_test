
from django.shortcuts import render
from tutoapp.models import Member,Details

def index(request):
    members=Member.objects.all()
    details = Details.objects.all()

    return render(request , 'tutoapp/index.html',{
     'members' :members,
     'details':details,}
    )

def contact(request):
    members=Member.objects.all()
    details = Details.objects.all()

    return render(request , 'tutoapp/contact.html',{'members' :members,
     'details':details,} 
     )

def wdqd(request):
    members=Member.objects.all()
    details = Details.objects.all()

    return render(request , 'tutoapp/wdqd.html',{'members' :members,
     'details':details,} 
     )
