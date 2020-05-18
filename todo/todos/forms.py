from django import forms

from .models import Tag, Todo


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('order', 'name',)


class TodoForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Todo
        fields = ('content', 'tags',)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.request.user
        if commit:
            instance.save()
            self.save_m2m()
        return instance
