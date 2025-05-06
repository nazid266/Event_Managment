from django import forms 
from events.models import Event,Category,Participant

class EventModelForm(forms.ModelForm):
    class Meta:
       model=Event
       fields=['name','description','date','time','location','category']
       widgets={
             
            'name': forms.TextInput(attrs={
                "class": "border-2 border-rose-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
            }),
            'description': forms.Textarea(attrs={
                "class": "border-2 border-rose-300 w-full h-40 p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
            }),
            'date': forms.SelectDateWidget(attrs={'class':'rounded-md p-1'}), 
            'time': forms.TimeInput(attrs={'type': 'time' ,'class':"mt-2 rounded-md"}),
            'location': forms.TextInput(attrs={
                "class": "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-blue-500 focus:ring-blue-500"
            }),
            'category': forms.Select()
        
       }
       
       
class CategoryModelForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name','description']
        widgets={
            'name':forms.TextInput(attrs={"class": "border-2 border-rose-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
            }),
            'description':forms.Textarea(attrs={"class": "border-2 border-rose-300 w-full h-40 p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
            })
        }
        
class ParticipantModelForm(forms.ModelForm):
    class Meta:
        model=Participant
        fields=['name','email','assinged_to']
        widgets={
            'name':forms.TextInput(attrs={"class": "border-2 border-rose-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
            }),
            'email':forms.TextInput(attrs={"class": "border-2 border-rose-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
            }),
            'assinged_to':forms.CheckboxSelectMultiple()
        }