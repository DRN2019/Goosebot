CREATE DATABASE IF NOT EXISTS goosebot;

CREATE TABLE servers IF NOT EXISTS(
    id INT AUTO_INCREMENT PRIMARY KEY,
    guild_id INT NOT NULL,
    guild_name varchar(33) NOT NULL,
);

CREATE TABLE IF NOT EXISTS text_permissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message_honk BOOLEAN NOT NULL DEFAULT 0,
    reaction BOOLEAN NOT NULL DEFAULT 0,
    memes BOOLEAN NOT NULL DEFAULT 0,
    delete_msg BOOLEAN NOT NULL DEFAULT 0,
    message_goose BOOLEAN NOT NULL DEFAULT 0,
    no_peace BOOLEAN NOT NULL DEFAULT 0,
    server_id INT NOT NULL,
    FOREIGN KEY (server_id) REFERENCES servers(id)
);

CREATE TABLE IF NOT EXISTS voice_permissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    disconnect BOOLEAN NOT NULL DEFAULT 0,
    voice_honk BOOLEAN NOT NULL DEFAULT 0,
    server_id INT,
    FOREIGN KEY (server_id) REFERENCES servers(id)
)
