from django.forms import ModelForm

from ..chapter_3.models import Engine


class EngineForm(ModelForm):
    def __init__(self, *args, **kwargs):
        print('EngineForm Initialized')
        super(EngineForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Engine
        fields = '__all__'


class AddEngineForm(ModelForm):
    def __init__(self, *args, **kwargs):
        print('AddEngineForm Initialized')
        super(AddEngineForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Engine
        fields = '__all__'


class EngineSuperUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        print('EngineSuperUserForm Initialized')
        super(EngineSuperUserForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Engine
        fields = '__all__'
