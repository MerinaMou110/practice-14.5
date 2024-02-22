from django import forms
from django.forms.widgets import NumberInput
import datetime
from first_app.models import Student
# from .models import MyModel

BIRTH_YEAR_CHOICES = ['2022', '2023', '2024']

class contactForm(forms.Form):
    # name=forms.CharField(label="Enter your name")
    # email = forms.EmailField(label = "User Email")
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField(required=False)
    message = forms.CharField(
	max_length = 20,min_length=10
     )
    email_address = forms.EmailField( 
    label="Please enter  email address",
)
    first_name = forms.CharField(initial='Your name')
    You_agree= forms.BooleanField(initial=True)
    day = forms.DateField(initial=datetime.date.today)
    
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

   
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
   
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]   
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
    favorite_colors_multichoice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)

    # model_choice = forms.ModelChoiceField(
    #     queryset = MyModel.objects.all(),
    #     initial = 0
    #     )
    title = forms.CharField() 
    description = forms.CharField() 
    # field_name = forms.Field(**options)
    first_name = forms.CharField(max_length = 200)  
    last_name = forms.CharField(max_length = 200)  
    roll_number = forms.IntegerField(  
                     help_text = "Enter 6 digit roll number"
                     )  
    password = forms.CharField(widget = forms.PasswordInput())  




class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'name' : 'Student Name',
            'roll' : "Student Roll"
            
        }
        widgets  = {
            'name' : forms.TextInput(),
        }
        help_texts = {
            'name' : "Write your full name"
        }
        
        error_messages = {
            'name' : {'required' : 'Your name is required'}
        }



