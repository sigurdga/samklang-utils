import floppyforms as forms

class MarkdownTextarea(forms.Textarea):
    template_name = 'samklang_utils/markdown_textarea.html'

    class Media:
        js = ('js/wmd.js', 'js/flext.js')
        css = {
                'all': ('css/wmd.css',)
                }

    def get_context_data(self):
        self.attrs['class'] += " flext growme maxheight-500"
        return super(MarkdownTextarea, self).get_context_data()

class SharedToGroup(forms.MultiWidget):
    #template_name = 'samklang_utils/shared_to_group.html'

    def __init__(self, attrs=None):
        widgets = (forms.Checkbox, forms.Modelselect)
        super(SharedToGroup, self).__init__(widgets, attrs)

