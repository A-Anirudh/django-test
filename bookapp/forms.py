from django import forms
top_choices =(('general','General Enquiry'),('bug','Bug report'),('suggestion','Suggestion'))



class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=top_choices)
    message = forms.CharField(max_length=25)
    sender = forms.EmailField(required=False)



    