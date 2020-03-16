from django import forms


class ContactForm(forms.Form):
    from_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "name-text", "placeholder": "Your Name"}
        ),
        max_length=50,
        required=True,
        label="",
    )
    from_email = forms.EmailField(
        widget=forms.TextInput(
            attrs={"class": "email-text", "placeholder": "Your Email"}
        ),
        required=True,
        label="",
    )
    category = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "class": "category",
                "placeholder": "Select Message Category",
            }
        ),
        choices=[(1, "General"), (2, "Fact"), (3, "Myth"), (4, "Prevention")],
        label="",
    )
    link = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "link-text", "placeholder": "Information Source"}
        ),
        max_length=5000,
        label="",
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "message", "placeholder": "Message"}
        ),
        required=True,
        label="",
    )
