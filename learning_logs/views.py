from django.shortcuts import render, redirect 
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
	"""Домашняя страница Learning Log"""
	return render(request, 'learning_logs/index.html')
def topics(request):
	"""Выводит список тем """
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)
def topic(request , topic_id):
	"""Выводит одну тему и все её записи"""
	topic = Topic.objects.get(id = topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic , 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)
def new_topic(request):
	"""Определяет новую тему """
	if request.method != 'POST':#Проверка на запрос
		#Данные не отпровлялись; создается новая форма
		form = TopicForm()
	else:
		#отпровлять данные POST;Отображать данные
		form = TopicForm(data=request.POST)
		if form.is_valid():#функция is_valid проверяет, что все обяз поля были заполнены 
			form.save()#сохранение в БД
			return redirect('learning_logs:topics')#перенапровляет
	#Вывести пустую или не действительную форму
	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request , topic_id):
	"""Добовляет новую запись по конкретной теме"""
	topic = Topic.objects.get(id = topic_id)

	if request.method != 'POST':#Проверка на запрос
		#Данные не отпровлялись; создается новая форма
		form = EntryForm()
	else:
		#отпровлять данные POST;Отображать данные
		form = EntryForm(data=request.POST)
		if form.is_valid():#функция is_valid проверяет, что все обяз поля были заполнены 
			new_entry = form.save(commit = False)#сохранение в БД
			new_entry.topic = topic
			new_entry.save()
			return redirect('learning_logs:topic', topic_id = topic_id)#перенапровляет два аргумента:
			#имя представления, которому передается управление 
			#аргумент для функции представления 
	#Вывести пустую или не действительную форму
	context = {'topic': topic , 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
	"""Редактирование существующей записи"""
	entry = Entry.objects.get(id = entry_id)
	topic = entry.topic

	if request.method != 'POST':#Проверка на запрос
		#Исходный запрос;форма заполняется данными текущей записи 
		form = EntryForm(instance = entry)
	else:
		#отпровлять данные POST;Отображать данные
		form = EntryForm(instance = entry, data=request.POST)#говорит создать экземпляр на основании информ сущ объекта записи 
		if form.is_valid():#функция is_valid проверяет, что все обяз поля были заполнены 
			form.save()
			return redirect('learning_logs:topic', topic_id = topic.id)#перенапровляет два аргумента:
			#имя представления, которому передается управление 
			#аргумент для функции представления 
	#Вывести пустую или не действительную форму
	context = {'entry':entry, 'topic': topic , 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context) 