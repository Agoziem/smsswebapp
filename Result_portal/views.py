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
	classobject=Class.objects.get(Class=Classname)
	Students = Students_Pin_and_ID.objects.filter(student_class=classobject)
	Students_list = list(Students.values('id', 'student_name'))
	return JsonResponse(Students_list, safe=False)

# Result Portal View 
def Result_Portal_view(request):
	classes=Class.objects.all()
	Terms=Term.objects.all()
	if request.method == 'POST':
	# get the Student name from the request
		student_name=str(request.POST['student_name'])
		student_id=str(request.POST['student_id'])
		Pin=str(request.POST['student_pin'])
		term = request.POST['Term']
		labels=[]
		data=[]
		Annual_Result=False
		# Get the Student details, the Students_Result_Details and the Results (Both Annual & Termly )
		try:
			resultTerm=Term.objects.get(term=term)
			student = Students_Pin_and_ID.objects.get(student_name=student_name,student_id=student_id,student_pin=Pin)
			if Student_Result_Data.objects.filter(student_name=student,Term=resultTerm).exists():
				Student_Result_details=Student_Result_Data.objects.get(student_name=student,Term=resultTerm)
				Student_Results=Result.objects.filter(student=student,students_result_summary=Student_Result_details)
				for result in Student_Results:
					labels.append(result.Subject)
					data.append(result.Total)
					
				if AnnualStudent.objects.filter(student_name=student).exists():
					Annual_Result=True
					Annual_Student_Result_details=AnnualStudent.objects.get(student_name=student)
					Annual_Student_Results=AnnualResult.objects.filter(student_name=Annual_Student_Result_details)
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
			"classes":classes,
			"Terms":Terms
		}
		return render(request, "Result_Portal.html",context)
	

