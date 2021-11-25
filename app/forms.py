from flask_wtf import FlaskForm
from wtforms import IntegerField, HiddenField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo


class MLRForm(FlaskForm):
    hdi = IntegerField('Human Development Index', validators=[DataRequired()])
    med_age = IntegerField('Median Age', validators=[DataRequired()])
    pop_den = IntegerField('Population Density', validators=[DataRequired()])
    death_count = HiddenField('Death Count')
    submit = SubmitField('Submit')
