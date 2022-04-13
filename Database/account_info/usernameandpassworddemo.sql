create table usernameandpassworddemo
(
    U_Id         int unsigned auto_increment
        primary key,
    UserId       varchar(255) null,
    UserPassword varchar(255) null,
    constraint UserId
        unique (UserId)
);

