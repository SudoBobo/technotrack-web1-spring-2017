from django import forms
from blogs.models import Blog, Category


class FilterForm(forms.Form):
    sort = forms.ChoiceField(choices=(
        ('title', 'Заголовок'),
        ('description', 'Описание')
    ), label='Сортировать по', required=False)

    search = forms.CharField(max_length=255, label='Поиск', required=False)


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description')

    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),
                                              widget=forms.TextInput(attrs={'class': "input-lg"}),
                                              )


# class AuthenticationForm(forms.Form):
#     username = forms.CharField(
#         max_length=254,
#         widget=forms.TextInput(attrs={'class': "input-lg"}),
#     )
#     password = forms.CharField(widget=forms.PasswordInput)


class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'category')
