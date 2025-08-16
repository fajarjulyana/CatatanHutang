#!/usr/bin/env python3
"""
Script untuk menambahkan data contoh ke aplikasi Fajar Mandiri Store
"""
from datetime import datetime, timedelta
from app import app, db
from models import Debt

def seed_sample_data():
    """Add sample debt data for testing"""
    
    with app.app_context():
        # Clear existing data
        Debt.query.delete()
        
        # Sample debts
        sample_debts = [
            {
                'creditor': 'Fajar Mandiri Store',
                'debtor_name': 'Budi Santoso',
                'amount': 150000,
                'description': 'Beli sembako: beras 5kg, minyak goreng, gula pasir',
                'due_date': datetime.now().date() - timedelta(days=2),  # Overdue
                'created_at': datetime.now() - timedelta(days=10),
                'is_paid': False
            },
            {
                'creditor': 'Fajar Mandiri Store',
                'debtor_name': 'Siti Aminah',
                'amount': 75000,
                'description': 'Beli sabun, sampo, pasta gigi',
                'due_date': datetime.now().date() + timedelta(days=2),  # Due soon
                'created_at': datetime.now() - timedelta(days=5),
                'is_paid': False
            },
            {
                'creditor': 'Fajar Mandiri Store',
                'debtor_name': 'Ahmad Wijaya',
                'amount': 250000,
                'description': 'Beli pulsa dan token listrik',
                'due_date': datetime.now().date() + timedelta(days=15),
                'created_at': datetime.now() - timedelta(days=3),
                'is_paid': False
            },
            {
                'creditor': 'Fajar Mandiri Store',
                'debtor_name': 'Dewi Sartika',
                'amount': 50000,
                'description': 'Beli rokok dan kopi sachet',
                'due_date': datetime.now().date() - timedelta(days=1),  # Overdue
                'created_at': datetime.now() - timedelta(days=8),
                'is_paid': True  # Already paid
            },
            {
                'creditor': 'Fajar Mandiri Store',
                'debtor_name': 'Rudi Hartono',
                'amount': 125000,
                'description': 'Beli gas 3kg dan mie instan',
                'due_date': datetime.now().date() + timedelta(days=7),
                'created_at': datetime.now() - timedelta(days=2),
                'is_paid': False
            }
        ]
        
        # Add sample debts
        for debt_data in sample_debts:
            debt = Debt(
                creditor=debt_data['creditor'],
                debtor_name=debt_data['debtor_name'],
                amount=debt_data['amount'],
                description=debt_data['description'],
                due_date=debt_data['due_date'],
                created_at=debt_data['created_at'],
                is_paid=debt_data['is_paid']
            )
            db.session.add(debt)
        
        db.session.commit()
        print(f"✅ Berhasil menambahkan {len(sample_debts)} data contoh!")
        print("🏪 Data siap untuk testing Fajar Mandiri Store")

if __name__ == '__main__':
    seed_sample_data()