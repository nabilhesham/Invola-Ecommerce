from django.shortcuts import render

from django.views.generic import RedirectView, UpdateView, ListView, TemplateView, CreateView, DetailView
from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url
from django.urls import reverse, reverse_lazy


class HomeView(TemplateView):
    template_name = "home.html"
    # bread_crumbs = [_("Inovola")]
    page_title = _("Home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["bread_crumbs"] = self.bread_crumbs
        context["page_title"] = self.page_title
        return context


class CoffeeMachineView(TemplateView):
    template_name = "pages/c_m.html"
    bread_crumbs = [_("Inovola"), _("Coffee Machine")]
    page_title = _("Coffee Machines")
    coffee_machine_api_url: url = reverse_lazy("api:coffee_machine_data")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bread_crumbs"] = self.bread_crumbs
        context["page_title"] = self.page_title
        context["coffee_machine_api_url"] = self.coffee_machine_api_url
        return context


class CoffeePodView(TemplateView):
    template_name = "pages/c_p.html"
    bread_crumbs = [_("Inovola"), _("Coffee Pod")]
    page_title = _("Coffee Pods")
    coffee_pod_api_url: url = reverse_lazy("api:coffee_pod_data")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bread_crumbs"] = self.bread_crumbs
        context["page_title"] = self.page_title
        context["coffee_pod_api_url"] = self.coffee_pod_api_url
        return context

