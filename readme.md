# Project: Able Investigation and Enforcements Ltd Web Application (Title: AbleCase)

## Table of Contents

1. [Overview](#overview)
2. [Scope](#scope)
3. [Key Features](#key-features)
4. [Importance / Feasibility score](#importance--feasibility-score)
5. [User Stories](#user-stories)
6. [Conclusion](#conclusion)
7. [Structure](#structure)
   - [Overview](#overview)
   - [Dashboard](#dashboard-app)
   - [Case Management](#case-management-app)
   - [Client Management](#client-management-app)
   - [User Management](#user-management-app)
   - [Invoice Management](#invoice-management-app)
   - [Customer Portal](#customer-portal-app)
8. [User Workflow](#user-workflow)
9. [Models & Schema](#models--schema)
   - [Database Overview](#database-overview)
   - [Tables](#tables)
10. [Layout & Design](#layouts--design)
      - [Content and Colour Scheme](#content-and-colour-scheme)
      - [Typogrpphy](#typogrophy)
      - [Wireframes](#wireframes)
      - [Login Screen](#login-screen)
      - [Dashboard Screen](#dashboard-screen)
      - [List Views](#list-views)
      - [Form Views](#form-views-add--edit-views)
11. [Implementation](#implementation)
      - [Technologies Used](#technologies-used)
      - [Development Process](#development-process)
12. [Deployment](#deployment)
      - [Local Deployment](#local-deployment)
      - [Remote/Production Deployment](#remoteproduction-deployment)
13. [Testing](#testing)
      - [Manual Testing](#manual-testing)
      - [Automated Testing](#automated-testing)
      - [Browser Testing](#browser-testing)
      - [Code Validation](#code-validation)
14. [Known Issues & Bugs](#known-issues--bugs)
15. [Final Screenshots](#final-screenshots)


## Overview
The Able Investigation and Enforcements Ltd web application aims to streamline case management, invoicing, and payment processes for the company. This document provides an overview of the project, its key features, and implementation details.

## Scope
As this will be submitted for an assignmet there will be trade-offs against the design and development process. Any additonal features classified as low importance can be revisitted at a later date. Using the AGILE method for development, I will carry out weekly reviews both personally and with the client to add or modify features as applicable to the project at the end of each sprint phase.

## Key Features
After the initial disscussion with the client, I have listed out each key feature for the project and assigned each an importance and feasibility score to help avoid scope creep and secure a MVP by the deadline.

1. **Case File Management**
   - Create new case files for clients, capturing and storing case-specific information.
   - Search case files based of specific criteria like client or case number.
   - Organize case files for easy retrieval and management.
   - Update case files with any on going communication history specific to the case.

2. **Client Management**
   - Create new clients.
   - Edit and Update client details.
   - Delete Clients from the system.

3. **User Management**
   - Create new users.
   - Set user permissions with application specific permission levels.
     (e.g. View/Edit case files, View/Edit client detials).
   - Edit user details.
   - Block and allow access to the platform.
   - Change own password.
   - Add and track tasks.
   
4. **Invoice Generation and Management**
   - Generate invoices from case files.
   - Include detailed breakdowns of services provided and costs.
   - Manage invoice lifecycle, including tracking payment status.

5. **Online Payment Portal for Clients and Customers**
   - Allow clients to view and pay invoices securely online.
   - Support multiple payment methods such as credit/debit cards and bank transfers.
   - Ensure compliance with industry standards for payment processing.

6. **Report Management**
   - Create audit reports for tracking updates to clients.
   - Create audit reports for tracking updates to cases.
   - Create audit reports for tracking updates to invoices.

## Importance / Feasibility score
**1** - Low, **5** - High   

| Feature | Importance | Feasibility |
|---------|------------|-----------|
| Create new case files for clients, capturing and storing case-specific information. | 5 | 5 |
| Search case files based of specific criteria like client or case number. | 5 | 5 |
| Organize case files for easy retrieval and management. | 4 | 4 |
| Update case files with any on going communication history specific to the case. | 5 | 4 |
| Create new clients. | 5 | 5 |
| Edit and Update client details. | 5 | 5 |
| Delete Clients from the system. | 3 | 5 |
| Create new users. | 5 | 5 |
| Set user permissions with application specific permission levels. | 3 | 3 |
| Edit user details. | 5 | 5 |
| Block and allow access to the platform. | 5 | 4 |
| Change own password. | 3 | 4 |
| Add and track tasks. | 2 | 4 |
| Generate invoices from case files. | 4 | 4 |
| Include detailed breakdowns of services provided and costs. | 3 | 3 |
| Manage invoice lifecycle, including tracking payment status. | 4 | 3 |
| Allow clients to view and pay invoices securely online. | 5 | 5 |
| Support multiple payment methods such as credit/debit cards and bank transfers. | 3 | 3 |
| Ensure compliance with industry standards for payment processing. | 5 | 5 |
| Create audit reports for tracking updates to clients. | 2 | 3 |
| Create audit reports for tracking updates to casess. | 2 | 3 |
| Create audit reports for tracking updates to invoices. | 2 | 3 |

## User Stories
### As a user
   > I want a clear view of all the case files and wether they are open or closed. I want to be able to access each case in as few clicks as possible, and easily create and update case files as needed.

### As a user
   > I want to be able to create and modify user accounts, and set the required access levels for that user.

### As a user
   > I want to be able to generate an invoice from a case file, and edit the invoices as required. I want to be able to easily view and change the status of an invoice.

### As a customer
   > I want to be able to make a payment for any invoices easily online.

### As a customer
   > I want to be able to create an account to keep track of any fines or notices, along with any payments I have made or need to make.

## Conclusion
The Able Investigation and Enforcements Ltd web application will provide a comprehensive solution for managing cases, generating invoices, and processing payments efficiently. By leveraging Django and other technologies, the application will streamline operations and enhance customer satisfaction.

## Structure
### Overview
During the second design meeting with the client, the general user interaction was fleshed out for how the staff and clients will interact with the web app.

![Flow chart](docs/flowchart/flow-chart.png)

### Dashboard (app)
   - Dashboard (page): Overview of current open cases and stats, current tasks for user.

### Case management (app)
   - Cases (page): List of cases showing current status (Open/Closed)
   - Case details (page): Create a or edit details of a case. Can add and view case communications.
   - Case Communications (page): Record of all communications relating to the case. Can search and filter.

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
   - Invoices (page): All invoices specific to the customer.
   - Payments (page): Make a payment.

## User workflow
After this meeting, the following user flow chart and app layout was put together for the client to sign off. The flowcharts were drawn in [SmartDraw](https://app.smartdraw.com/)

## Models & Schema
The following database models and schema were drawn in [DrawSQL](https://drawsql.app), and an embedded link to the full database schema with comments can be found [here](https://drawsql.app/teams/dan-54/diagrams/ablecase/embed).

### Database Overview
![Database Schema](docs/database/ablecase-schema-overview.png)

### Tables
#### Clients
![Database Schema](docs/database/ablecase-clients.png)

#### Cases
![Database Schema](docs/database/ablecase-cases.png)

#### Communications
![Database Schema](docs/database/ablecase-communications.png)

#### Case Types
![Database Schema](docs/database/ablecase-casetypes.png)

#### Users
![Database Schema](docs/database/ablecase-users.png)

#### Tasks
![Database Schema](docs/database/ablecase-tasks.png)

#### Invoices
![Database Schema](docs/database/ablecase-invoices.png)

#### Invoice Codes
![Database Schema](docs/database/ablecase-invoicecode.png)

#### Payments
![Database Schema](docs/database/ablecase-payments.png)

## Layouts & Design

### Content and Colour Scheme
The clients request was to keep everything sleek with a modern feel. They wanted to include their new logo, with hints of the red they currently use as their brand company colour.
In order to stick to the given brief, i've chosen to go with a slightly off black mixed with white for the backgrounds, and use a light grey/ off white to make the user input areas stand out more.
For the various buttons, I intend to use the commonly used Red, Blue and Green for specific actions, such as Red for a delete action.

Content is generated soley off data held in the database, and as such I do not need to worry about any content text, apart from names and labels.

### Typogrophy
After discussing it through during the initial design phase, the client does not have any specific fonts in mind, so I have chosen to leverage Bootstraps default fonts as the provide the clean and modern feel requried.

### Wireframes
Below are a set of initial drafts for the overall design and layout for the application. By sticking with the clean and simple design requested by the client and utilising Bootstrap 5, it was possible to keep alot of the key views following the same layout.

### Login screen
It has been decided that the same design will be used for both the User login and the Client Portal login.

**Desktop**

![Login wireframe](docs/wireframes/login-desktop.png)

**Mobile**

![Mobile login wireframe](docs/wireframes/login-mobile.png)

### Dashboard screen
The dashboard screen will be the first landing page the user reaches after logging in. The idea will be to have several large sectional areas with live tracking of the KPI's, such as Open case and cases that have passed their review date.

Along with a larger display list of the current cases that are due to be reviewed.

Also featured, will be a simple task list for the user.

**Desktop**

![Dashboard wireframe](docs/wireframes/dashboard-desktop.png)

**Mobile**

![Mobile dashboard wireframe](docs/wireframes/dashboard-mobile.png)


### List views
Each of the pages that utilise displaying a list will all follow the same layout to ease usability. 
As simple breadcrumb for navigation, the main list for that page (Clients, Cases, Users, etc.)
And a search and add new function.

**Desktop**
![List view wireframe](docs/wireframes/list-view-desktop.png)

**Mobile**

![Mobile list view wireframe](docs/wireframes/list-view-mobile.png)


### Form views (add & edit views)
All pages that utilise a form layout will follow the same layout and structure as well. The style will follow the rest of the site keeping with the simple, clean and modern asspect.

**Desktop**

![Form view wireframe](docs/wireframes/form-views-desktop.png)

**Mobile**

![Mobile form view wireframe](docs/wireframes/form-views-mobile.png)

### Invoice Creation
Alot of the invoice fields will be pre-populated from the held case data, this includes things like the client and the case name and address.

Also within the structure, several of the fields will be coded using JS to auto calculate off selected data.

**Date due:** This will auto fill based of the date and whatever term is selected. e.g If 14 days is selected the due date will auto-update with a value of 14 days after the date.

**Total amount:** This will auto fill based of the amount and whatever VAT rate is selected. e.g If 20% is selected, the total amount will auto-update with a value of the amount plus 20%.

![Invoice wireframe](docs/wireframes/invoice.png)

## Implementation

### Technologies Used
- Django framework for backend development
- HTML/CSS/JavaScript for frontend development
- PostgreSQL database for data storage
- Stripe API for payment processing

In order to convert the html invoices to a downloadable PDF, I have opted to use an open-source package called **xhtml2pdf**. A full explination and further details of **xhtml2pdf** can be found [here](https://pypi.org/project/xhtml2pdf/).

A full list of packages used can be found in the [requirements.txt](/requirements.txt) file.

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
   - Define models for invoices and invoice line items.
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

6. **Report Management**
   - Create view to pull update and created records for client, cases and invoices.
   - Implement search and filter requests.
   - Create templates to show each of the required reports.

6. **Testing and Quality Assurance**
   - Conduct unit tests and integration tests for each feature.
   - Perform manual testing to validate user workflows and edge cases.
   - Address any bugs or issues identified during testing.

7. **Deployment and Maintenance**
   - Deploy the application to a reliable hosting environment.
   - Configure monitoring and logging to track application performance.
   - Establish procedures for ongoing maintenance and support.

## Deployment

### Local deployment

**1. Clone the GitHub Repository:**

   - Open your chosen IDE and use the terminal to clone the project from GitHub to your local machine.

**2. Navigate to the directory**

   - Change into the directory:

    cd your-dir

**3. Create a Virtual Environment:**

   - Set up a Python virtual environment to manage dependencies:

    python -m venv venv

   - Activate the virtual environment:

   Windows:

    venv\Scripts\activate
   
   macOS/Linux:

    source venv/bin/activate

**4. Install Project Dependencies:**

   - Install the required Python packages from the requirements.txt file:

    pip install -r requirements.txt

**5. Install PostgreSQL:**

   - Install PostgreSQL:

   - Windows: Download from PostgreSQL website.

   - macOS: Use Homebrew:

    brew install postgresql

   - Linux (Debian/Ubuntu):

    sudo apt-get update
    sudo apt-get install postgresql postgresql-contrib

**6. Start PostgreSQL Service:**

   - Ensure that the PostgreSQL service is running:

   - macOS/Linux:

    sudo service postgresql start
   
   - Windows: The service should start automatically after installation, but you can check the PostgreSQL service status in "Services."

**7. Create a PostgreSQL Database:**

   - Open the PostgreSQL shell or use a database management tool:

    psql -U postgres
   
   - Enter the PostgreSQL password you set during installation. Then create a new database:

    CREATE DATABASE db_name;
    CREATE USER db_user WITH PASSWORD 'db_password';
    ALTER ROLE db_user SET client_encoding TO 'utf8';
    ALTER ROLE db_user SET default_transaction_isolation TO 'read committed';
    ALTER ROLE db_user SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE db_name TO db_user;

   - Replace db_name, db_user, and db_password with your preferred database name, username, and password.

**8. Set Up Environment Variables:**

   - Copy the sample .env.sample file to a new .env file:

    cp .env.sample .env

   - Open the .env file in your IDE and update it with the PostgreSQL connection details:

   - Replace the values with the values you set in the PostgreSQL setup. Make sure to set a secure SECRET_KEY.

**9. Run Database Migrations:**

   - Apply the database migrations to set up your local database schema:

    python manage.py migrate

**10. Create a Superuser (Admin):**

   - Create a superuser account to access the Django admin interface:

    python manage.py createsuperuser

   - Follow the prompts to set a username, email, and password.

**11. Run the Development Server:**

   - Start the Django development server:

    python manage.py runserver

   - You should now be able to access the Django project locally by navigating to http://127.0.0.1:8000/ in your web browser.

**12. Verify Everything Works:**

   - Visit http://127.0.0.1:8000/admin/ to log in to the Django admin using the superuser credentials you created earlier.

   - Check the main pages of your application to ensure everything is working as expected.

### Remote/Final production deployment

The following steps assume that there is a server already set up with a Linux operating system, and a web server (like Nginx or Apache) is installed and running. I have optted to use Gunicorn as the WSGI server to serve the Django application, and use UFW as the firewall.

For the final deployment in order to keep things as secure as possible, I offloaded the database to anoter hosting platform. However the steps below also include installing a PostgreSQL database on the same server.

**1. Connect to the Server:**

   - Use SSH to connect to your server:

    ssh username@your-server-ip

   - Be sure to replace username with your server's username and your-server-ip with your server's IP address.

**2. Install Required Packages:**

   - Update the package list and install the required packages, including Git, Python, virtual environment tools, and PostgreSQL client libraries:

    sudo apt update
    sudo apt install git python3-pip python3-venv postgresql postgresql-contrib libpq-dev nginx

**3. Clone the GitHub Repository:**

   - Navigate to the directory where you want to deploy the web app (e.g., /var/www/):

    cd /var/www/

   - Clone your files from GitHub:

    sudo git clone https://github.com/isdanryan/ablecase.git


**4. Create and Activate a Virtual Environment:**

   - Navigate to your directory and create a virtual environment:

    cd your-dir
    python3 -m venv venv

   - Activate the virtual environment:

    source venv/bin/activate

**5. Install Project Dependencies:**

   - Install the required Python packages from the requirements.txt file:

    pip install -r requirements.txt

**6. Set Up PostgreSQL Database:**

   - Switch to the PostgreSQL user:

    sudo -i -u postgres

   - Open the PostgreSQL shell:

    psql

   - Create a new database and user with the following commands:

    CREATE DATABASE your_db_name;
    CREATE USER your_db_user WITH PASSWORD 'your_db_password';
    ALTER ROLE your_db_user SET client_encoding TO 'utf8';
    ALTER ROLE your_db_user SET default_transaction_isolation TO 'read committed';
    ALTER ROLE your_db_user SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;
    \q

   - Exit back to your normal user:

    exit

**7. Set Up Environment Variables:**

   - Copy the .env.sample file to a new .env file:

    cp .env.sample .env

   - Open the .env file with a text editor and update it with the PostgreSQL connection details and other environment variables:

    DATABASE_URL=postgres://your_db_user:your_db_password@localhost:5432/your_db_name
    SECRET_KEY=your_secret_key
    DEBUG=False
    ALLOWED_HOSTS=your_server_ip, your_domain

   - Replace your_db_user, your_db_password, your_db_name, your_secret_key, your_server_ip, and your_domain with the appropriate values.

**8. Run Database Migrations:**

   - Apply the database migrations to set up your database schema:

    python manage.py migrate

**9. Collect Static Files:**

   - Collect all static files into the STATIC_ROOT directory:

    python manage.py collectstatic

**10. Create a Superuser (Admin):**

   - Create a superuser account to access the Django admin interface:

    python manage.py createsuperuser

   - Follow the prompts to set a username, email, and password.

**11. Install and Configure Gunicorn:**

   - Install Gunicorn in the virtual environment:

    pip install gunicorn

   - Test the Gunicorn setup by running:

    gunicorn --workers 3 ablecase.wsgi:application

**12. Create a Gunicorn Systemd Service File:**

   - Create a service file to manage Gunicorn with systemd:

    sudo nano /etc/systemd/system/gunicorn.service

   - Add the following configuration, replacing any placeholders with the correct information:

    [Unit]
    Description=gunicorn daemon for AbleCase
    After=network.target

    [Service]
    User=your_username
    Group=www-data
    WorkingDirectory=/var/www/your-dir
    ExecStart=/var/www/your-dir/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/var/www/your-dir/ablecase.sock ablecase.wsgi:application

    [Install]
    WantedBy=multi-user.target

   - Save and close the file.

**13. Start and Enable Gunicorn:**

- Reload the systemd daemon, start Gunicorn, and enable it to start on boot:

   sudo systemctl daemon-reload
   sudo systemctl start gunicorn
   sudo systemctl enable gunicorn

**14. Configure Nginx:**

   - Create an Nginx configuration file for the web app:

    sudo nano /etc/nginx/sites-available/ablecase

   - Add the following Nginx server block:

    server {
       listen 80;
       server_name your_server_ip your_domain;

       location = /favicon.ico { access_log off; log_not_found off; }
       location /static/ {
          root /var/www/your-dir;
       }

       location / {
          include proxy_params;
          proxy_pass http://unix:/var/www/your-dir/ablecase.sock;
       }

       client_max_body_size 100M;  # Adjust the max body size if needed
    }

   - Save and close the file.

   - Enable the site by creating a symbolic link to sites-enabled:

    sudo ln -s /etc/nginx/sites-available/ablecase /etc/nginx/sites-enabled

**15. Test Nginx Configuration and Restart:**

   - Test the Nginx configuration for syntax errors:

    sudo nginx -t

   - If the test is successful, restart Nginx:

    sudo systemctl restart nginx

**16. Adjust Firewall Settings (if needed):**

   - Allow HTTP and HTTPS traffic through the firewall:

    sudo ufw allow 'Nginx Full'

**17. Verify Deployment:**

   - Open a web browser and navigate to your server's IP address or domain.

   - You should see the website running live.


## Testing

Both manual and automated testing was used in order to fully test the functionality and useability of the new web application. Combinging both allowed me do achieve a well rounded test on both UXI and funcationality.

Testing was done under local deployment and remote deployment to a hosted server to mimic final production deployment.

### Manual Testing

Throughout the course of the build phase, I periodically checked the features in order to ensure they operated as the client required.
As well as this, once each module was able to operate to a satifactory standard, I had several members of the staff who would be end users test out the module. This gave me quick feedback from the client, in terms of not only function, but also user experience. Allowing me to make any design changes as the build progressed.

The following is how the initial user stories compare against the final testing.

### As a user
   > I want a clear view of all the case files and wether they are open or closed. I want to be able to access each case in as few clicks as possible, and easily create and update case files as needed.
#### Tests
   - Use the menu to browse to the cases page, visually see from the list which cases are open or closed.
   - Filter the cases by either open or closed status.
   - Click on the link next to the case to go to the update page and update the details for that case.
#### Results
   - Users confirmed each step of the process worked to a clear and satisfactory manor. They were able to create and modify cases successfully.

### As a user
   > I want to be able to create and modify user accounts, and set the required access levels for that user.
#### Tests
   - Use the menu to browse to the users page.
   - Select which user needs to be updated.
   - Modify permissions and details.
   - Create a new user and supply the required permissions.
#### Results
   - Users confirmed each step of the process worked to a clear and satisfactory manor.

### As a user
   > I want to be able to generate an invoice from a case file, and edit the invoices as required. I want to be able to easily view and change the status of an invoice.
#### Tests
   - Use the menu to browse to the invoice page.
   - Create a new invoice by selecting a case file.
   - Select and existing invoice to update the status on.
#### Results
   - Users confirmed each step of the process worked to a clear and satisfactory manor, they were able to create a new invoice and update an existing invoice from sent to paid.

### As a customer
   > I want to be able to make a payment for any invoices easily online.
#### Tests
   - Register for an account
   - Sign in to the account
   - Select and invoice to pay.
#### Results
   - Acting as a customer, users confirmed each step of the process worked to a clear and satisfactory manor. They were able to select and pay for an invoice.

### As a customer
   > I want to be able to create an account to keep track of any fines or notices, along with any payments I have made or need to make.
#### Tests
   - Register for an account
   - Sign in to the account
   - View any invoices, and see wether they have been paid or are due.
   - Select and invoice to pay.
   - View my past payments.
#### Results
   - Acting as a customer, users confirmed each step of the process worked to a clear and satisfactory manor. They could create and view any previous payments.

### Automated Testing

Using Django's testing framework I carried out serval unit tests on the key operations of the site, such as Authentication and CRUD functions for each module.
These tests can be ran under local deployment using the relevant python command for your cli followed by manage.py tests.
Each modules tests are located in their respective tests.py file.

### Browser Testing

Due to the specific user and use case of this project, I know that all users will be using the web application on Windows desktop, using either Chrome or Edge browsers.
Still in order to keep the site as usable as possible, I have made sure that any frameworks used are all compatable with the current versions of all major browsers; i.e. Chrome, Edge, Firefox, Safari etc.
I also made it a key point to ensure that the layout was responsive as per the inital design ideas. This allows a user to quickly log in and view/edit data if they are away from the desk or out of the office.
In order to meet theses standard, I continualy tested browser support and responsiveness as the website was being built.

### Code validation

The following validators were used during final testing to ensure all code was up to standards;

- Javascript - [JSHint](https://jshint.com/)
- Python - [Flake8 VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8)
- CSS - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- HTML - [W3C HTML Validator](https://validator.w3.org/)

**Note:** W3C's HTML Validator dosen't play well with Django's HTML template langauge, so after pasting in the code, I purposfully ignored some of the errors and only paid attention to the ones directly relating to the HTML launage and formatting.

As this was built specificaly for an end client and their end user requirements, I didn't feel the need to pass this through Googles Lighthouse.

## Known issues & Bugs

While there are currently no known issues, several bugs were found during the build. These were picked up by myself during coding the site and some were picked up by the users during testing.
These mostly stemned from incorrect code syntax and the calls to functions before data was readily available. 
These were fixed as they were found in order to avoid any larger issues devloping.
I originally want to use a uuid to generate a customer reference, but limit it to specific number of characters, however I could not get shortUUID to work and opted to use the customers intitals along with a datetime stamp.

## Final screenshots

**Dashboard**

<img src="/docs/screenshots/dashboard.png" width="800">

**Client List**

<img src="/docs/screenshots/clients-list.png" width="800">

**New Case**

<img src="/docs/screenshots/new-case.png" width="800">

**Invoice List**

<img src="/docs/screenshots/invoice-list.png" width="800">

**Create Invoice**

<img src="/docs/screenshots/create-invoice.png" width="800">

**Edit User**

<img src="/docs/screenshots/edit-user.png" width="800">


## Future Enhancements

Speaking with the client, they are very happy with the final delivery. We have had disscussions about adding in additional features.

One of the key areas they would like to expand on, is having a reports module that would allow them to generate various reports based of the KPI's and data held within the system.