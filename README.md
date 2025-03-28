# Inventory Management System

Deployment Link
[https://inventory-management-my-app-2ca5c492a94f.herokuapp.com/]

# Overview

The Inventory Management System is a web application developed using Django, Python, and deployed on Heroku. The purpose of this project is to provide an efficient solution for managing inventory, tracking stock levels, and ensuring that items are readily available when needed. It solves the problem of manual inventory tracking and helps businesses streamline their operations, saving time and reducing errors.

# User Stories:

Modify or delete a post:

As a Site User I can modify or delete my comment on a post so that I can be involved in the conversation

AC1 Given a logged in user, they can modify their comment
AC2 Given a logged in user, they can delete their comment

View Inventory Item: 

As a site user, I can view a paginated list of inventory items so that I can select which item I want to view.

Acceptance Criteria:

AC1: Given more than one inventory item in the database, these multiple items are listed.
AC2: When a user opens the main page, a list of inventory items is seen.
AC3: The user sees all inventory item names with pagination to choose what to view.

Add Inventory Item:

As an inventory manager, I can add a new inventory item so that the inventory system stays updated.

Acceptance Criteria:

AC1: Given a form to add a new inventory item, the form includes fields for item name, quantity, and location.
AC2: When a user submits the form with valid data, the item is added to the inventory.
AC3: The user receives a confirmation message upon successfully adding the item.

Update Inventory Item:

As an inventory manager, I can update existing inventory items so that the inventory details remain accurate.

Acceptance Criteria:

AC1: Given a list of inventory items, each item has an "Edit" button.
AC2: When a user clicks the "Edit" button, they are taken to a form pre-filled with the item's current details.
AC3: The user can modify the details and save the changes, which updates the item in the inventory.

Delete Inventory Item:

As an inventory manager, I can delete an inventory item so that the inventory system stays clean and relevant.

Acceptance Criteria:

AC1: Given a list of inventory items, each item has a "Delete" button.
AC2: When a user clicks the "Delete" button, they are asked to confirm the deletion.
AC3: Upon confirmation, the item is removed from the inventory and the user sees a success message.


# UX Design Process

# Agile

Link to User Stories in GitHub Projects:
[https://github.com/users/Hodoo08/projects/4]

In designing my inventory management system, I applied Agile development principles even as a solo developer to stay organised and adaptive throughout the project. I structured my work into iterative cycles, focusing on smaller, manageable tasks that allowed for continuous progress. By frequently reflecting on completed features and identifying areas for improvement, I was able to refine the system incrementally. Regular self-reviews helped me stay aligned with the project's goals and adjust to challenges as they arose. This Agile approach ensured that I delivered a robust and user-focused solution efficiently, even while working independently.


# Wireframes:

![wireframes](static/images/New%20Wireframe%201.png)
![wireframes](static/images/New%20Wireframe%202.png)

# Design Rationale:

The layout and design choices were made with a focus on usability and accessibility. Key design decisions included a clean and simple interface, high contrast colors for readability, and a responsive design to ensure accessibility on various devices. Accessibility guidelines (e.g., WCAG) were integrated.
I opted for a sandstone theme from bootswatch which is a simple theme with a touch of warmth that attracts users.

# Reasoning For Any Final Changes:

During development, significant changes were made to enhance the user interface's inclusivity and accessibility. For example, adjustments were made to improve keyboard navigation and ensure all interactive elements are accessible to screen readers. These changes enhance the overall user experience.

# Key Features

Feature 1: View Inventory Items
Users can view a paginated list of inventory items, making it easy to navigate through large inventories.

Feature 2: Add Inventory Item
Inventory managers can add new items to the inventory, ensuring the system stays updated.

Feature 3: Edit Inventory Item
Inventory managers are able to edit already listed items, by changing and keeping up to date with the quantity of listed inventory items.

Feature 4: Delete Inventory Item
Users are able to delete inventory items via their disgression. Gives users the flexibilty to delete out of stock inventory. This adheres to one of CRUD functionality features.

Feature 5: Low Stock Alert
Whenever an inventory item is below 3, i have added a feature where an alert message will pop up and notify the user that their inventory stock is running low. I have also made it so that when the item is low and is visiable on the dashboard that the quantity number is displayed in red.


# Deployment
Platform: Heroku

High-Level Deployment Steps:

Step 1: Set up a Heroku account and create a new app.

Step 2: Configure the Django application for Heroku deployment, including setting up the Procfile and necessary environment variables.

Step 3: Deploy the application using Git and Heroku CLI.

Verification and Validation:
Steps were taken to verify that the deployed version matches the development version in functionality. Additional checks were conducted to ensure the accessibility of the deployed application.

# Security Measures:

Environment variables are used for sensitive data.
DEBUG mode is disabled in production.
AI Implementation and Orchestration


# Code Creation: 
AI was used for rapid prototyping, with minor adjustments for alignment with project goals. Examples include using reverse prompts for alternative code solutions and question-answer prompts for resolving specific challenges.

# Debugging: 
AI tools were instrumental in resolving logic errors and enhancing maintainability, with a focus on simplifying complex logic to make it accessible. I was able to input error messages into co pilot and was able to pin point the error therefore resolving any issues swiftly.

# Performance and UX Optimization: 
AI-driven improvements were applied to enhance application speed and user experience for all users.
Automated Unit Testing: 
Adjustments were made to improve test coverage and ensure alignment with functionality. Prompts were used to generate inclusive test cases that considered edge cases for accessibility.

# AI Implementation:
AI tools streamlined repetitive tasks, enabling focus on high-level development. Efficiency gains included faster debugging, comprehensive testing, and improved code quality. Challenges included contextual adjustments to AI-generated outputs, which were resolved effectively, enhancing inclusivity.

# Testing Summary

# Manual Testing:

I successfully created test_forms for both my models and views. I initiated prompts from co-pilot to assist me in this process.


I used Devtool Lighthouse to conduct testing, outcome below:
![Lighthouse Test](static/images/LightHouse%20Testing.png)

I tested My HTML via the HTML validator, Find report below:
![HTML Validation](static/images/HTML%20validator.png)

I also tested my CSS via the CSS Validator, find report below:
![CSS Validation](static/images/CSS%20validator.png)

# Devices and Browsers Tested: 

The application was tested on various devices and browsers, ensuring testing was conducted with assistive technologies such as screen readers and keyboard-only navigation.

Features Tested: 
CRUD operations, navigation, and accessibility features were tested manually.
Results: All critical features worked as expected, including accessibility checks.


# Tools Used:

Django TestCase and other testing frameworks.
Features Covered: CRUD operations, authentication, and accessibility checks.

# Adjustments Made: 

Manual corrections were made to AI-generated test cases, particularly for accessibility.

# Future Enhancements:

Consider adding voice input capabilities for improved accessibility.
Implement additional language support to cater to a broader audience.

Add reporting features to provide more detailed insights into inventory trends.
