<?php

    //Get form inputs
    $name = isset($_GET["name"]) ? $_GET["name"] : "|";
    $content = isset($_GET["content"]) ? $_GET["content"] : "|";
    
    if(sanitizeInputs($name, $content)) {
        
        //Declare variables
        $db = mysqli_connect('localhost', '*', '*', 'bulletinBoard');
        $query = "CALL bulletinBoard.sp_insert_post(?, ?);";
        $stmt = $db->prepare($query);
        $stmt->bind_param('ss', $name, $content);
        $stmt->execute();
        
        //Try to connect to the database
        if(mysqli_connect_errno()) {
            printResult("Database Error");
        }
        else {
            
            //Try to add the record
            if($stmt->affected_rows > 0) {
                printResult("Post added");
            } else {
                printResult("Database Error: $db->error");
            }
        }
    } else {        
        printResult("Invalid input");
    }
    
    function sanitizeInputs($name, $content) {
        $result = true;
        
        //Test for specific invalid characters
        if($name == "" || $content == "") {
            $result = false;
        }
        return $result;
    }
    
    function printResult($text) {
        echo "<h1>$text</h1>";
        echo "<a href='../index.php'>Back to Website</a>";
    }
?>
