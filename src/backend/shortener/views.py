from django.views.generic import CreateView, RedirectView, DetailView

from .models import URL
from .services import IndexService, RedirectionService, InfoService
from .forms import URLForm


class IndexView(CreateView):
    template_name = 'index.html'
    template_name_suffix = ''
    form_class = URLForm

    index_service = IndexService()

    def form_valid(self, form: URLForm):
        return self.index_service.handle_form_valid(
            form) or super().form_valid(form)


class InfoView(DetailView):
    model = URL
    template_name = 'info.html'
    context_object_name = 'url'

    # An `InfoService` instance is used in `get_context_data`, but line below
    # is commented out because instance is being created only in one place and
    # with using `self.object`

    # info_service: InfoService

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return InfoService(self.object).modify_context(context)


class RedirectionView(RedirectView):
    redirection_service = RedirectionService()

    def get_redirect_url(self, *args, **kwargs):
        return self.redirection_service.get_redirect_url(*args, **kwargs)
