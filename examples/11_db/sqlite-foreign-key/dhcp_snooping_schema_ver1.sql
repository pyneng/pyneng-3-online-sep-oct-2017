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
    switch       text not null,
    FOREIGN KEY (switch) references switches(hostname)
);
