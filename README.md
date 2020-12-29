## Attendance Control System using RDS-MySQL directly from the AWS cloud
The algorithm consists of a control system for offices via the PyQt5 graphical interface, connected to an RDS-MySQL database directly from the AWS cloud, without the need for a local server. The system allows the control of the activities / services performed in an office in a simple and easy way, allowing to perform service registration, consultations based and by item the choice of the professional.

## Requirements
You will need to install the library below:
- mysql-connector
- PyQt5

## Creating RDS-MySQL instance
- Access the "AWS Management Console"
- Open the services menu and select the RDS option
- Select the "Create database" option
- Select MySQL
- Version: MySQL 8.0.11
-> Free tier
- Enter the basic data, username and password:

db instance: "database name"

username: "your username"

password: "your password"

- DB instance size and Storage is default not to mess
- VPC: Default
- Subnet group: default
- Public access: Yes
- VPC security group: Create new

New VPC security group name: <enter_com_the_name>

- Availability Zone: choose where you are connected


## Home screen
When opening the interface, the following options are presented:
- Register: Allows you to register a new service in the cloud database.
- Consult: Allows you to consult the service history performed.
- Search: Allows you to search for a specific record through pre-defined fields.

![1](https://user-images.githubusercontent.com/40063504/102730553-dc09c700-4313-11eb-8f77-c8bff9356711.PNG)

## Registration screen
- Initial registration screen

![2](https://user-images.githubusercontent.com/40063504/102730555-df04b780-4313-11eb-9820-b56c3fc1fee8.PNG)

- Registration screen filled. By clicking on "Insert Data" the registered data will automatically go to the RDS database in the cloud.

![3](https://user-images.githubusercontent.com/40063504/102730559-e1671180-4313-11eb-8f32-8503ac5f7cab.PNG)

## Base query screen
- When we click "Consult" the interface brings the entire service history to the user.

![4](https://user-images.githubusercontent.com/40063504/102730563-e3c96b80-4313-11eb-9c37-cf54331cf0db.PNG)

## Search screen by item
- In this screen we can perform a search with filters through the checkboxes and the fields.

![5](https://user-images.githubusercontent.com/40063504/102730587-edeb6a00-4313-11eb-9b48-e8442ebd5798.PNG)

- Search result by item.

![4](https://user-images.githubusercontent.com/40063504/102730593-f17ef100-4313-11eb-8691-144634cae76d.PNG)
