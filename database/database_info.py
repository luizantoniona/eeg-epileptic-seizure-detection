"""
Module: database_info

This module provides configuration information for connecting to a MySQL database. It includes functions that return specific details such as the database name, username, password, and IP address.

Usage:
- Import this module to access the database configuration details.

Configuration Details:
- Modify the functions in this module to reflect the actual configuration details of your MySQL database.
"""

def name():
    """
    Returns the name of the MySQL database.
    """
    return "eeg_data"

def username():
    """
    Returns the username used for connecting to the MySQL database.
    """
    return "root"

def password():
    """
    Returns the password used for connecting to the MySQL database.
    """
    return "luiz"

def ip():
    """
    Returns the IP address or hostname of the MySQL database server.
    """
    return "127.0.0.1"
