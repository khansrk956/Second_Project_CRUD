from django.shortcuts import render,redirect
from django.views import View
from app2.models import Student
from app2.forms import StudentForm
# Create your views here.

# Here View,Delete,Add,Update data
class Home(View):
    def get(self,request):
        stu_data = Student.objects.all()
        return render(request,'home.html',{'data':stu_data})
    

# Here Insert Data 
class Addstudent(View):
    def get(self, request):
        show_form = StudentForm()
        return render(request,'add-student.html',{'show_form':show_form})
    
    def post(self,request):
        show_form = StudentForm()
        save_data = StudentForm(request.POST)
        if save_data.is_valid():
            save_data.save()
            return redirect('/')
        else:
            return render(request,'add-student.html',{'show_form':show_form})


# Here Delete Data..    
class DeleteStudent(View):
    def post(self,request):
        del_id = request.POST
        form_id = del_id.get('id')
        stu_del = Student.objects.get(id=form_id)
        stu_del.delete()
        return redirect('/')


# Here Update Data
class UpdateStudent(View):
    def get(self,request,id):
        stu = Student.objects.get(id=id)
        all_data = StudentForm(instance=stu)
        
        return render(request,'edit.html',{'form':all_data})
    
    def post(self,request,id):
        stu=Student.objects.get(id=id)
        up_data = StudentForm(request.POST, instance=stu)
        if up_data.is_valid():
            up_data.save()
            return redirect('/')

    