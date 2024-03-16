-- User table
CREATE TABLE Employee (
    id VARCHAR(10) PRIMARY KEY,
    Fname VARCHAR(255) NOT NULL,
	Lname VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    department VARCHAR(20) NOT NULL,
    salary VARCHAR (12) NOT NULL,
    contact CHAR(12) UNIQUE NOT NULL
);

-- Salary Record table
CREATE TABLE Salary_Record (
    employee_id VARCHAR(10) REFERENCES Employee(id) on delete cascade on update cascade,
    date_ DATE,
    amount INT,
    deduction INT,
    total INT,
    PRIMARY KEY (employee_id, date_)
);

-- Leave Record table
CREATE TABLE Leave_Record (
    leave_id SERIAL PRIMARY KEY,
    employee_id VARCHAR(10) REFERENCES Employee(id) on delete cascade on update cascade,
    start_date DATE UNIQUE NOT NULL,
    end_date DATE UNIQUE NOT NULL,
    description TEXT,
    category VARCHAR(20),
    status VARCHAR(20) CHECK (status IN ('accepted', 'rejected', 'pending'))
);

-- Attendance table
CREATE TABLE Attendance (
    employee_id VARCHAR(10) REFERENCES Employee(id) on delete cascade on update cascade,
    date_ DATE,
    status VARCHAR(20) CHECK (status IN ('P', 'A')),
    PRIMARY KEY (employee_id, date_)
);

-- Sample insertions for the Employee table with Pakistani data
INSERT INTO Employee VALUES
(1001, 'Ali',  'Khan', 'ali.khan@example.com', 'pass123', '123 Main Street, Karachi', 'sales', 50000.00, '0321-1234567'),
(1002, 'Sana', 'Ahmed', 'sana.ahmed@example.com', 'securepass', '456 Market Street, Lahore', 'marketing', 60000.00, '0333-9876543'),
(1003, 'Amir', 'Malik', 'amir.malik@example.com', 'password123', '789 Business Street, Islamabad', 'accounts', 55000.00, '0312-3456789'),
(1004, 'Farah', 'Khan', 'farah.khan@example.com', 'mypassword', '987 Avenue Street, Karachi', 'finance', 70000.00, '0344-5678901'),
(1005, 'Nida','Shah', 'nida.shah@example.com', 'mypass', '654 Park Street, Lahore', 'research', 65000.00, '0322-3456789'),
(1006, 'Saad', 'Ahmed', 'saad.ahmed@example.com', 'topsecret', '321 Plaza Street, Islamabad', 'HR', 75000.00, '0311-2345678');

INSERT INTO Salary_Record VALUES
(1001, '2023-11-01', 50000, 2*(50000/30.0), 50000-2*(50000/30.0)),
(1001, '2023-12-01', 50000, 4*(50000/30.0), 50000-4*(50000/30.0));

-- Sample insertions for Attendance table for employee with 'id 1001'
INSERT INTO Attendance (employee_id, date_, status)
VALUES
    -- October
    ('1001', '2023-10-02', 'P'),
    ('1001', '2023-10-03', 'P'),
    ('1001', '2023-10-04', 'P'),
    ('1001', '2023-10-05', 'P'),
    ('1001', '2023-10-06', 'P'),

    ('1001', '2023-10-09', 'P'),
    ('1001', '2023-10-10', 'P'),
    ('1001', '2023-10-11', 'P'),
    ('1001', '2023-10-12', 'P'),
    ('1001', '2023-10-13', 'P'),

    ('1001', '2023-10-16', 'P'),
    ('1001', '2023-10-17', 'A'),
    ('1001', '2023-10-18', 'P'),
    ('1001', '2023-10-19', 'P'),
    ('1001', '2023-10-20', 'A'),

    ('1001', '2023-10-23', 'A'),
    ('1001', '2023-10-24', 'P'),
    ('1001', '2023-10-25', 'P'),
    ('1001', '2023-10-26', 'P'),
    ('1001', '2023-10-27', 'P'),

    ('1001', '2023-10-30', 'P'),
    ('1001', '2023-10-31', 'P'),

    -- November
    ('1001', '2023-11-01', 'P'),
    ('1001', '2023-11-02', 'P'),
    ('1001', '2023-11-03', 'A'),

    ('1001', '2023-11-06', 'A'),
    ('1001', '2023-11-07', 'P'),
    ('1001', '2023-11-08', 'P'),
    ('1001', '2023-11-09', 'P'),
    ('1001', '2023-11-10', 'A'),

    ('1001', '2023-11-13', 'P'),
    ('1001', '2023-11-14', 'P'),
    ('1001', '2023-11-15', 'P'),
    ('1001', '2023-11-16', 'P'),
    ('1001', '2023-11-17', 'P'),

    ('1001', '2023-11-20', 'P'),
    ('1001', '2023-11-21', 'P'),
    ('1001', '2023-11-22', 'A'),
    ('1001', '2023-11-23', 'P'),
    ('1001', '2023-11-24', 'P'),

    ('1001', '2023-11-27', 'P'),
    ('1001', '2023-11-28', 'A'),
    ('1001', '2023-11-29', 'P'),
    ('1001', '2023-11-30', 'P'),

    -- December
    ('1001', '2023-12-01', 'P'),

    ('1001', '2023-12-04', 'A'),
    ('1001', '2023-12-05', 'P');
	

-- Sample input for Leave_Record table for employee with 'id 1001'
INSERT INTO Leave_Record (employee_id, start_date, end_date, description, category, status)
VALUES
    ('1001', '2023-10-17', '2023-10-17', 'Vacation', 'general', 'accepted'),
    ('1001', '2023-11-03', '2023-11-06', 'Family event', 'general', 'rejected'),
    ('1001', '2023-12-04', '2023-12-04', 'Sick leave', 'health', 'pending');


