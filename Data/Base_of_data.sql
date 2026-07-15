create database smart_finance_manager;

use smart_finance_manager;

create table users (
    userId int auto_increment primary key,
    username varchar(12) not null unique,
    firstName varchar(10) not null,
    lastName varchar(10) not null,
    email varchar(50) not null unique,
    passwordHash varchar(20) not null,
    createdAt date not null
);

create table incomes (
    incomeId int auto_increment primary key,
    amount decimal(10,2) not null,
    category varchar(20),
    description varchar(70),
    date date not null,
    userId int not null,
    foreign key (userId) references users(userId)
);

create table expenses (
    expenseId int auto_increment primary key,
    amount decimal(10,2) not null,
    category varchar(50),
    description varchar(70),
    date date not null,
    userId int not null,
    foreign key (userId) references users(userId)
);

create table financial_goals (
    goalId int auto_increment primary key,
    title varchar(15) not null,
    targetAmount decimal(10,2) not null,
    currentAmount decimal(10,2) not null default 0,
    deadline date,
    status varchar(30),
    userId int not null,
    foreign key (userId) references users(userId)
);