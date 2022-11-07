from django.views.generic import TemplateView


class SuccessView(TemplateView):
    template_name = "feedback/feed_back_success.html"
