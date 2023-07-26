from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Personaje
from django.contrib.auth import get_user_model
User = get_user_model()


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    def save(self, commit=True):
        user = super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit :
            user.save()
        return user


class crearPersonajeForm(forms.ModelForm):

    class Meta: 
        #Espeficiar a que modelo está asociado el formulario
        model = Personaje

        fields = [
            'nombre',
            'nivel',
            'clase',
            'especializacion',
            'imagen',
            'imagen3d'
        ]

        labels = {
            'nombre':'Nombre',
            'nivel':'Nivel',
            'clase':'Clase',
            'especializacion':'Especializacion',
            'imagen':'Imagen',
        }

        widgets = {
            'nombre':forms.Select(attrs={'class':'form-control'}),
            'nivel':forms.TextInput(attrs={'class':'form-control'}),
            'clase':forms.TextInput(attrs={'class':'form-control'}),
            'especializacion':forms.TextInput(attrs={'class':'form-control'}),
            'imagen':forms.FileInput(attrs={'class':'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(crearPersonajeForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].error_messages = {'required': 'custom required message'}

        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required':'El campo {fieldname} es obligatorio'.format(
                fieldname=field.label)}