from django import forms 
from events.models import Event,Category



class StyledFormMixin:
    
    def __init__(self,*args,**kwarg):
        super().__init__(*args,**kwarg)
        self.apply_style_widgets()
        
   
    defult_class="border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-gray-500 focus:ring-rose-500"
   
    def apply_style_widgets(self):
       for field_name,field in self.fields.items():
           if isinstance(field.widget,(forms.TextInput,forms.EmailInput,forms.PasswordInput)):
               field.widget.attrs.update(
                   {
                       "class":self.defult_class,
                       "placeholder":f"Enter Your {(field.label or field_name).lower()}"
                   }
               )
            
           elif isinstance(field.widget,(forms.Textarea)):
               field.widget.attrs.update(
                   {
                       "class":self.defult_class,
                       "placeholder":f"Enter Your {(field.label or field_name).lower()}"
                   }
               )
           elif isinstance(field.widget,(forms.SelectDateWidget)):
               field.widget.attrs.update(
                   {
                       "class":'rounded-md p-1',
                       "placeholder":f"Enter Your {(field.label or field_name).lower()}"
                   }
               )
               
           elif isinstance(field.widget,(forms.TimeInput)):
               field.widget.attrs.update(
                   {
                       "class":'mt-2 rounded-md',
                       "placeholder":f"Enter Your {(field.label or field_name).lower()}"
                   }
               )


class EventModelForm(StyledFormMixin,forms.ModelForm):
    class Meta:
       model=Event
       fields=['name','description','date','time','location','category','asset']
       '''widgets={
             
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
        
       }'''
       
      
        
class CategoryModelForm(StyledFormMixin,forms.ModelForm):
    class Meta:
        model=Category
        fields=['name','description']
        '''widgets={
            'name':forms.TextInput(attrs={"class": "border-2 border-rose-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
            }),
            'description':forms.Textarea(attrs={"class": "border-2 border-rose-300 w-full h-40 p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-500 focus:ring-rose-500"
            })
        }'''
        
