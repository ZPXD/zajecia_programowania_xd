from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import pandas as pd

class X(FlaskForm):
    wykonawca = StringField('Wykonawca:', validators=[DataRequired()])
    utwor = StringField('Utwór:', validators=[DataRequired()])
    kto = StringField('Kto dodaje:',validators=[DataRequired()], default='Anonim')
    #date = datetime.now(tz=None)
    button = SubmitField('Prześlij')

def save_data(string):
    
    '''df = pd.DataFrame(data_lst)
    df.to_csv("dane/form_data.csv", index=False, mode='a', header=False)'''

    with open('dane/form_data.csv','a') as fd:
        fd.write(string)