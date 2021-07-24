from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length = 50, required=True)
    message = forms.CharField(widget = forms.Textarea, required=True)
    email = forms.EmailField(max_length = 100, required=True)


    # def send_email(self):
    #     # send email using the self.cleaned_data dictionary

    #     message = """
    #     New message: {}
        
    #     from: {}
    #     """.format(fields['message'], fields['email'])
    #     send_mail(fields['subject'], message, "", ['fulonline1@gmail.com'])
