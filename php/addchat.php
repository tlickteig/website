<?php 
    
    $outputString = "hello";

    if(isset($_GET["name"]) && isset($_GET["message"]) 
            && ($_GET["name"] != "") && ($_GET["message"] != "")) {
        
        //Get name and the message body
        $name = $_GET["name"];
        $message = $_GET["message"];
        $outputString = "null";
        
        //Prevent cross site scripting
        $name = str_replace("<", "&#60", $name);
        $message = str_replace("<", "&#60", $message);
        
        //Intialize database connection and execute the query
        $db = mysqli_connect('localhost', 'web', '*****', 'chat');
        $query = "CALL chat.sp_insert_chat(?, ?);";
        $stmt = $db->prepare($query);
        $stmt->bind_param('ss', $name, $message);
        $stmt->execute();
        
        //Try to read the results and print results
        if(mysqli_connect_errno()) {
            $outputString = "error";
        } else {
            $outputString = "success";
        }        
    }
    
    echo $outputString;
?>