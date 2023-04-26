# STG-TEAM1-SolarSystem - Final Assignment

SolarSystem app created

Parts of Final Assignment:
  1. Created Rest API endpoints to receive, create, delete and update information.
  2. Created MySQL DB.
  3. Created Docker compose file and Dockerfiles to create two dicker containers:
      - one to deploy Python application;
      - decond one to deploy MySQL server.
  4. Created Terraform script, which created an instance, which runs Ansible playbook automatically.
  5. Created Ansible playbook to:
      - create a new user on the instance;
      - run updates on the instance;
      - install Docker on the instance;
      - download all content from GitHub repository;
      - run two containers: MySQL DB and Python applications;
      - restore MySQL DB from the dump;
      - delete all downloaded repository information from the instande.
    

