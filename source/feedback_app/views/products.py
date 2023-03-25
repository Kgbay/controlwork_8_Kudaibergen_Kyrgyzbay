from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from feedback_app.forms import ProductForm
from feedback_app.models import Product


class ProductDetail(DetailView):
    template_name = 'product.html'
    model = Product


class GroupPermissionMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.groups.filter(name__in=['moderator']).exists()


class ProductCreateView(GroupPermissionMixin, SuccessMessageMixin, CreateView):
    template_name = 'product_create.html'
    model = Product
    form_class = ProductForm
    success_message = 'Товар создан'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView, ):
    template_name = 'product_update.html'
    form_class = ProductForm
    model = Product
    success_message = 'Товар обновлен'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(GroupPermissionMixin, SuccessMessageMixin, DeleteView, ):
    template_name = 'product_confirm_remove.html'
    model = Product
    success_url = reverse_lazy('index')
    success_message = 'Задача удалена'
