from django.views.generic import ListView
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = 'core/home.html'
    profie ="Немецкие команды"

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'profie': self.profie
        })
        return context

















    # def HomeView(request):
    #     model = Post
    #     data = {
    #         'new_field': 'Главная страница',
    #     }
    #     return render(request, 'core/home.html', data)








