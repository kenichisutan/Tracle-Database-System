DROP TABLE IF EXISTS Students, Courses, Semester, Class, Attendance;
CREATE TABLE Students (
	ID INTEGER NOT NULL AUTO_INCREMENT,
    First_Name VARCHAR(30),
    Last_Name VARCHAR(30),
    Gender CHAR(1),
    Email VARCHAR(30) NOT NULL,
    Address VARCHAR(80) NOT NULL,
    Credits INTEGER,
    Current_Status VARCHAR(20),
    Major VARCHAR(20),
    CONSTRAINT PK_Students PRIMARY KEY(ID)
);
ALTER TABLE Students AUTO_INCREMENT = 910000001;

CREATE TABLE Courses (
	ID INTEGER NOT NULL AUTO_INCREMENT,
    Title VARCHAR(60) NOT NULL,
    Credits INTEGER NOT NULL,
    Department VARCHAR(30) NOT NULL,
    CONSTRAINT PK_Courses PRIMARY KEY(ID)
);
ALTER TABLE Courses AUTO_INCREMENT = 1;

CREATE TABLE Semester (
	Semester_ID INTEGER NOT NULL AUTO_INCREMENT,
    Semester VARCHAR(30) NOT NULL,
    Offered_Year INTEGER,
    CONSTRAINT PK_Semester PRIMARY KEY(Semester_ID),
    CONSTRAINT Natural_PK_Semester UNIQUE (Semester, Offered_Year)
);
ALTER TABLE Semester AUTO_INCREMENT = 1;

CREATE TABLE Class (
	Class_ID INTEGER NOT NULL AUTO_INCREMENT,
    Semester_ID INTEGER NOT NULL,
	Course_ID INTEGER NOT NULL,
    Days VARCHAR(10) NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL,
    CONSTRAINT PK_Class PRIMARY KEY(Class_ID),
    CONSTRAINT FK_Class_Course FOREIGN KEY(Course_ID) REFERENCES Courses(ID),
    CONSTRAINT FK_Class_Semester_ID FOREIGN KEY(Semester_ID) REFERENCES Semester(Semester_ID)
);
ALTER TABLE Class AUTO_INCREMENT = 1;

CREATE TABLE Attendance (
	Attendance_ID INTEGER NOT NULL AUTO_INCREMENT,
	Student_ID INTEGER NOT NULL,
    Class_ID INTEGER NOT NULL,
    Present INTEGER NOT NULL,
    Attendance_Date DATE NOT NULL,
    CONSTRAINT PK_Attendance PRIMARY KEY(Attendance_ID),
    CONSTRAINT Natural_PK_Attendance UNIQUE (Student_ID, Class_ID, Attendance_Date),
    CONSTRAINT FK_Attendance_Students FOREIGN KEY(Student_ID) REFERENCES Students(ID),
    CONSTRAINT FK_Attendance_Class FOREIGN KEY(Class_ID) REFERENCES Class(Class_ID)
);
ALTER TABLE Attendance AUTO_INCREMENT = 1;