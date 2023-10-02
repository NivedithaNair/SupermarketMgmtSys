# Supermarket Management System

The Supermarket Management System is a Python-based software solution that helps manage various aspects of a supermarket, including product management, billing, and tax code management. This system is designed for both system administrators and supermarket staff, providing different functionalities based on user roles.

## Features

- **Product Management**: System administrators can add, update, delete, and display products in the supermarket's inventory. They can also manage product details like name, quantity, price, and discount.

- **Billing**: Staff members can use the billing module to generate bills for customers. This module allows them to select products, specify quantities, and calculate the total bill amount, including taxes and discounts.

- **Tax Code Management**: System administrators can manage HSN (Harmonized System of Nomenclature) codes and their corresponding tax percentages. This feature helps in calculating taxes accurately for different products.

## Usage

The Supermarket Management System is a command-line application. It provides a menu-driven interface for users to perform various operations. Users can choose between two roles:

- **Sysadmin**: System administrators have full access to product management, tax code management, and billing functionalities. They need to enter a password to access sysadmin features.

- **Admin**: Supermarket staff can use the billing module to create bills for customers.

## Installation

1. Clone this repository to your local machine:

2. Install the required dependencies. Make sure you have Python and MySQL installed.

3. Set up your MySQL database with the necessary tables. You can use the provided SQL scripts to create the database schema.

4. Configure the database connection settings in the Python code.

5. Run the `Main Supermarket Program.py` file to start the Supermarket Management System.

## Contributing

Contributions are welcome! If you find any issues or have ideas for improvements, please open an issue or submit a pull request.

This Supermarket Management System is developed by Niveditha Nair as a sample project for educational purposes.
