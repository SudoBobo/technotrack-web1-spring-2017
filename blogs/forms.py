from django import forms
from blogs.models import Blog


class FilterForm(forms.Form):
    sort = forms.ChoiceField(choices=(
        ('title', 'Заголовок'),
        ('description', 'Описание')
    ), label='Сортировать по', required=False)

    search = forms.CharField(max_length=255, label='Поиск', required=False)


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'category')


class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'category')
