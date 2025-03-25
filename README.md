# Inventory Management System

# Overview

The Inventory Management System is a web application developed using Django, Python, and deployed on Heroku. The purpose of this project is to provide an efficient solution for managing inventory, tracking stock levels, and ensuring that items are readily available when needed. It solves the problem of manual inventory tracking and helps businesses streamline their operations, saving time and reducing errors.

# UX Design Process

Link to User Stories in GitHub Projects:
GitHub Projects Kanban Board

# Wireframes:

[Attach or link to accessible wireframes used in the design process, ensuring high colour contrast and alt text for visual elements.]

# Design Rationale:

The layout and design choices were made with a focus on usability and accessibility. Key design decisions included a clean and simple interface, high contrast colors for readability, and a responsive design to ensure accessibility on various devices. Accessibility guidelines (e.g., WCAG) were integrated, and considerations were made for users with disabilities, such as screen reader support.

# Reasoning For Any Final Changes:

During development, significant changes were made to enhance the user interface's inclusivity and accessibility. For example, adjustments were made to improve keyboard navigation and ensure all interactive elements are accessible to screen readers. These changes enhance the overall user experience, especially for users with disabilities.

# Key Features

Feature 1: View Inventory Items
Users can view a paginated list of inventory items, making it easy to navigate through large inventories.

Feature 2: Add Inventory Item
Inventory managers can add new items to the inventory, ensuring the system stays updated.

Inclusivity Notes:
The features were designed to address the needs of diverse users, including those with Special Educational Needs and Disabilities (SEND). The interface supports screen readers, and high contrast themes are available for users with visual impairments.

# Deployment
Platform: Heroku

# High-Level Deployment Steps:

Step 1: Set up a Heroku account and create a new app.
Step 2: Configure the Django application for Heroku deployment, including setting up the Procfile and necessary environment variables.
Step 3: Deploy the application using Git and Heroku CLI.
Verification and Validation:
Steps were taken to verify that the deployed version matches the development version in functionality. Additional checks were conducted to ensure the accessibility of the deployed application.

# Security Measures:

Environment variables are used for sensitive data.
DEBUG mode is disabled in production.
AI Implementation and Orchestration

Use Cases and Reflections:

# Code Creation: 
AI was used for rapid prototyping, with minor adjustments for alignment with project goals. Examples include using reverse prompts for alternative code solutions and question-answer prompts for resolving specific challenges.

# Debugging: 
AI tools were instrumental in resolving logic errors and enhancing maintainability, with a focus on simplifying complex logic to make it accessible.

# Performance and UX Optimization: 
AI-driven improvements were applied to enhance application speed and user experience for all users.
Automated Unit Testing: Adjustments were made to improve test coverage and ensure alignment with functionality. Prompts were used to generate inclusive test cases that considered edge cases for accessibility.

# Overall Impact:
AI tools streamlined repetitive tasks, enabling focus on high-level development. Efficiency gains included faster debugging, comprehensive testing, and improved code quality. Challenges included contextual adjustments to AI-generated outputs, which were resolved effectively, enhancing inclusivity.

# Testing Summary

# Manual Testing:

# Devices and Browsers Tested: 

The application was tested on various devices and browsers, ensuring testing was conducted with assistive technologies such as screen readers and keyboard-only navigation.
Features Tested: CRUD operations, navigation, and accessibility features were tested manually.
Results: All critical features worked as expected, including accessibility checks.
Automated Testing:

# Tools Used:

Django TestCase and other testing frameworks.
Features Covered: CRUD operations, authentication, and accessibility checks.

# Adjustments Made: 

Manual corrections were made to AI-generated test cases, particularly for accessibility.

# Future Enhancements:

Consider adding voice input capabilities for improved accessibility.
Implement additional language support to cater to a broader audience.
Enhance the reporting features to provide more detailed insights into inventory trends.
