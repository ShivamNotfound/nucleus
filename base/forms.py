from django.forms import ModelForm,DateInput,IntegerField
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=['name','scheduled_date','description','default',"priority_level","urgency_level"]
        widgets={'scheduled_date':DateInput(attrs={'type':'date'})}
        labels={'name':'Task','default':'Repeat daily'}
    priority_level=IntegerField(min_value=1,max_value=3)
    urgency_level=IntegerField(min_value=1,max_value=3)
