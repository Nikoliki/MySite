from django import forms
from .models import Topic, Entry 

class TopicForm(forms.ModelForm):#Определяем класс, наследующий от forms.ModelForm
	class  Meta:#вложенный класс, с параметрами 
		model = Topic #создается на базе модели Topic 
		fields = ['text']#размещ поле text 
		labels = {'text': ''}# не генерировать подпись для текстового поля

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': 'Entry:'}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}#80столбцов 
