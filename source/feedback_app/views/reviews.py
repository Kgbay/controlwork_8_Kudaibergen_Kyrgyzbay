from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from feedback_app.forms import ReviewForm
from feedback_app.models import Review


class ReviewDetail(DetailView):
    template_name = 'product.html'
    model = Review


class GroupPermissionMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.groups.filter(name__in=['moderator']).exists()


class TaskCreateView(GroupPermissionMixin, SuccessMessageMixin, CreateView):
    template_name = 'product_create.html'
    model = Review
    form_class = ReviewForm
    success_message = 'Товар создан'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class TaskUpdateView(GroupPermissionMixin, SuccessMessageMixin, UpdateView, ):
    template_name = 'product_update.html'
    form_class = ReviewForm
    model = Review
    success_message = 'Товар обновлен'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(GroupPermissionMixin, SuccessMessageMixin, DeleteView, ):
    template_name = 'product_confirm_remove.html'
    model = Review
    success_url = reverse_lazy('index')
    success_message = 'Задача удалена'
