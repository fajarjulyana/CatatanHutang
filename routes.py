from flask import render_template, request, redirect, url_for, flash, jsonify
from app import app, db
from models import Debt
from forms import DebtForm
from datetime import datetime, timedelta

@app.route('/')
def index():
    # Get filter and sort parameters
    status_filter = request.args.get('status', 'all')
    sort_by = request.args.get('sort', 'created_at')
    order = request.args.get('order', 'desc')
    search = request.args.get('search', '')
    
    # Base query
    query = Debt.query
    
    # Apply filters
    if status_filter == 'paid':
        query = query.filter(Debt.is_paid == True)
    elif status_filter == 'unpaid':
        query = query.filter(Debt.is_paid == False)
    elif status_filter == 'overdue':
        query = query.filter(Debt.due_date < datetime.now().date(), Debt.is_paid == False)
    
    # Apply search
    if search:
        query = query.filter(
            db.or_(
                Debt.creditor.ilike(f'%{search}%'),
                Debt.debtor_name.ilike(f'%{search}%'),
                Debt.description.ilike(f'%{search}%')
            )
        )
    
    # Apply sorting
    if sort_by == 'amount':
        if order == 'asc':
            query = query.order_by(Debt.amount.asc())
        else:
            query = query.order_by(Debt.amount.desc())
    elif sort_by == 'due_date':
        if order == 'asc':
            query = query.order_by(Debt.due_date.asc().nullslast())
        else:
            query = query.order_by(Debt.due_date.desc().nullsfirst())
    elif sort_by == 'creditor':
        if order == 'asc':
            query = query.order_by(Debt.creditor.asc())
        else:
            query = query.order_by(Debt.creditor.desc())
    elif sort_by == 'debtor_name':
        if order == 'asc':
            query = query.order_by(Debt.debtor_name.asc())
        else:
            query = query.order_by(Debt.debtor_name.desc())
    else:  # created_at
        if order == 'asc':
            query = query.order_by(Debt.created_at.asc())
        else:
            query = query.order_by(Debt.created_at.desc())
    
    debts = query.all()
    
    # Calculate totals
    total_debt = Debt.get_total_debt()
    total_paid = Debt.get_total_paid()
    total_all = total_debt + total_paid
    
    # Calculate alerts for overdue and due soon debts
    today = datetime.now().date()
    
    overdue_debts = Debt.query.filter(
        Debt.due_date.isnot(None),
        Debt.due_date < today,
        Debt.is_paid == False
    ).count()
    
    due_soon_debts = Debt.query.filter(
        Debt.due_date.isnot(None),
        Debt.due_date >= today,
        Debt.due_date <= today + timedelta(days=3),
        Debt.is_paid == False
    ).count()
    
    return render_template('index.html', 
                         debts=debts, 
                         total_debt=total_debt,
                         total_paid=total_paid,
                         total_all=total_all,
                         status_filter=status_filter,
                         sort_by=sort_by,
                         order=order,
                         search=search,
                         overdue_count=overdue_debts,
                         due_soon_count=due_soon_debts,
                         today=today)

@app.route('/add_debt', methods=['GET', 'POST'])
def add_debt():
    form = DebtForm()
    
    if form.validate_on_submit():
        # Use form created_date if provided, otherwise use current time
        created_date = form.created_date.data if form.created_date.data else datetime.now()
        
        # Validate amount
        if form.amount.data < 1000:
            flash('Jumlah hutang harus minimal Rp 1.000', 'error')
            return render_template('add_debt.html', form=form)
        
        debt = Debt(
            creditor=form.creditor.data,
            debtor_name=form.debtor_name.data,
            amount=form.amount.data,
            description=form.description.data,
            due_date=form.due_date.data,
            created_at=created_date
        )
        
        db.session.add(debt)
        db.session.commit()
        
        flash('Hutang berhasil ditambahkan!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_debt.html', form=form)

@app.route('/edit_debt/<int:debt_id>', methods=['GET', 'POST'])
def edit_debt(debt_id):
    debt = Debt.query.get_or_404(debt_id)
    form = DebtForm(obj=debt)
    
    # Set the created_date in the form from the debt's created_at
    if debt.created_at:
        form.created_date.data = debt.created_at.date()
    
    if form.validate_on_submit():
        # Validate amount
        if form.amount.data < 1000:
            flash('Jumlah hutang harus minimal Rp 1.000', 'error')
            return render_template('edit_debt.html', form=form, debt=debt)
        
        debt.creditor = form.creditor.data
        debt.debtor_name = form.debtor_name.data
        debt.amount = form.amount.data
        debt.description = form.description.data
        debt.due_date = form.due_date.data
        
        # Update created_at if form created_date is provided
        if form.created_date.data:
            debt.created_at = form.created_date.data
        
        debt.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        flash('Hutang berhasil diperbarui!', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit_debt.html', form=form, debt=debt)

@app.route('/toggle_paid/<int:debt_id>', methods=['POST'])
def toggle_paid(debt_id):
    debt = Debt.query.get_or_404(debt_id)
    debt.is_paid = not debt.is_paid
    debt.updated_at = datetime.utcnow()
    
    db.session.commit()
    
    status = 'lunas' if debt.is_paid else 'belum lunas'
    flash(f'Hutang ditandai sebagai {status}!', 'success')
    
    return redirect(url_for('index'))

@app.route('/delete_debt/<int:debt_id>', methods=['POST'])
def delete_debt(debt_id):
    debt = Debt.query.get_or_404(debt_id)
    
    db.session.delete(debt)
    db.session.commit()
    
    flash('Hutang berhasil dihapus!', 'success')
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
