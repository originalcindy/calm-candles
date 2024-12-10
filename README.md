# **Calm Candles**

**Calm Candles** was originally created as a Bi weekly blog which posted candle frangrance combinations as well as how to tutorials for its readers. The blog became so popular and received so many messages for sales of the products featured that the owners decided to create a shop.

## Table of Contents
1. [Introduction](#introduction)
2. [Overview](#overview)
3. [UX - User Experience](#ux---user-experience)
    - [Design Inspiration](#design-inspiration)
    - [Colour Scheme](#colour-scheme)
    - [Font](#font)
4. [Project Planning](#project-planning)
    - [Strategy Plane](#strategy-plane)
    - [Site Goals](#site-goals)
    - [Agile Methodologies - Project Management](#agile-methodologies---project-management)
    - [MoSCoW Prioritization](#moscow-prioritization)
    - [Sprints](#sprints)
    - [User Stories](#user-stories)
5. [Scope Plane](#scope-plane)
6. [Structural Plane](#structural-plane)
7. [Skeleton & Surface Planes](#skeleton--surface-planes)
    - [Wireframes](#wireframes)
8. [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
9. [Security](#security)
10. [Features](#features)
    - [User View - Registered/Unregistered](#user-view---registeredunregistered)
    - [Role-Based Dashboard Features](#role-based-dashboard-features)
    - [Role-Based Navigation](#role-based-navigation)
    - [Soft Delete/Archiving for Patient Accounts](#soft-deletearchiving-for-patient-accounts)
    - [Appointment Booking System](#appointment-booking-system)
    - [Messaging System](#messaging-system)
    - [Profile Management](#profile-management)
    - [Confirmation Messages](#confirmation-messages)
    - [CRUD Functionality](#crud-functionality)
    - [Feature Showcase](#feature-showcase)
11. [Future Features](#future-features)
12. [Technologies & Languages Used](#technologies--languages-used)
13. [Libraries & Frameworks](#libraries--frameworks)
14. [Tools & Programs](#tools--programs)
15. [Testing](#testing)
  - [Validation Testing](#validation-testing)
  - [User Testing](#user-testing)
  - [Bugs](#bugs)
16. [Deployment](#deployment)
    - [Connecting to GitHub](#connecting-to-github)
    - [Django Project Setup](#django-project-setup)
    - [Cloudinary API](#cloudinary-api)
    - [PostgreSQL](#postgresql)
    - [Heroku deployment](#heroku-deployment)
    - [Clone project](#clone-project)
    - [Fork Project](#fork-project)
17. [Privacy Policy](#privacy-policy)
18. [Credits](#credits)
    - [Code](#code)
    - [Media](#media)
    - [Additional reading/tutorials/books/blogs](#additional-readingtutorialsbooksblogs)
19. [Acknowledgements](#acknowledgements)

## Overview
Calm Candles is an online blog turned ecommerce shop that allows users to: 
- register and create a profile
- view the catalogue of candles available
- add items to a basket and purchase
- contact us via a form

## UX - User Experience

### Design Inspiration
My inspiration for Calm Candles came from my joy of making candles  .I thought about how many medical consultations, especially those that don’t require physical examinations, could easily be handled online. This thought extended to pregnant women, who often need guidance and reassurance from their midwives or doctors but don’t necessarily need an in-person visit. The convenience of a digital platform for such consultations became clear. The name HealMate reflects the idea of a supportive, reliable partner in managing one's health—much like popular health apps such as ClueMate, where ‘Mate’ signifies companionship and guidance in managing health.

### Colour Scheme
![alt text](<static/images/colour scheme calm candles.png>)
In line with the healthcare theme, I chose a neutral, clean palette:
- **Primary Color:** #17A2B8 (Navy Blue-Grey)
- **Secondary Color:** #132B67 (Hospital Blue)
- **Accent Color:** #333 (grey)
- **Background:** #fff (White)
This combination ensures clarity, accessibility, and a professional appearance, allowing for easy navigation throughout the site.

### Font
- For the logo and headers, I will be using **Lora**.
- The rest of the body text and interactive elements will use **Catamaran** for its readability and clean look.

## Project Planning

### Strategy Plane
The primary objective of Calm Candles is to bring together an informative blog about candle creation and ecommerce. By offering an intuitive interface, users can easily buy candles safely and seamlessly from a trusted company who beleive in high quality. 

### Site Goals
- Provide customers with a user-friendly platform to buy candles.
- Allow customers to register a username so they can track their orders with ease.
- Offer an intuitive interface with role-based dashboards for admins.

### Agile Methodologies - Project Management
I used an agile approach to project management. The HealMate development process was broken into sprints, and tasks were added to the GitHub project board to be tracked and managed through issues.

### MoSCoW Prioritization
- **Must-Haves:** User registration and login, specialist search, appointment booking, role-based dashboards.
- **Should-Haves:** Feedback system, health tools, advanced filtering options.
- **Could-Haves:** Profile pictures for users and specialists, messaging system.
- **Won’t-Haves:** Full payment integration, doctor-patient messaging for now.

### Sprints
- **Sprint 1:** Initial Setup - Project, repository, environment setup.
- **Sprint 2:** User Authentication & Role-Based Dashboards.
- **Sprint 3:** Specialist Search & Appointment Booking System.
- **Sprint 4:** Static Pages & UI/UX Improvements.
- **Sprint 5:** Deployment & Testing.

## User Stories
- As a user (customer/admin), I want to register and log in securely so that I can access my dashboard and manage my activities.
- As a user, I want a personalized dashboard based on my role (patient, doctor, admin) so that I can access the features relevant to me.
- As a visitor, I want to see a well-designed home page that introduces HealMate so that I understand the platform's purpose and value.
- As a patient, I want to search for specialists by category (e.g., Dermatologist, Psychologist) so that I can find a doctor that meets my needs.
- As a patient, I want to view available time slots for a specialist and book an appointment, so that I can get medical advice and treatment.
- As a patient, I want to message my doctor before or after a consultation so that I can ask follow-up questions or clarify doubts.
- As a specialist, I want to manage my schedule and view patient appointments so that I can efficiently conduct consultations.

## Scope Plane
The HealMate platform will include the following MVP functionalities:
- User registration and role-based dashboards.
- Search and filtering system for specialists.
- Appointment scheduling with available specialists.
- Specialist profiles showcasing specialty, experience, and availability.

## Structural Plane
The site is structured around an easy-to-use interface. The primary menu includes links to specialist searches, appointment bookings, and user profile management.

## Skeleton & Surface Planes

### Wireframes
Wireframes were created for the following key pages to ensure an intuitive user journey:
- **Home Page**

mobile home page view

![alt text](<static/images/New Wireframe 1.png>)

Tablet home page view

![alt text](<static/images/calm candles tablet design home page.png>)

Desktop home page view

![alt text](<static/images/calm candles website design home page.png>)



- **Specialist Search Results**

![Homepage Wireframe](docs/wireframe/search-result-large-screen.png)

![Homepage Wireframe](docs/wireframe/search-result-mobile.png)

- **Appointment Booking**

![Homepage Wireframe](docs/wireframe/booking-page-large-screen.png)

![Homepage Wireframe](docs/wireframe/booking-page-mobile.png)

- **User Dashboards** (Patient and Specialist)
- **Admin Panel**

Wireframes were designed using [Balsamiq](https://balsamiq.com/), ensuring responsiveness across devices.

## Database Schema - Entity Relationship Diagram
The ERD for HealMate illustrates the relationships between the users, specialists, appointments, and more. This is essential to demonstrate the relationships between the different models in the PostgreSQL database.

The ERD also demonstrates the platform's role-based structure. Each user is assigned to a specific group (patient, specialist, or admin) that determines their access level. PatientProfile and SpecialistProfile models are linked to the User model, and each profile type has specific fields relevant to their role. Admins have broader access to manage both specialist vetting and platform data.

![ERD Illustration](docs/erd/erd-healmate.png)

The above ERD was generated using Python Extension - pygraphviz and pydotplus. Documentation at https://django-extensions.readthedocs.io/en/latest/graph_models.html.

## Security
All data is securely handled with Django’s security features, including:
- CSRF protection for form submissions.
- Data encryption for sensitive information like passwords using Django's built-in authentication.
- Role-based access control to restrict sensitive data to authorized users.

Role-based access control (RBAC) is implemented using Django's Group and Permission systems. Patients, specialists, and admins are grouped based on their role, and their access to features and sensitive information is restricted accordingly. Patients can only access their own medical data and booking history, while specialists can only view data related to their consultations. Admins have the broadest access for system management.