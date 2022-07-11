# Library
# Author : Anil Yalala

# Concepts and Technologies

    Project Management - Trello
    Python Fundamentals
    Python Testing - Pytest
    Version Control - Git
    Linux - Ubuntu
    Python Web Development
    Databases - MySQL Database for Azure
    Continuous Integration and Deployment (CI/CD) - Jenkins
    Cloud Fundamentals - Azure
    Containerisation Docker
    Deployment - Docker Swarm
    
# Project

The objective of this project is to achieve the following:

    - Create a Web Application that integrates with a Database and demonstrates CRUD functionality.
    - Utilise Containers to host and deploy the application.
    - Create a Continuous Integration (CI)/Continuous Deployment (CD) pipeline that will automatically test, build and deploy the application.

# Application

I have choosen to create a Library web application using Flask application that serves both the frontend and backend of the application. The frontend aspect of the app will use HTML templates to serve the web pages that allow the user to perform CRUD functionality with information from the database. The backend aspect of the application will use SQLAlchemy to model and integrate with MySQL database. This application will be hosted in a container to allow it to be deployed to a Docker Swarm.

![Untitled Diagram-Page-1 drawio](https://user-images.githubusercontent.com/105712346/178278022-e4f600a1-6af8-4ed0-a39d-2398c481888d.png)

# Database

I am using MySQL database to store the user input data and to retrive the data when needed. I have designed the database to have two tables one is Books Table and another is Authors table. These two tables will have a one-to-many relationship

![Database 2](https://user-images.githubusercontent.com/105712346/178298212-f4d97281-dc97-4813-9117-3473c985e601.png)

