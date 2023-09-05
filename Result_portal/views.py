from django.shortcuts import render
from .models import *
import base64
base64.encodestring = base64.encodebytes
base64.decodestring = base64.decodebytes
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse

# get students for each Class

def get_Students(request, Classname):
    Students = Students_Pin_and_ID.objects.filter(student_class=Classname)
    Students_list = list(Students.values('id', 'student_name'))
    return JsonResponse(Students_list, safe=False)

# Result Portal View 
def Result_Portal_view(request):
	classes=Class.objects.all()
	if request.method == 'POST':
	# get the Student name from the inque
		student_name=str(request.POST['student_name'])
		student_id=str(request.POST['student_id'])
		Pin=str(request.POST['student_pin'])
		labels=[]
		data=[]
		Annual_Result=False
		# Get the Student details, the Students_Result_Details and the Results (Both Annual & Termly )
		try:
			student = Students_Pin_and_ID.objects.get(student_name=student_name,student_id=student_id,student_pin=Pin)
			if Student.objects.filter(student_name=student_name,Student_id=student_id).exists():
				Student_Result_details=Student.objects.get(student_name=student_name,Student_id=student_id)
				Student_Results=Result.objects.filter(student_name=student_name,Student_id=student_id)
				for result in Student_Results:
					labels.append(result.Subject)
					data.append(result.Total)
					
				if AnnualStudent.objects.filter(student_name=student_name,Student_id=student_id).exists():
					Annual_Result=True
					Annual_Student_Result_details=AnnualStudent.objects.get(student_name=student_name,Student_id=student_id)
					Annual_Student_Results=AnnualResult.objects.filter(student_name=student_name,Student_id=student_id)
					PromotionVerdict=int(float(Annual_Student_Result_details.Average))
					context={
						"student_details":student,
						"Result_details":Student_Result_details,
						"Results":Student_Results,
						"labels":labels,
						"data":data,
						"AnnualStudent":Annual_Student_Result_details,
						'AnnualResult': Annual_Student_Results,
						"Annual_Result":Annual_Result,
						"PromotionVerdict":PromotionVerdict,
						}
					return render(request,"Result.html", context)
				else:
					Annual_Result=False	
					context={
						"Annual_Result":Annual_Result,
						"student_details":student,
						"Result_details":Student_Result_details,
						"Results":Student_Results,
						"labels":labels,
						"data":data,
								}
					return render(request,"Result.html", context)
			else:
				return render(request,"404.html")

		except Students_Pin_and_ID.DoesNotExist:
			# Display an error message if the student does not exist
			classes=Class.objects.all()
			context={
				"classes":classes,
			}
			messages.error(request, 'Check your Student id or the Pin and try again , make sure you are entering it Correctly')
			return render(request, "Result_Portal.html",context)
	else:
		context={
			"classes":classes
		}
		return render(request, "Result_Portal.html",context)
	



		
# //////////////////////////////////////////////////////////
	
# def createPin(request):
# 	student=Excelfiles()
# 	student.readPin()
# 	context = {
# 		}
# 	return render(request, "pins.html", context)

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
	

