from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    """
    Formulario para facilitar la creación y edición de productos.
    """

    class Meta: 
        #Espeficiar a que modelo está asociado el formulario
        model = Producto

        fields = [
            'ref_especializacion',
            'ref_estado',
            'nombre',
            'nivel',
            'ilevel',
            'dps',
            'dañofisico',
            'dañomagico', 
            'vataque', 
            'stadistica1',
            'stadistica2',
            'descripcion',
            'caracteristicas',
            'precio',
            'imagen'
        ]

        labels = {
            'ref_especializacion':'Especializacion',
            'ref_estado':'Estado',
            'nombre':'Nombre',
            'nivel':'Nivel',
            'ilevel':'ItemLevel',
            'dps':'Dps',
            'dañofisico':'Daño',
            'dañomagico':'DañoMagico', 
            'vataque':'VelocidadAtaque', 
            'stadistica1':'Stat1',
            'stadistica2':'Stat2',
            'descripcion':'Descripción',
            'caracteristicas':'Caracteristicas',
            'precio':'Precio',
            'imagen':'Imagen'
        }

        widgets = {
            'ref_categoria':forms.Select(attrs={'class':'form-control'}),
            'ref_estado':forms.Select(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'nivel':forms.TextInput(attrs={'class':'form-control'}),
            'ilevel':forms.TextInput(attrs={'class':'form-control'}),
            'dps':forms.TextInput(attrs={'class':'form-control'}),
            'dañofisico':forms.TextInput(attrs={'class':'form-control'}),
            'dañomagico':forms.TextInput(attrs={'class':'form-control'}),
            'vataque':forms.TextInput(attrs={'class':'form-control'}),
            'stadistica1':forms.TextInput(attrs={'class':'form-control'}),
            'stadistica2':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control','rows':3}),
            'caracteristicas':forms.Textarea(attrs={'class':'form-control','rows':3}),
            'precio':forms.NumberInput(attrs={'class':'form-control'}),
            'imagen':forms.FileInput(attrs={'class':'form-control'})
        }
    
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].error_messages = {'required': 'custom required message'}

        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required':'El campo {fieldname} es obligatorio'.format(
                fieldname=field.label)}