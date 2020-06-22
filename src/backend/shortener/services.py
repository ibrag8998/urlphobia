from typing import Dict
from urllib.parse import urlparse

from django.shortcuts import get_object_or_404, redirect
# from django.http import Http404

from .forms import URLForm
from .models import URL


class IndexService:
    def handle_form_valid(self, form: URLForm):
        queried_url_object = URL.objects.filter(
            destination=form.cleaned_data['destination'])

        if queried_url_object.exists():
            return redirect(queried_url_object[0])


class InfoService:
    def __init__(self, url_object: URL) -> None:
        self.object = url_object

    def modify_context(self, context: Dict):
        context['short'] = self.short
        context['destination_trunc'] = self.destination_trunc
        return context

    @property
    def short(self):
        return f'localhost:8000/{self.object.slug}'

    @property
    def destination_trunc(self):
        raw_url = urlparse(self.object.destination)
        return f'{raw_url.scheme}://{raw_url.netloc}/...'


class RedirectionService:
    def get_redirect_url(self, slug, *args, **kwargs):
        return get_object_or_404(URL, slug=slug).destination
