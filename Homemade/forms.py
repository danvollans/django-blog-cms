from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from Homemade.models import *


class AddPost(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddPost, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_class = 'blueForms'

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Posts


class AddPage(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddPage, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_class = 'blueForms'

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Pages


class AddTags(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddTags, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Tags