from django import forms

class ApprovalForm(forms.Form):
	Firstname=forms.CharField(max_length=150,widget=forms.TextInput(attrs={'placeholder':'Enter Firstname'}))
	Lastname=forms.CharField(max_length=150,widget=forms.TextInput(attrs={'placeholder':'Enter Lastname'}))
	Dependents=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter Number of Dependents'}))
	ApplicantIncome=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter Monthly Gross Income'}))
	CoapplicantIncome=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter Co-Applicant Gross income'}))
	LoanAmount=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Request Loan Amount'}))
	Loan_Amount_Term=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Request Loan Terms'}))
	Credit_History=forms.ChoiceField(choices=[('0',0),('1',1),('2',2),('3',3)])
	Gender=forms.ChoiceField(choices=[('Male','Male'),('Female','Female')])
	Married=forms.ChoiceField(choices=[('Yes','Yes'),('No','No')])
	Education=forms.ChoiceField(choices=[('Graduate','Graduated'),('Not_Graduate','Not_Graduated')])
	Self_Employed=forms.ChoiceField(choices=[('Yes','Yes'),('No','No')])
	Property_Area=forms.ChoiceField(choices=[('Rural','Rural'),('Semiurban','Semiurban'),('Urban','Urban')])