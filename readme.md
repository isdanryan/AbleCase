# Project: Able Investigation and Enforcements Ltd Web Application (Title: AbleCase)

## Overview
The Able Investigation and Enforcements Ltd web application aims to streamline case management, invoicing, and payment processes for the company. This document provides an overview of the project, its key features, and implementation details.

## Key Features
1. **Case File Management**
   - Create new case files for clients.
   - Capture and store client details and case-specific information.
   - Organize case files for easy retrieval and management.

2. **Invoice Generation and Management**
   - Generate invoices from case files.
   - Include detailed breakdowns of services provided and costs.
   - Manage invoice lifecycle, including tracking payment statuses.

3. **Online Payment Portal for Clients**
   - Allow clients to view and pay invoices securely online.
   - Support multiple payment methods such as credit/debit cards and bank transfers.
   - Ensure compliance with industry standards for payment processing.

4. **Online Payment Portal for End Customers**
   - Enable end customers to pay fines or fees associated with cases.
   - Provide a user-friendly interface for submitting payments.
   - Integrate with case files to update payment statuses automatically.

## Implementation Details
### Technologies Used
- Django framework for backend development
- HTML/CSS/JavaScript for frontend development
- PostgreSQL database for data storage
- Stripe API for payment processing

### Development Process
1. **Setup and Configuration**
   - Create Django project and application structure.
   - Configure project settings, including database settings and security measures.
   - Set up virtual environment for dependency management.

2. **Case File Management**
   - Define Django models for case files and client details.
   - Develop views and templates for CRUD operations on case files.
   - Implement forms for capturing and validating user input.

3. **Invoice Generation and Management**
   - Design models for invoices and invoice line items.
   - Create views and templates for generating and managing invoices.
   - Integrate with PDF generation library for generating PDF invoices.

4. **Payment Integration**
   - Integrate with Stripe API for processing online payments.
   - Develop views and forms for handling payment transactions.
   - Ensure secure communication and data handling during payment processing.

5. **User Authentication and Authorization**
   - Implement user authentication and authorization mechanisms.
   - Define user roles and permissions for accessing different features.
   - Secure sensitive data and endpoints to prevent unauthorized access.

6. **Testing and Quality Assurance**
   - Conduct unit tests and integration tests for each feature.
   - Perform manual testing to validate user workflows and edge cases.
   - Address any bugs or issues identified during testing.

7. **Deployment and Maintenance**
   - Deploy the application to a reliable hosting environment.
   - Configure monitoring and logging to track application performance.
   - Establish procedures for ongoing maintenance and support.

## User Stories
### As a user
   > I want a clear view of all the case files and wether they are open or closed. I want to be able to access each case in as few clicks as possible, and easily create and update case files as needed.

### As a user
   > I want to be able to create and modify user accounts, and set the required access levels for that user.

### As a user
   > I want to be able to generate an invoice from a case file, and edit the invoices as required. I want to be able to easily view and change the status of an invoice.

### As a customer
   > I want to be able to make a payment for any fines or notices without having to create an account.

### As a customer
   > I want to be able to create an account to keep track of any fines or notices, along with any payments I have made or need to make.

### As a customer
   > I want to be able to easily pay for an invoice and recieve an email reciept.

## Conclusion
The Able Investigation and Enforcements Ltd web application will provide a comprehensive solution for managing cases, generating invoices, and processing payments efficiently. By leveraging Django and other technologies, the application will streamline operations and enhance customer satisfaction.

## Apps, Pages & Page Features
### Case management (app)
   - Cases (page): List of cases showing current status (Open/Closed)
   - Case details (page): Create a or edit details of a case. Can add and view case communications.
   - Case Communications (page): Record of all communications relating to the case. Can search and filter.
   - Case history (page): An overview of the history of the case, showing any updates to the case.

### Client Management (app)
   - Client details (page): Create or edit the main details of each client along with login details for customer portal.

### User Management (app)
   - Users (page): List of users
   - User details (page): Create or edit users and permissions.

### Invoice Management (app)
   - Invoices (page): List of invoices, with search and filter options.
   - Invoice details (page): Create or edit an invoice.

### Customer Portal (app)
   - Profile (page): Edit details and change password.
   - Cases (page): Current open and closed cases for customer.
   - Payment (page): Make a payment.

