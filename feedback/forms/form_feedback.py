from django import forms
from feedback.tasks import send_email_feedback_task


class FeedBackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={"rows": 5})
    )

    def send_email(self):
        send_email_feedback_task.delay(
            self.cleaned_data["email"], self.cleaned_data["message"]
        )
