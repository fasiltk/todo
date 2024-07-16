# from django import forms
# from .models import Task

# # iterable
# GEEKS_CHOICES = (
#     ("1", "Complete"),
#     ("2", "Not Complete"),
#     ("3", "Progress"),
# )

# class GeeksForm(forms.ModelForm):
#     status = forms.ChoiceField(choices=GEEKS_CHOICES)

#     class Meta:
#         model = Task
#         fields = ['name', 'title', 'description', 'duedate', 'status']


# from django import forms
# from .models import Task, Status

# # iterable
# GEEKS_CHOICES = (
#     (1, "Complete"),
#     (2, "Not Complete"),
#     (3, "Progress"),
# )

# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['name', 'title', 'description', 'duedate']

# class StatusForm(forms.ModelForm):
#     status = forms.ChoiceField(choices=GEEKS_CHOICES)
    
#     class Meta:
#         model = Status
#         fields = ['status']



from django import forms
from .models import Task, Status

# iterable
GEEKS_CHOICES = (
    (1, "Complete"),
    (2, "Not Complete"),
    (3, "Progress"),
)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'title', 'description', 'duedate']

class StatusForm(forms.ModelForm):
    status = forms.ChoiceField(choices=GEEKS_CHOICES)
    
    class Meta:
        model = Status
        fields = ['status']
