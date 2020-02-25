DROP DATABASE IF EXISTS bulletinBoard;

CREATE DATABASE bulletinBoard;

USE bulletinBoard;

DROP USER IF EXISTS 'web'@'%';

CREATE USER 'web'@'%' IDENTIFIED WITH mysql_native_password BY 'webaccess';

-- Create table for storing posts
CREATE TABLE postRecord (
	PostID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    PostDate DATE NOT NULL,
    UserName NVARCHAR(100) NOT NULL,
    Content NVARCHAR(4000) NOT NULL,
    IsOwner BOOLEAN NOT NULL
);

-- Create table for the view counter
CREATE TABLE viewCounter (
	ViewNumber INT NOT NULL PRIMARY KEY
);
INSERT INTO viewCounter
VALUES (1);

DELIMITER //

-- Create procedure for getting the number of website views
CREATE PROCEDURE sp_get_views()
BEGIN
	
    -- Declare variables
    DECLARE views INT;
    SET views = 0;
    
    -- Get the number of views
    SELECT MAX(ViewNumber)
    INTO views
    FROM viewCounter;
    
    -- Increment the value
    SET views = views + 1;
    
    -- Update the table
    UPDATE viewCounter
    SET ViewNumber = views  
    WHERE ViewNumber > 0;
    
    -- Return the views
    SELECT views;
END//

-- Procedure for the root user to edit the number of views
CREATE PROCEDURE sp_update_views(
	p_views INT
)
BEGIN
	
    UPDATE viewCounter
    SET ViewNumber = p_views
    WHERE ViewNumber > 0;
END//

-- Create procedure for inserting posts
CREATE PROCEDURE sp_insert_post(
	p_name NVARCHAR(100),
    p_content NVARCHAR(4000)
)
BEGIN 
	INSERT INTO postRecord
    (PostDate, UserName, Content, IsOwner)
    VALUES
    (CURRENT_DATE, p_name, p_content, FALSE);
END//

-- Create procedure for viewing all posts
CREATE PROCEDURE sp_select_all_posts()
BEGIN
	SELECT
		UserName, Content, PostDate, IsOwner
    FROM postRecord;
END//

-- Create procedure for viewing all posts as root
CREATE PROCEDURE sp_select_all_posts_as_root()
BEGIN
	SELECT *
    FROM postRecord;
END//

-- Create procedure for the website owner to add new posts
CREATE PROCEDURE sp_insert_post_as_owner(
	p_content NVARCHAR(4000)
)
BEGIN
	INSERT INTO postRecord
    (PostDate, UserName, Content, IsOwner)
    VALUES
    (CURRENT_DATE(), "The Minivan Master", p_content, TRUE);
END//

-- Create procedure for removing a post
CREATE PROCEDURE sp_delete_post(
	p_post_id INT
)
BEGIN
	DELETE FROM postRecord
    WHERE PostID = p_post_id;
END//

DELIMITER ;

GRANT EXECUTE ON PROCEDURE sp_insert_post TO 'web'@'%';
GRANT EXECUTE ON PROCEDURE sp_select_all_posts TO 'web'@'%';
GRANT EXECUTE ON PROCEDURE sp_get_views TO 'web'@'%';

/*
CALL sp_insert_post("Timothy Lickteig", "This is the first post");
CALL sp_insert_post("Timothy Lickteig", "This is the second post");
CALL sp_insert_post("Timothy Lickteig", "This is the third post");
CALL sp_insert_post("Timothy Lickteig", "This is the fourth post");
CALL sp_insert_post("Timothy Lickteig", "This is the fifth post");
*/

INSERT INTO postRecord
(PostDate, UserName, Content, IsOwner)
VALUES
("2020-02-15", "The Minivan Master", "This is a post", 1),
("2020-02-15", "Tony Farrington", "NSFW", 0),
("2020-02-15", "UwU", "OwO", 0),
("2020-02-15", "A Guy", "BMW's > Toyota's", 0),
("2020-02-16", "Cody Freeberg", "Cody was here.", 0),
("2020-02-18", "Tim Lickteig", "Tony sucks", 0),
("2020-02-18", "Bob Trapp", "More essay's", 0),
("2020-02-18", "Thicc dip sticc", "suh", 0),
("2020-02-18", "Toothpaste man", "Motives are still unknown", 0),
("2020-02-18", "Jerry Glasgow", "42.146775, -91.744898", 0),
("2020-02-18", "L33t hacker", '&#60script>console.log("Hello World!");&#60/script>', 0),
("2020-02-19", "Gooder", "Hi Tim!", 0),
("2020-02-19", "Tony Farrington", "@Tim Lickteig (Not the real one, the one below), clearly has no sense of humor!", 0),
("2020-02-19", "Anonymous Yanker", "Hey Tim, Put some more fun stuff on this page would you. I really get bored while cruising the net and I just feel like if we had some more great, compelling content like the items found on this site, well the world would be a better place. Please make more... I'll be watching p.s. I would like to see a picture of this homemade truck.", 0),
("2020-02-20", "Schwarzbraun is die hasulnuts", "YA YA YA DA DA", 0),
("2020-02-20", "Test for html break", '&#60h1>Test&#60/h1>', 0),
("2020-02-20", "Last test", '&#60/textarea>&#60input type="submit" value="Submit" id="btnSubmitPost" class="ui-button ui-corner-all ui-widget" role="button">&#60/form>&#60p>Did this break?&#60/p>', 0),
("2020-02-21", "Gooder", "Has big pp", 0)
;