-- Schema for dhcp-snopping parsing example.

create table switches (
    hostname    text not null primary key,
    location    text
);

create table dhcp (
    mac          text primary key,
    ip           text,
    vlan         text,
    interface    text,
    switch       text,
    FOREIGN KEY (switch) REFERENCES switches (hostname) 
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
