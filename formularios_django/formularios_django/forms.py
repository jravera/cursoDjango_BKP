from django import forms
    


class CommentForm(forms.Form):
    name = forms.CharField(max_length=100, 
                           required=True, 
                           label="Nombre:",
                           help_text='100 caracteres maximo',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu nombre'})  
                           )
    url   = forms.URLField(label='Tu sitio web', 
                           required=False
                           )
    comment = forms.CharField()