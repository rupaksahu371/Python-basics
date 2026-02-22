# LOGINWINDOWINPYTHON

A basic frontend/GUI login window application built with Python's Tkinter library.

## 📋 Description

This is a simple Login Window application that provides a graphical user interface (GUI) for user authentication. It includes a login form with username and password fields, along with a password reset functionality.

## ✨ Features

- **User Login**: Enter username and password to log in
- **Password Masking**: Password is displayed as `*` for security
- **Success Notification**: Shows a success message box upon successful login
- **Forget Password**: Allows users to reset their password
- **Password Validation**: Confirms that new password and confirm password match

## 🛠️ Prerequisites

- Python 3.x installed on your system
- No external dependencies required (uses built-in tkinter)

## 📁 Project Structure

```
LOGIN WINDOW/
├── LOGINWINDOWINPYTHON.py   # Main login window application
├── forgetpage.py            # Password reset functionality
└── README.md                # This file
```

## 🚀 How to Run

1. Navigate to the project directory:
   
```
bash
   cd "Python coding/PYTHON PROJECTS/LOGIN WINDOW"
   
```

2. Run the main application:
   
```bash
   python LOGINWINDOWINPYTHON.py
   
```

## 📖 Usage Instructions

### Login Window
1. Enter your username in the "User name" field
2. Enter your password in the "Password" field (characters will be masked as `*`)
3. Click the **LOGIN** button
4. A success message box will appear if login is successful

### Forget Password
1. Click the **FORGET PASSWORD** button
2. A new window will open for password reset
3. Enter your username
4. Enter your new password
5. Confirm your new password
6. Click **RESET PASSWORD**
7. If passwords match, a success message will appear

## 💡 Code Overview

### Main File (LOGINWINDOWINPYTHON.py)
- Creates the main Tkinter window (600x400)
- Contains username and password entry fields
- Login button triggers the `submit()` function
- Forget Password button opens the reset window

### Password Reset (forgetpage.py)
- Creates a separate Tkinter window for password reset
- Validates that new password and confirm password match
- Shows appropriate success/error messages

## ⚠️ Note

This is a **basic frontend application**. It does not include:
- Backend authentication logic
- Database connection
- Password encryption
- Input validation

For a production application, you would need to integrate with a backend system and add proper security measures.

## 📝 License

This project is for educational purposes.
