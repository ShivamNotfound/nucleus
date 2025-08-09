from django.forms import ModelForm,DateInput
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=['name','scheduled_date','description','default']
        widgets={'scheduled_date':DateInput(attrs={'type':'date'})}
        labels={'name':'Task'}