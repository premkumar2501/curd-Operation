from django.shortcuts import render,redirect
from .models import Profile

def home(request):
    details=Profile.objects.all()
    if (details!=''):
        return render(request,'see_profile.html',{'details':details})
    else:
        return render(request,'profile.html')

def save(request):
    if request.method=='POST':
        my_name=request.POST['name']
        mother_name=request.POST['mother']
        father_name=request.POST['father']
        cell=request.POST['phone']
        mail=request.POST['mail']
        dateofbirth=request.POST['dob']
        obj=Profile()

        obj.Name=my_name
        obj.Mother=mother_name
        obj.Father=father_name
        obj.Phone=cell
        obj.Email=mail
        obj.Date_of_birth=dateofbirth
        obj.save()
        return redirect('home')
    return render(request,'profile.html')

def addData(request):
    return redirect('save')

def viewData(request):
    return redirect('home')

def update(request,id):
    mydata=Profile.objects.get(id=id)
    if request.method=='POST':
        my_name=request.POST['name']
        mother_name=request.POST['mother']
        father_name=request.POST['father']
        cell=request.POST['phone']
        mail=request.POST['mail']
        dateofbirth=request.POST['dob']

        mydata.Name=my_name
        mydata.Mother=mother_name
        mydata.Father=father_name
        mydata.Phone=cell
        mydata.Email=mail
        mydata.Date_of_birth=dateofbirth
        mydata.save()
        return redirect('home')
    return render(request,'update_profile.html',{'mydata':mydata})

def delete(request,id):
    mydata=Profile.objects.get(id=id)   
    mydata.delete()
    return redirect('home')









