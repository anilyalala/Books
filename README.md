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
    - Create a Continuous Integration (CI)/Continuous Deployment (CD) pipeline 
      that will automatically test, build and deploy the application.

# Application

I have choosen to create a Library web application using Flask application that serves both the frontend and backend of the application. The frontend aspect of the app will use HTML templates to serve the web pages that allow the user to perform CRUD functionality with information from the database. The backend aspect of the application will use SQLAlchemy to model and integrate with MySQL database. This application will be hosted in a container to allow it to be deployed to a Docker Swarm.

![Untitled Diagram-Page-1 drawio](https://user-images.githubusercontent.com/105712346/178278022-e4f600a1-6af8-4ed0-a39d-2398c481888d.png)

# Database

I am using MySQL database to store the user input data and to retrive the data when needed. I have designed the database to have two tables one is Books Table and another is Authors table. These two tables will have a one-to-many relationship

![Database 3](https://user-images.githubusercontent.com/105712346/178305565-a905da68-f38e-426f-bc45-cc7f3b2761c6.png)

# CI/CD Pipeline

I am creating a CI/CD pipeline that will automate the integration and deployment of new code. I am using Jenkins for automation server. A CI/CD pipeline automates the process of software delivery. It builds code, runs tests, and helps to safely deploy a new version of the software. Every time I push new code in my GitHub repository, the pipeline should be triggered. This can be achieved using a GitHub Webhook. The main aim of CI/CD pipeline is to achieve:

    - Run unit tests.
    - Build the Docker images.
    - Push the Docker images to a registry.
    - Deploy to a Swarm.
    
![CICD](https://user-images.githubusercontent.com/105712346/178314600-039fc219-1d4c-4d62-8624-e3125bc4270f.png)

# Project Management - Trello

