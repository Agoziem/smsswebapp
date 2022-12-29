from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from Home.models import School
from django.contrib.auth.decorators import login_required
import base64
base64.encodestring = base64.encodebytes
base64.decodestring = base64.decodebytes
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.contrib import messages



# //////////////////////////////////////////////////////////

# Result Portal View 

def classes_view(request):
	queryset= Class.objects.all()
	context = {
		"classes": queryset,
    }
	return render(request, "Classes.html", context)
	
def students_view(request):
	try:
		Classname=str(request.POST.get('class'))
		queryset=Student.objects.filter(Class=Classname)
	# queryset3=Assignments.objects.filter(Class=id)
		queryset2=Class.objects.get(Class=Classname)
		context = {
			"students": queryset,
			"class":queryset2,
			# "Assignments":queryset3,
    	}
		return render(request, "Students.html", context)
	
	except:
		messages.error(request, 'please Select your Class or Check the Class you Selected') 
		queryset= Class.objects.all()
		context = {
		"classes": queryset,
    	}
	return render(request, "Classes.html", context)

	
def result_view(request,Classname):

	# get the Student name from the inpue
	stu=str(request.POST.get('Name'))

	# Convert the name coming from the input to uppercase /////////
	studentname=stu.upper().strip()

	# get Class name ////////////////////////////////
	Student_class=Class.objects.get(Class=Classname)

	# to get back all the students list if submission fails ///////////////
	Students_list=Student.objects.filter(Class=Classname)

	# Termly Queryset details & Results ////////
	Student_Results=Result.objects.filter(Name=studentname,Class=Classname)
	Student_details=get_object_or_404(Student,Name=studentname)

	# Annual Results //////////////////////////////////////////////////////
	# queryset2=AnnualStudent.objects.filter(Class=Classname)
	# stuff2=get_object_or_404(AnnualStudent,Name=studentname)
	# queryset5=AnnualResult.objects.filter(Name=studentname,Class=Classname)

	# for the Bar Chart and the Pie Chart /////////////////////////////////
	labels=[]
	data=[]
	for result in Student_Results:
		labels.append(result.Subject)
		data.append(result.Total)
	# Newsletter 
	letter=Newsletter.objects.all()
	if request.method=='POST':
		try:
			enteredpin=request.POST.get('Pin')
			mainpin=int(enteredpin)
			studentpin=get_object_or_404(Students_Pin_and_ID,student_name=studentname)
			if mainpin == studentpin.student_pin:
				context={
					"Student":Student_details,
					"Result":Student_Results,
					"labels":labels,
					"data":data,
					# "AnnualStudent":stuff2,				
					# 'AnnualResult': queryset5,
					'letter':letter,
					}
				return render(request,"Result.html", context)
			else:
				messages.error(request, 'Invalid card pin , check your input and try again') 
				context = {
					"students": Students_list,
					"class":Student_class
					}
				return render(request, "Students.html", context)
		except:
			messages.error(request, 'name mismatched in the database, contact the number in your Card') 
			context = {
				"students": Students_list,
				"class":Student_class
			}
			return render(request, "Students.html", context)
		
def result_pdf_view(request,Name,Classname):
	stuff=get_object_or_404(Student,Name=Name)
	stuff2=get_object_or_404(AnnualStudent,Name=Name)
	queryset4=Result.objects.filter(Name=Name,Class=Classname)
	queryset5=AnnualResult.objects.filter(Name=Name,Class=Classname)
	school=School.objects.all()
	letter=Newsletter.objects.all()
	template_path ='Result_pdf.html'
	context={
		"AnnualStudent":stuff2,
		"Student":stuff,
		"Result":queryset4,
		'schoollogo': school,
		'letter':letter,
		'AnnualResult': queryset5,
		}
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment'; filename="Result.pdf"
	template = get_template(template_path)
	html = template.render(context)
	pisa_status = pisa.CreatePDF(
		html, dest=response)
	if pisa_status.err:
		return HttpResponse('We had some errors <pre>' + html + '</pre>')
	return response

# /////////////////////////////////////////////////////////

# Result Admin Side Views

def activation_view(request):
	context = {
		}
	return render(request, "activation.html", context)
	
def createPin(request):
	student=Excelfiles()
	student.readPin()
	context = {
		}
	return render(request, "pins.html", context)

# //////////////////////////////////////////////////////////

# Create Junior Students Termly Results Details

# Jss1 //
def createjuniorstudent1_view(request):
	student=Excelfiles()
	student.createJuniorStudent1()
	context = {
		}
	return render(request, "Congratulation.html", context)
# Jss2 //
def createjuniorstudent2_view(request):
	student=Excelfiles()
	student.createJuniorStudent2()
	context = {
		}
	return render(request, "Congratulation.html", context)
# Jss3 //
def createjuniorstudent3_view(request):
	student=Excelfiles()
	student.createJuniorStudent3()
	context = {
		}
	return render(request, "Congratulation.html", context)

# ////////////////////////////////////////////////////////////

# create Junior Students Termly Results

# Jss1 //
def createjuniorresult1_view(request):
	result=Student()
	result.createJuniorResult1()
	context = {
		}
	return render(request, "Congratulation.html", context)
# Jss2//
def createjuniorresult2_view(request):
	result=Student()
	result.createJuniorResult2()
	context = {
		}
	return render(request, "Congratulation.html", context)
# Jss3 //
def createjuniorresult3_view(request):
	result=Student()
	result.createJuniorResult3()
	context = {
		}
	return render(request, "Congratulation.html", context)

# ////////////////////////////////////////////////////////////

# Create Junior Student's Annual Details

# Jss1//
def createjuniorstudentAnnual1_view(request):
	student=Excelfiles()
	student.createJuniorStudentAnnual1()
	context = {
		}
	return render(request, "Congratulation.html", context)
# Jss2 //
def createjuniorstudentAnnual2_view(request):
	student=Excelfiles()
	student.createJuniorStudentAnnual2()
	context = {
		}
	return render(request, "Congratulation.html", context)
# Jss3 //
def createjuniorstudentAnnual3_view(request):
	student=Excelfiles()
	student.createJuniorStudentAnnual3()
	context = {
		}
	return render(request, "Congratulation.html", context)

# ////////////////////////////////////////////////////////////

# create Junior Annual Results

# Jss1 //
def createjuniorresultAnnual1_view(request):
	result=AnnualStudent()
	result.createJuniorAnnual1()
	context = {
		}
	return render(request, "Congratulation.html", context)
# Jss2 //
def createjuniorresultAnnual2_view(request):
	result=AnnualStudent()
	result.createJuniorAnnual2()
	context = {
		}
	return render(request, "Congratulation.html", context)
# Jss3 //
def createjuniorresultAnnual3_view(request):
	result=AnnualStudent()
	result.createJuniorAnnual3()
	context = {
		}
	return render(request, "Congratulation.html", context)

# /////////////////////////////////////////////////////////////

# Termly Senior Students details

# SS1 //
def createseniorstudent1_view(request):
	student=Excelfiles()
	student.createSeniorStudents1()
	context = {
	 }
	return render(request, "Congratulation.html", context)
# SS2 //
def createseniorstudent2_view(request):
	student=Excelfiles()
	student.createSeniorStudents2()
	context = {
	 }
	return render(request, "Congratulation.html", context)
# SS3 //  
def createseniorstudent3_view(request):
	student=Excelfiles()
	student.createSeniorStudents3()
	context = {
	 }
	return render(request, "Congratulation.html", context)

# ////////////////////////////////////////////////////////////////

# Termly Senior Students Result

# SS1 //
def createseniorresult1_view(request):
	result=Student()
	result.createSeniorResult1()
	context = {
		}
	return render(request, "Congratulation.html", context)
# SS2 //
def createseniorresult2_view(request):
	result=Student()
	result.createSeniorResult2()
	context = {
		}
	return render(request, "Congratulation.html", context)  
# SS3 //
def createseniorresult3_view(request):
	result=Student()
	result.createSeniorResult3()
	context = {
		}
	return render(request, "Congratulation.html", context)

# ////////////////////////////////////////////////////////////////


# Annual Senior Students Result details  

# SS1 //
def createseniorstudentAnnual1_view(request):
	student=Excelfiles()
	student.createSeniorStudentsAnnual1()
	context = {
	 }
	return render(request, "Congratulation.html", context)
# SS2 //
def createseniorstudentAnnual2_view(request):
	student=Excelfiles()
	student.createSeniorStudentsAnnual2()
	context = {
	 }
	return render(request, "Congratulation.html", context)
# SS3 //
def createseniorstudentAnnual3_view(request):
	student=Excelfiles()
	student.createSeniorStudentsAnnual3()
	context = {
	 }
	return render(request, "Congratulation.html", context)    


# ////////////////////////////////////////////////////////////////////

# Annual Senior Students Result 

# SS1//

def createseniorresultAnnual1_view(request):
	result=AnnualStudent()
	result.createSeniorAnnual1()
	context = {
		}
	return render(request, "Congratulation.html", context)
# SS2 //
def createseniorresultAnnual2_view(request):
	result=AnnualStudent()
	result.createSeniorAnnual2()
	context = {
		}
	return render(request, "Congratulation.html", context)
# SS3 //
def createseniorresultAnnual3_view(request):
	result=AnnualStudent()
	result.createSeniorAnnual3()
	context = {
		}
	return render(request, "Congratulation.html", context)


# //////////////////////////////////////////////////////////////////////////
	

