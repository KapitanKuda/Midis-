from django import forms
from .models import Review
from django.utils.translation import ugettext_lazy as _


#
# class ReviewsForm(forms.Form):
#     name = forms.CharField(max_length=150, label="Ваше имя*")
#     email = forms.EmailField(max_length=254,label="Email*")
#     site = forms.URLField(max_length=150,label="Ваш сайт",required=False)
#     body = forms.CharField(max_length=1000,label="Информация*")
#     pic = forms.ImageField(label="Изображение")
#     name.widget.attrs.update({'class':'form-control'})
#     body.widget.attrs.update({'class':'form-control'})
#     site.widget.attrs.update({'class':'form-control'})
#     email.widget.attrs.update({'class':'form-control'})
#     pic.widget.attrs.update({'class':'form-control'})

class ReviewsForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['name',
        'email',
        'site',
        'body',
        'img']
        labels = {
            'name': _('Имя'),
            'site': _('Сайт'),
            'body': _('Сообщение'),
            'img': _('Изображение')
        }
