from django.db import models

# Create your models here.
class Topic(models.Model):#класс наследующий от Model-родительского класса  который определяет базовую функциональность модели 
	"""Тема, которую изучает пользоваель"""
	text = models.CharField(max_length = 200)#Тут объявление двух атрибутов, в этом указываеться длина символов сколько понад
	date_added = models.DateTimeField(auto_now_add = True)
class Entry(models.Model):
	"""Информация, изученная аользователем по теме"""
	topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)#Временная метка 

	class Meta:#Вкладывается в класс Entry
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Возврощает строковое представление модели"""
		if self.text[:50] > self.text[:0]:#условие 
			return f"{self.text[:50]}"#Сообщаем DjANGO выводить только 50 символов
		else:
			return f"{self.text[:50]}..."
		#18.2