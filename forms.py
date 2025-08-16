from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, DateField
from wtforms.validators import DataRequired, NumberRange, Length, Optional
from datetime import datetime

class DebtForm(FlaskForm):
    creditor = StringField('Nama Toko/Pemberi Hutang', 
                          validators=[DataRequired(message="Nama toko wajib diisi"), 
                                    Length(min=1, max=100, message="Nama toko harus antara 1 dan 100 karakter")])
    
    debtor_name = StringField('Nama Orang yang Berhutang', 
                             validators=[DataRequired(message="Nama orang yang berhutang wajib diisi"), 
                                       Length(min=1, max=100, message="Nama harus antara 1 dan 100 karakter")])
    
    amount = IntegerField('Jumlah Hutang (Rp)', 
                         validators=[DataRequired(message="Jumlah wajib diisi"), 
                                   NumberRange(min=1000, message="Jumlah harus minimal Rp 1.000")])
    
    description = TextAreaField('Deskripsi', 
                               validators=[Optional(), 
                                         Length(max=500, message="Deskripsi harus kurang dari 500 karakter")])
    
    created_date = DateField('Tanggal Hutang Dibuat', 
                             validators=[Optional()],
                             format='%Y-%m-%d')
    
    due_date = DateField('Tanggal Jatuh Tempo', 
                        validators=[Optional()],
                        format='%Y-%m-%d')
    
    def validate_due_date(self, field):
        if field.data and field.data < datetime.now().date():
            # Allow past dates but could add warning in template
            pass
