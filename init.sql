-- Create a new database
CREATE DATABASE IF NOT EXISTS user_data;

-- Use the newly created database
USE user_data;

-- Create a new table
CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    message text not null
);

-- Insert initial data into the table
INSERT INTO contacts (name, email, message) VALUES ('Harsh Kumar', 'harshkumar084834@gmail.com', ('Hi Harsh Kumar'));

