DROP DATABASE IF EXISTS chat;

CREATE DATABASE chat;

USE chat;

-- Create table for storing messages
CREATE TABLE message (
	ChatID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    PostDate DATE NOT NULL,
    PostTime TIME NOT NULL,
    UserName NVARCHAR(50) NOT NULL,
    Message NVARCHAR(500) NOT NULL,
    IsOwner BOOLEAN NOT NULL DEFAULT FALSE
);

DELIMITER //

-- Create a procedure for inserting new chats
CREATE PROCEDURE sp_insert_chat(
	p_name NVARCHAR(50),
    p_message NVARCHAR(500)
)
BEGIN
	INSERT INTO message
    (PostDate, PostTime, UserName, Message, IsOwner)
    VALUES
    (CURRENT_DATE, CURRENT_TIME, p_name, p_message, FALSE);
END//

-- Create a procedure for the owner to insert messages
CREATE PROCEDURE sp_insert_chat_as_owner(
    p_message NVARCHAR(500)
)
BEGIN
	INSERT INTO message
    (PostDate, PostTime, UserName, Message, IsOwner)
    VALUES
    (CURRENT_DATE, CURRENT_TIME, 'MinivanMaster', p_message, TRUE);
END//

-- Procedure for viewing all chats
CREATE PROCEDURE sp_select_all_chats(
	p_limit INT
)
BEGIN
	SELECT
		UserName, Message, PostDate, PostTime, IsOwner
    FROM message
    ORDER BY ChatID DESC
    LIMIT p_limit;
END//

-- Procedure for the owner to view all chats
CREATE PROCEDURE sp_select_all_chats_as_owner()
BEGIN
	SELECT
		UserName, Message, PostDate, PostTime, IsOwner, ChatID
    FROM message;
END//

-- Procedure for deleting chats
CREATE PROCEDURE sp_delete_chat(
	p_chatID INT
)
BEGIN
	DELETE FROM message
    WHERE ChatID = p_chatID;
END//

DELIMITER ;

GRANT EXECUTE ON PROCEDURE sp_insert_chat TO 'web'@'%';
GRANT EXECUTE ON PROCEDURE sp_select_all_chats TO 'web'@'%';