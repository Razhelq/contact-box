# contact-box

contact-box django based web application.

This application was created to store people's contact details in pre-created groups. 

For a first time I created a model which can store a picture.
This picture has to be displayed inside a contact card and has an option to change. 
Also this time I used classes instead of functions in views.

The application contains:
1. Models:
    - Person (can store a picture)
    - Address with one to many relation to Person model as there can be more than one address
    - Phone with one to many relation to Person model as there can be more than one phone number
    - Email with one to many relation to Person model as there can be more than one email address
    - Group with many to many relation to Person model
2. Classes:
    - to create, modify, delete a person and display a contact card
    - to add new email, phone number and address
    - to create, delete a group and to add, remove person from it
    - to display a group and search for a person inside it    
3. Separated html templates for almost every action.
4. Cooperation with PostgreSQL database.
5. Separated file for local settings.


For the front-end side I used basic bootstrap css theme to have a top menu and the container below. 
In the future I will improve this part.



