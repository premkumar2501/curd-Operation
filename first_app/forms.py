# from wtforms import Form,StringField,TextAreaField
# from wtforms.validators import DataRequired

# class Phone(Form):
#     phone_name=StringField('phone_name',validators=[DataRequired()])
#     company_name=StringField('company_name',validators=[DataRequired()])
#     color=StringField('color',validators=[DataRequired()])
#     feedback=TextAreaField('feedback',validators=[DataRequired()])




# from wtforms import Form,StringField,IntegerField
# from wtforms.validators import DataRequired

# class My_data(Form):
#     My_name=StringField('name',validators=[DataRequired()])
#     My_cell=IntegerField('cell',validators=[DataRequired()])
#     Gender=StringField('gender',validators=[DataRequired()])
#     Date_of_birth=IntegerField('DOB',validators=[DataRequired()])




# from django.forms import ModelForm,TextInput
# from .models import City

# class CityForm(ModelForm):
#     class Meta:
#         model = City
#         fields = ['name']
#         widgets = {'name':TextInput(attrs={
#             'class':'form-control','placeholder':'City Name'
#         })}