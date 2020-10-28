from django.forms import ModelForm, TextInput, EmailInput , Textarea
from.models import Messages
from django.forms.utils import ValidationError

class ValidationError(ValidationError):
    def __str__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return ''
        return  '<div claas="error-message">%s</div>'%''.join(['<p class="small error">%S</p>'%e for e in self])
class MessageForm( ModelForm):
    class Meta:
        model = Messages
        fields = ["name","email","subject","message"]
        widget = {
            'name': TextInput(attrs={
                'class': 'form-control',
                }),

            'email': EmailInput(attrs= {
                'class': 'form-conttrol'}),

            'subject': TextInput(attrs={
                'class': 'form-control'  }),

            'message': Textarea(attrs = {
                'class':'form-control'    })
        }