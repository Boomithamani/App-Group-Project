import sqlite3
import sys


# Check if running in a GUI-capable environment
def is_gui_available():
    return sys.platform in ("win32", "darwin", "linux")


if is_gui_available():
    import tkinter as tk
    from tkinter import messagebox
else:
    print("GUI is not supported in this environment.")


def create_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)
    conn.commit()
    conn.close()


def get_usernames():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users")
    usernames = [row[0] for row in cursor.fetchall()]
    conn.close()
    return usernames


def register_user(username, password, role):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
        conn.commit()
        if is_gui_available():
            messagebox.showinfo("Success", "User registered successfully")
            update_username_dropdown()
        else:
            print("User registered successfully")
    except sqlite3.IntegrityError:
        if is_gui_available():
            messagebox.showerror("Error", "Username already exists")
        else:
            print("Error: Username already exists")
    finally:
        conn.close()


def login():
    username = entry_username.get()
    password = entry_password.get()

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        role = result[0]
        if is_gui_available():
            messagebox.showinfo("Login Successful", f"Welcome {role} {username}!")
        else:
            print(f"Login Successful: Welcome {role} {username}!")
    else:
        if is_gui_available():
            messagebox.showerror("Login Failed", "Invalid username or password")
        else:
            print("Login Failed: Invalid username or password")


def update_username_dropdown():
    usernames = get_usernames()
    username_var.set("")
    entry_username['menu'].delete(0, 'end')
    for name in usernames:
        entry_username['menu'].add_command(label=name, command=lambda value=name: username_var.set(value))


def view_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users


def update_user(username, new_password, new_role):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password = ?, role = ? WHERE username = ?", (new_password, new_role, username))
    conn.commit()
    conn.close()
    if is_gui_available():
        messagebox.showinfo("Success", "User updated successfully")
    else:
        print("User updated successfully")


def delete_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE username = ?", (username,))
    conn.commit()
    conn.close()
    if is_gui_available():
        messagebox.showinfo("Success", "User deleted successfully")
        update_username_dropdown()
    else:
        print("User deleted successfully")


if is_gui_available():
    def register_window():
        reg_win = tk.Toplevel(root)
        reg_win.title("Register")
        reg_win.geometry("300x200")

        tk.Label(reg_win, text="Username:").pack()
        reg_username = tk.Entry(reg_win)
        reg_username.pack()

        tk.Label(reg_win, text="Password:").pack()
        reg_password = tk.Entry(reg_win, show="*")
        reg_password.pack()

        tk.Label(reg_win, text="Role (admin/user):").pack()
        reg_role = tk.Entry(reg_win)
        reg_role.pack()

        tk.Button(reg_win, text="Register",
                  command=lambda: register_user(reg_username.get(), reg_password.get(), reg_role.get())).pack()


    def view_users_window():
        users = view_users()
        user_list_win = tk.Toplevel(root)
        user_list_win.title("Users List")

        for user in users:
            tk.Label(user_list_win, text=f"ID: {user[0]}, Username: {user[1]}, Role: {user[3]}").pack()


    def delete_user_window():
        del_win = tk.Toplevel(root)
        del_win.title("Delete User")

        tk.Label(del_win, text="Username:").pack()
        del_username = tk.Entry(del_win)
        del_username.pack()

        tk.Button(del_win, text="Delete", command=lambda: delete_user(del_username.get())).pack()


    # Create database
    create_db()

    # GUI setup
    root = tk.Tk()
    root.title("Login System")
    root.geometry("300x300")

    tk.Label(root, text="Username:").pack()
    username_var = tk.StringVar()
    entry_username = tk.OptionMenu(root, username_var, *get_usernames())
    entry_username.pack()

    tk.Label(root, text="Password:").pack()
    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    tk.Button(root, text="Login", command=login).pack()
    tk.Button(root, text="Register", command=register_window).pack()
    tk.Button(root, text="View Users", command=view_users_window).pack()
    tk.Button(root, text="Delete User", command=delete_user_window).pack()

    root.mainloop()
else:
    print("GUI mode is not available. Please run this script in a GUI-supported environment.")
