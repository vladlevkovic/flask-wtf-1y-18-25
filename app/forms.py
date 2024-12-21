from flask_wtf import FlaskForm
import wtforms

class SubscribeForm(FlaskForm):
    name = wtforms.StringField('Name')
    email = wtforms.EmailField('Email')
    submit = wtforms.SubmitField('Subscribe')


class IceCreamForm(FlaskForm):
    tastes = wtforms.SelectField('Смак')
    topping = wtforms.SelectMultipleField('Топінг')
    cup_size = wtforms.RadioField('Стаканчик')
    submit = wtforms.SubmitField('Замовити')
