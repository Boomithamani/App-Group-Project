from flask import Flask, render_template, request, redirect, url_for, flash
from Forms import CreateSaleForm
import shelve, Sale

app = Flask(__name__)
app.secret_key = 'secretkey'
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/createSale', methods=['POST'])
def create_sale():
    create_sale_form = CreateSaleForm(request.form)
    if create_sale_form.validate():
        sales_dict = {}
        db = shelve.open('sale.db','c')
        sale_id_counter = db.get('SaleIDCounter', 0)
        sale_id_counter += 1

        try:
            sales_dict = db['Sales']
        except:
            print("Error in retrieving sales from sales.db.")

        sale = Sale.Sale(create_sale_form.item_name.data,
                         create_sale_form.category.data,
                         create_sale_form.quantity_sold.data,
                         create_sale_form.unit_price.data
                         )
        sales_dict[sale.get_sale_id()] = sale
        db['Sales'] = sales_dict

        db.close()

        flash(f"{sale.get_item_name()} added successfully!", "success")

        return redirect(url_for('retrieve_sales'))

    flash("Error adding sale. Please try again.", "danger")
    return redirect(url_for('retrieve_sales'))

@app.route('/retrieveSales')
def retrieve_sales():
    sales_dict = {}
    db = shelve.open('sale.db', 'r')
    sales_dict = db['Sales']
    db.close()

    sales_list = []
    for key in sales_dict:
        sale = sales_dict.get(key)
        sales_list.append(sale)

    return render_template('retrieveSales.html', count=len(sales_list), sales_list=sales_list)

@app.route('/updateSale/<int:id>/', methods=['POST'])
def update_sale(id):
    update_sale_form = CreateSaleForm(request.form)
    if update_sale_form.validate():
        db = shelve.open('sale.db', 'w')
        sales_dict = db.get('Sales', {})

        sale = sales_dict.get(id)
        if sale:
            sale.set_item_name(update_sale_form.item_name.data)
            sale.set_category(update_sale_form.category.data)
            sale.set_quantity_sold(update_sale_form.quantity_sold.data)
            sale.set_unit_price(update_sale_form.unit_price.data)
            total_price = sale.get_quantity_sold() * sale.get_unit_price()
            sale.set_total_price(total_price)

            db['Sales'] = sales_dict
            db.close()

        flash(f"Sale {sale.get_item_name()} updated successfully!", "success")
        return redirect(url_for('retrieve_sales'))

    flash("Failed to update sale. Please check your input.", "danger")
    return redirect(url_for('retrieve_sales'))

@app.route('/deleteSale/<int:id>', methods=['POST'])
def delete_sale(id):
    sales_dict = {}

    db = shelve.open('sale.db', 'w')
    sales_dict = db['Sales']

    if id in sales_dict:
        sale = sales_dict.pop(id)

        db['Sales'] = sales_dict
        db.close()

        # flash success message
        flash(f"Sale {sale.get_item_name()} deleted successfully!", "success")
    else:
        flash("Sale not found. Deletion failed.", "danger")

    return redirect(url_for('retrieve_sales'))

@app.route('/searchSales', methods=['GET'])
def search_sales():
    query = request.args.get('query', '').strip().lower()
    sales_dict = {}

    db = shelve.open('sale.db', 'r')
    sales_dict = db.get('Sales', {})
    db.close()

    filtered_sales = []
    for sale in sales_dict.values():
        if (query in sale.get_item_name().lower()) or (query.isdigit() and float(query) == sale.get_unit_price()):
            filtered_sales.append(sale)

    return render_template('retrieveSales.html', count=len(filtered_sales), sales_list=filtered_sales,
                           search_query=query)
@app.route('/filterSales', methods=['GET'])
def filter_sales():
    selected_category = request.args.get('category', '')

    sales_dict = {}
    db = shelve.open('sale.db', 'r')
    sales_dict = db.get('Sales', {})
    db.close()

    # Filter sales based on category
    filtered_sales = [sale for sale in sales_dict.values() if sale.get_category() == selected_category] if selected_category else list(sales_dict.values())

    return render_template('retrieveSales.html', count=len(filtered_sales), sales_list=filtered_sales, selected_category=selected_category)

if __name__ == '__main__':
    app.run()