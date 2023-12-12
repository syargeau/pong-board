from django import forms
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

from leaderboard.models import Match, Player

DUPLICATE_ERROR = 'Player has already been added with the same first and last name.'


class MatchForm(forms.ModelForm):
    """Form to submit a match result."""
    winner = forms.ModelChoiceField(queryset=Player.objects.order_by('first_name'))
    loser = forms.ModelChoiceField(queryset=Player.objects.order_by('first_name'))

    def __init__(self, *args, **kwargs):
        """Initialize form with initial winning score of 7."""
        super().__init__(*args, **kwargs)
        self.min_score = 7    
        self.fields['winning_score'].initial = self.min_score

    class Meta():
        model = Match
        fields = ['winner', 'winning_score', 'loser', 'losing_score']
        widgets = {
            'winning_score': forms.NumberInput(attrs={'min': 7}),
            'losing_score': forms.NumberInput(attrs={'min': 0}),
        }

    def clean(self):
        """Validate winning and losing scores."""
        cleaned_data = super().clean()
        winning_score = cleaned_data.get('winning_score')
        losing_score = cleaned_data.get('losing_score')
        winner = cleaned_data.get('winner')
        loser = cleaned_data.get('loser')
        if winner == loser:
            raise ValidationError('The winner and loser must be different players.')
        if winning_score < self.min_score:
            raise ValidationError('Winning score must be ' + self.min_score + ' or greater.')
        if losing_score < 0:
            raise ValidationError('Losing score must be 0 or greater.')
        if winning_score - losing_score < 2:
            raise ValidationError(
                'Losing score must be less than the winning score by at least 2 points.'
            )
        if winning_score > self.min_score and winning_score - losing_score != 2:
            raise ValidationError(
                'Deuce game! Winner must win by exactly 2 points when above ' + self.min_score + '.'
            )


class PlayerForm(forms.ModelForm):
    """Form to add a new player."""
    
    class Meta:
        model = Player
        fields = ['first_name', 'last_name']
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': DUPLICATE_ERROR,
            }
        }
    
    def clean_first_name(self):
        """Capitalize first name."""
        return self.cleaned_data.get('first_name').capitalize()

    def clean_last_name(self):
        """Capitalize last name."""
        return self.cleaned_data.get('last_name').capitalize()
