from django.views.generic.edit import FormView
from feedback.forms.form_feedback import FeedBackForm


class FeedBackView(FormView):
    template_name = 'feedback/feed_back_form.html'
    form_class = FeedBackForm
    success_url = "/success/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
