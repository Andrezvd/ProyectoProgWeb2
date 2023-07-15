from django import forms
from .models import Expancion


class ExpancionForm(forms.ModelForm):
    """
    Formulario para facilitar la creación y edición de productos.
    """

    class Meta: 
        #Espeficiar a que modelo está asociado el formulario
        model = Expancion

        fields = [
            'nombre',
            'descripcion',
            'precio',
            'imagen'
        ]

        labels = {
            'nombre':'Nombre',
            'descripcion':'Descripción',
            'precio':'Precio',
            'imagen':'Imagen'
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control','rows':3}),
            'precio':forms.NumberInput(attrs={'class':'form-control'}),
            'imagen':forms.FileInput(attrs={'class':'form-control'})
        }
    
    def __init__(self, *args, **kwargs):
        super(ExpancionForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].error_messages = {'required': 'custom required message'}

        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required':'El campo {fieldname} es obligatorio'.format(
                fieldname=field.label)}