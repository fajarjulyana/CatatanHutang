from app import db
from datetime import datetime
from sqlalchemy import func

class Debt(db.Model):
    __tablename__ = "debt"
    id = db.Column(db.Integer, primary_key=True)
    creditor = db.Column(db.String(100), nullable=False)  # Toko/Pemberi hutang
    debtor_name = db.Column(db.String(100), nullable=False)  # Nama orang yang berhutang
    amount = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    due_date = db.Column(db.Date)
    is_paid = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Debt {self.debtor_name} ke {self.creditor}: Rp {self.amount}>'
    
    @property
    def formatted_amount(self):
        """Format amount as Rupiah currency"""
        return f"Rp {self.amount:,}".replace(',', '.')
    
    @property
    def is_overdue(self):
        """Check if debt is overdue"""
        if self.due_date and not self.is_paid:
            return self.due_date < datetime.now().date()
        return False
    
    @property
    def days_until_due(self):
        """Calculate days until due date"""
        if self.due_date and not self.is_paid:
            return (self.due_date - datetime.now().date()).days
        return None
    
    @property
    def is_due_soon(self):
        """Check if debt is due within 3 days"""
        days = self.days_until_due
        return days is not None and 0 <= days <= 3
    
    @staticmethod
    def get_total_debt():
        """Calculate total unpaid debt"""
        total = db.session.query(func.sum(Debt.amount)).filter(Debt.is_paid == False).scalar()
        return total or 0
    
    @staticmethod
    def get_total_paid():
        """Calculate total paid debt"""
        total = db.session.query(func.sum(Debt.amount)).filter(Debt.is_paid == True).scalar()
        return total or 0
