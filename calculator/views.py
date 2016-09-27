from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from calculator.forms import BreastForm

# Create your views here.

@login_required(login_url="/")
def form(request):

	# Coefficients
	coefficients = { 
	'race' : 0.0004,
	'vitalStatusRecord' : -4.6421,
	'grade' : 0.0186,
	'maritalStatus' : -0.0305 ,
	'histologicType' : 0.0009,
	'behaviorCode' : -0.9735,
	'csExtension' : -0.0091,
	'csLymphNode' : -0.0012 ,
	'radiation' : -0.0175,
	'seerHistoricStageA' : -0.7942,
	'ageAtDiognosis' : 0.0274,
	'csTumorSize' : -0.0010,
	'regionalNodesPositive' : -0.0066,
	'regionalNodesExamined' : -0.0001,
	'survivalMonths' : 1	
	}
	# Intercept
	intercept = 12.76321543

	form = BreastForm(request.POST or None)
	# form = BreastForm()

	if request.method == 'POST':

		form = BreastForm(request.POST)

		if form.is_valid():	

			# Calculate the result
			result = 0
			for i in request.POST:
				if i != 'csrfmiddlewaretoken':
					# print(coefficients[i]* int(request.POST.get(i)))
					result = result + (coefficients[i] * int(request.POST.get(i)))
					
			result = result + intercept

			save_it = form.save(commit=False)
			save_it.result = result
			save_it.save()

			# return render(request, 'myapp/register.html', 
			# 	{'form' : form, 'result' : request.POST}
			# )
			# return HttpResponseRedirect('/myapp/breast/%d' %result)
			return redirect('result', 166)


	return render(request, 'calculator/form.html', 
		{'form' : form, 'result' : 0}
		)


@login_required(login_url="/")
def result(request, ids):

	# values = Breast.objects.all()
	# df = read_frame(values)
	# dic = add(df)

	TokyoData = [17.0, 17.0, 9.5, 14.5, 18.2, 17.0, 17.0, 17.0, 17.0, 18.3, 13.9, 9.6]
	yTitle = 'Temprature'


	return render(request, 'calculator/result.html', 
		{
		'values' : 1, 'dic' : 0, 'TokyoData' : TokyoData, 'yTitle' : yTitle, 'result' : ids
			})

@login_required(login_url="/")
def chart(request):

	return render(request, 'navbar.html')