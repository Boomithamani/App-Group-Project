from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify, session
import json
import shelve
from Listing import Listing
from Forms import CreateListingForm
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Secret key for session and CSRF protection
app.config['SECRET_KEY'] = 'your_secret_key'

# Directory to save uploaded pictures
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/images/logo.png')
def image():
    return send_from_directory('images', 'logo.png')

@app.route('/images/banner.png')
def image2():
    return send_from_directory('images', 'banner.png')

@app.route('/images/search.png')
def image3():
    return send_from_directory('images', 'search.png')

@app.route('/images/filter.png')
def image4():
    return send_from_directory('images', 'filter.png')

@app.route('/images/shirt1.png')
def image5():
    return send_from_directory('images', 'shirt1.png')

@app.route('/images/shirt2.png')
def image6():
    return send_from_directory('images', 'shirt2.png')

@app.route('/images/shirt3.png')
def image7():
    return send_from_directory('images', 'shirt3.png')

@app.route('/images/shirt4.png')
def image8():
    return send_from_directory('images', 'shirt4.png')

@app.route('/images/shirt5.png')
def image9():
    return send_from_directory('images', 'shirt5.png')

@app.route('/images/shirt6.png')
def image10():
    return send_from_directory('images', 'shirt6.png')

@app.route('/images/shirt7.png')
def image11():
    return send_from_directory('images', 'shirt7.png')

@app.route('/images/shirt8.png')
def image12():
    return send_from_directory('images', 'shirt8.png')

@app.route('/images/shirt9.png')
def image13():
    return send_from_directory('images', 'shirt9.png')

@app.route('/images/shirt10.png')
def image14():
    return send_from_directory('images', 'shirt10.png')

@app.route('/images/shirt11.png')
def image15():
    return send_from_directory('images', 'shirt11.png')

@app.route('/images/shirt12.png')
def image16():
    return send_from_directory('images', 'shirt12.png')

@app.route('/images/chatbot.png')
def image17():
    return send_from_directory('images', 'chatbot.png')

@app.route('/images/footer.png')
def image18():
    return send_from_directory('images', 'footer.png')

@app.route('/images/icon1.png')
def image19():
    return send_from_directory('images', 'icon1.png')

@app.route('/images/icon2.png')
def image20():
    return send_from_directory('images', 'icon2.png')

@app.route('/images/icon3.png')
def image21():
    return send_from_directory('images', 'icon3.png')

@app.route('/images/searchbar.png')
def image22():
    return send_from_directory('images', 'searchbar.png')

@app.route('/images/addlist.png')
def image23():
    return send_from_directory('images', 'addlist.png')

@app.route('/images/shirt13.png')
def image24():
    return send_from_directory('images', 'shirt13.png')

@app.route('/images/shirt14.png')
def image25():
    return send_from_directory('images', 'shirt14.png')

@app.route('/images/shirt15.png')
def image26():
    return send_from_directory('images', 'shirt15.png')

@app.route('/images/shirt16.png')
def image27():
    return send_from_directory('images', 'shirt16.png')

@app.route('/images/shirt17.png')
def image28():
    return send_from_directory('images', 'shirt17.png')

@app.route('/images/shirt18.png')
def image29():
    return send_from_directory('images', 'shirt18.png')

@app.route('/images/shirt19.png')
def image30():
    return send_from_directory('images', 'shirt19.png')

@app.route('/images/shirt20.png')
def image31():
    return send_from_directory('images', 'shirt20.png')

@app.route('/images/shirt21.png')
def image32():
    return send_from_directory('images', 'shirt21.png')

@app.route('/images/shirt22.png')
def image33():
    return send_from_directory('images', 'shirt22.png')

@app.route('/images/shirt23.png')
def image34():
    return send_from_directory('images', 'shirt23.png')

@app.route('/images/shirt24.png')
def image35():
    return send_from_directory('images', 'shirt24.png')

@app.route('/images/viewlist.png')
def image36():
    return send_from_directory('images', 'viewlist.png')

@app.route('/homeM')
def home_m():
    return render_template('homeM.html')

@app.route('/homeK')
def home_k():
    return render_template('homeK.html')

@app.route('/home')
def home1():
    return render_template('home.html')

@app.route('/searchPage')
def search():
    return render_template('searchPage.html')

@app.route('/homeS')
def home_s():
    # Render the homeS.html page. Ensure you pass any necessary data, if applicable.
    return render_template('homeS.html')


@app.route('/navbarS')
def navbar_s():
    return render_template('navbarS.html')

@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')

@app.route('/addToCart')
def cart():
    return render_template('addToCart.html')


@app.route('/filter')
def filter_shirts():
    # Retrieve category and size from the URL parameters with default values
    category = request.args.get('category', 'women')  # Default to 'women'
    size = request.args.get('size', 'M')  # Default to 'M'

    # Print the parameters for debugging
    print(f"Filtering for category: {category}, size: {size}")

    # List of shirts (this should normally be from a database or a model)
    shirts = [
        {'img': 'shirt1.png', 'category': 'women', 'size': 'L'},
        {'img': 'shirt2.png', 'category': 'women', 'size': 'M'},
        {'img': 'shirt3.png', 'category': 'women', 'size': 'S'},
        {'img': 'shirt4.png', 'category': 'women', 'size': 'M'},
        {'img': 'shirt5.png', 'category': 'women', 'size': 'M'},
        {'img': 'shirt6.png', 'category': 'women', 'size': 'S'},
        {'img': 'shirt7.png', 'category': 'women', 'size': 'L'},
        {'img': 'shirt8.png', 'category': 'women', 'size': 'L'},
        {'img': 'shirt9.png', 'category': 'women', 'size': 'M'},
        {'img': 'shirt10.png', 'category': 'women', 'size': 'L'},
        {'img': 'shirt11.png', 'category': 'women', 'size': 'L'},
        {'img': 'shirt12.png', 'category': 'women', 'size': 'M'},
        {'img': 'shirt7.png', 'category': 'men', 'size': 'L'},
        {'img': 'shirt4.png', 'category': 'men', 'size': 'M'},
        {'img': 'shirt11.png', 'category': 'men', 'size': 'L'},
        {'img': 'shirt2.png', 'category': 'men', 'size': 'M'},
        {'img': 'shirt5.png', 'category': 'men', 'size': 'M'},
        {'img': 'shirt6.png', 'category': 'men', 'size': 'S'},
        {'img': 'shirt1.png', 'category': 'men', 'size': 'L'},
        {'img': 'shirt8.png', 'category': 'men', 'size': 'L'},
        {'img': 'shirt9.png', 'category': 'men', 'size': 'M'},
        {'img': 'shirt10.png', 'category': 'men', 'size': 'L'},
        {'img': 'shirt3.png', 'category': 'men', 'size': 'S'},
        {'img': 'shirt12.png', 'category': 'men', 'size': 'M'},
        {'img': 'shirt13.png', 'category': 'kids', 'size': 'L'},
        {'img': 'shirt14.png', 'category': 'kids', 'size': 'M'},
        {'img': 'shirt15.png', 'category': 'kids', 'size': 'S'},
        {'img': 'shirt16.png', 'category': 'kids', 'size': 'M'},
        {'img': 'shirt17.png', 'category': 'kids', 'size': 'M'},
        {'img': 'shirt18.png', 'category': 'kids', 'size': 'S'},
        {'img': 'shirt19.png', 'category': 'kids', 'size': 'M'},
        {'img': 'shirt20.png', 'category': 'kids', 'size': 'L'},
        {'img': 'shirt21.png', 'category': 'kids', 'size': 'M'},
        {'img': 'shirt22.png', 'category': 'kids', 'size': 'M'},
        {'img': 'shirt23.png', 'category': 'kids', 'size': 'L'},
        {'img': 'shirt24.png', 'category': 'kids', 'size': 'M'},
    ]

    # Filter the shirts based on category and size
    filtered_shirts = [shirt for shirt in shirts if shirt['category'] == category and shirt['size'] == size]

    # Debugging output
    print(f"Filtered shirts: {filtered_shirts}")

    # Pass filtered shirts, category, and size to the template
    return render_template('home_s.html', shirts=filtered_shirts, category=category, size=size)


@app.route('/createListing', methods=['GET', 'POST'])
def create_listing():
    try:
        db = shelve.open('list.db', 'c')
        listings_dict = db.get('Listings', {})

        if request.method == 'POST':
            name = request.form.get('name')
            sizing = request.form.get('sizing')
            price = float(request.form.get('price'))
            category = request.form.get('category')
            picture = request.files.get('picture')

            # Automatically generate the next ID based on existing listings
            next_id = max(listings_dict.keys(), default=0) + 1  # Get next available ID

            # Save the picture if provided
            picture_filename = None
            if picture:
                picture_filename = secure_filename(picture.filename)
                picture.save(os.path.join(app.config['UPLOAD_FOLDER'], picture_filename))

            # Create new listing
            listings_dict[next_id] = {
                'name': name,
                'sizing': sizing,
                'price': price,
                'category': category,
                'picture': picture_filename
            }

            # Save the new listing to the database
            db['Listings'] = listings_dict
            db.close()

            return redirect(url_for('retrieve_listing'))

        db.close()
        return render_template('createListing.html')

    except Exception as e:
        return f"Error adding listing: {e}"


@app.route('/retrieveListings', methods=['GET'])
def retrieve_listing():
    try:
        db = shelve.open('list.db', 'r')  # Open the database in read-only mode
        listings_dict = db.get('Listings', {})

        # Count the number of listings
        listings_count = len(listings_dict)

        # Pass the listings dictionary to the template directly
        db.close()

        return render_template('retrieveListings.html', listings=listings_dict, listings_count=listings_count)

    except Exception as e:
        return f"Error accessing the database: {e}"


@app.route('/updateListings/<int:id>/', methods=['GET', 'POST'])
def update_listing(id):
    try:
        db = shelve.open('list.db', 'c')
        listings_dict = db.get('Listings', {})

        # Check if the listing exists
        if id not in listings_dict:
            db.close()
            return f"Listing with ID {id} not found."

        listing = listings_dict[id]  # Retrieve listing by ID

        if request.method == 'POST':
            # Update listing details
            listing['name'] = request.form.get('name')
            listing['sizing'] = request.form.get('sizing')
            listing['price'] = float(request.form.get('price'))
            listing['category'] = request.form.get('category')

            # Handle image upload
            picture = request.files.get('picture')
            if picture and picture.filename:  # If a new image is uploaded
                picture_filename = secure_filename(picture.filename)
                picture_path = os.path.join(app.config['UPLOAD_FOLDER'], picture_filename)
                picture.save(picture_path)
                listing['picture'] = picture_filename  # Update picture in the listing

            # Save updated listing back to the database
            listings_dict[id] = listing
            db['Listings'] = listings_dict
            db.close()

            return redirect(url_for('retrieve_listing'))

        db.close()
        return render_template('updateListings.html', listing=listing, id=id)

    except Exception as e:
        return f"Error accessing the database: {e}"



@app.route('/deleteListings/<int:id>', methods=['POST'])
def delete_listing(id):
    try:
        db = shelve.open('list.db', 'w')
        listings_dict = db.get('Listings', {})

        # Remove the listing with the given id
        if id in listings_dict:
            listings_dict.pop(id)

        db['Listings'] = listings_dict
        db.close()

        return redirect(url_for('retrieve_listing'))  # Redirect after deletion

    except Exception as e:
        return f"Error deleting listing: {e}"

cart = []

CART_FILE = 'cart.json'

# Function to load the cart data from the file
def load_cart():
    if os.path.exists(CART_FILE):
        with open(CART_FILE, 'r') as file:
            return json.load(file)
    return {}

# Function to save the cart data to the file
def save_cart(cart_data):
    with open(CART_FILE, 'w') as file:
        json.dump(cart_data, file)

# CREATE: Add item to cart
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item_id = request.form.get('item_id')
    item_name = request.form.get('item_name')
    item_price = float(request.form.get('item_price'))

    # Initialize the cart in session if not already
    if 'cart' not in session:
        session['cart'] = []

    # Add the item to the cart
    session['cart'].append({
        'id': item_id,
        'name': item_name,
        'price': item_price
    })
    session.modified = True  # Indicate session data has changed

    return redirect(url_for('view_cart'))  # Redirect to cart page or wherever needed



@app.route('/delete-from-cart/<int:item_id>', methods=['POST'])
def delete_from_cart(item_id):
    cart = session.get('cart', [])
    cart = [item for item in cart if item['id'] != str(item_id)]  # Filter out the item
    session['cart'] = cart  # Update the session
    session.modified = True
    return redirect(url_for('cart'))

# View cart
@app.route('/view_cart')  # A specific route to avoid conflicts
def view_cart():
    cart_items = session.get('cart', [])  # Retrieve cart items from the session
    total_price = sum(item['price'] for item in cart_items)  # Calculate total price
    return render_template('home.html', cart_items=cart_items, total_price=total_price)


if __name__ == '__main__':
    app.run()

