import shelve

try:
    # Try opening (or creating) the shelve file
    db = shelve.open('list.db', 'c')  # 'c' means create if it doesn't exist
    db['test_key'] = 'test_value'
    print("Shelve database created successfully!")
    db.close()
except Exception as e:
    print(f"Error opening the shelve database: {e}")
