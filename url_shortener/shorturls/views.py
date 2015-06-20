# coding: utf-8
from __future__ import absolute_import, unicode_literals

from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import RedirectView
from django.shortcuts import redirect

from .models import Link


class LinkCreate(CreateView):
    model = Link
    fields = ['url']

    def form_valid(self, form):
        prev = Link.objects.filter(url=form.instance.url)

        if prev:
            if self.request.user.id:
                prev[0].users.add(self.request.user)
                prev[0].save()

            return redirect('link_show', pk=prev[0].pk)

        if self.request.user.id:
            link_form = form.save()
            link_form.users.add(self.request.user)
            link_form.save()

        return super(LinkCreate, self).form_valid(form)


class LinkShow(DetailView):
    model = Link


class RedirectToLongURL(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        short_url = kwargs['short_url']

        return Link.expand(short_url)


class LinkList(ListView):
    model = Link

    def get_queryset(self):
        if self.request.user.id:
            return self.model._default_manager.filter(users=self.request.user)

        return super(LinkList, self).get_queryset()
