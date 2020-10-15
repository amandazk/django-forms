from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime

class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today) #a pessoa pode ver o campo, mas não pode alterá-lo
    TIPOS_DE_CLASSE = {
        (1, 'Econômica'),
        (2, 'Executiva'),
        (3, 'Primeira classe'),
    }
    classe_viagem = forms.ChoiceField(label='Classe da viagem', choices=TIPOS_DE_CLASSE)
    informacoes = forms.CharField(
        label='Informações extras',
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label='Email', max_length=150)

    def clean_origem(self):
        origem = self.cleaned_data.get('origem')
        if any(char.isdigit() for char in origem):
            raise forms.ValidationError('Origem inválida: Não inclua números')
        else:
            return origem