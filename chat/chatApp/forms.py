from django import forms
from .models import Chat
from emoji_picker.widgets import EmojiPickerTextInputAdmin


class ChatMessage(forms.ModelForm):
    class Meta:
       model = Chat
       fields = '__all__'
       widgets = {
            'content': EmojiPickerTextInputAdmin(),
        }
