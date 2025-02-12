from django import forms
from .models import Ticket, Review


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5}),
            'rating': forms.RadioSelect(choices=[(i, str(i)) for i in range(6)])
        }


class CombinedTicketReviewForm(forms.Form):
    # Ticket
    title = forms.CharField(max_length=128)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), required=False)
    image = forms.ImageField(required=False)

    # Review
    headline = forms.CharField(max_length=128)
    rating = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[(i, str(i)) for i in range(6)]
    )
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('description') and not cleaned_data.get('image'):
            raise forms.ValidationError(
                "You must provide either a description or an image for the ticket."
            )
        return cleaned_data
