<?php

    //Declare variables
    $outputString = "";
    $limit = 35;

    //Class for representing message objects
    class Message {

        //Private class attributes
        private $name;
        private $message;
        private $date;
        private $time;
        private $isOwner;

        //Constructor
        function __construct($name, $message, $date, $time, $isOwner) {

            $this->name = $name;
            $this->message = $message;
            $this->date = $date;
            $this->time = $time;
            $this->isOwner = $isOwner;
        }

        //Get a json representation of the object
        function getJson() {
            $outputString = "{";
            $outputString .= '"name":' . '"' . $this->name . '",';
            $outputString .= '"message":' . '"' . $this->message . '",';
            $outputString .= '"date":' . '"' . $this->date . '",';
            $outputString .= '"time":' . '"' . $this->time . '",';
            if ($this->isOwner) {
                $outputString .= '"isOwner": "true"';
            } else {
                $outputString .= '"isOwner": "false"';
            }
            return $outputString . "}";
        }

    }

    //Declare variables
    $db = mysqli_connect('localhost', 'web', '*****', 'chat');
    $query = "CALL chat.sp_select_all_chats(?);";
    $stmt = $db->prepare($query);
    $stmt->bind_param('i', $limit);
    $stmt->execute();

    //Try to connect to db
    if (mysqli_connect_errno()) {
        $outputString = "Connection error";
    } else {

        //Return the results and make an array of messages
        $result = $stmt->get_result();
        $messages = array();

        //Test to see if there are any rows
        if ($result->num_rows > 0) {

            //Loop through the results and append to the array
            while ($row = $result->fetch_assoc()) {
                $message = new Message($row["UserName"], $row["Message"],
                        $row["PostDate"], $row["PostTime"], $row["IsOwner"]);
                array_unshift($messages, $message);
            }

            //Format the output string as a json object
            $outputString = '{"messages": [';
            foreach ($messages as $message) {
                $outputString .= $message->getJson() . ",";
            }
            $outputString = substr($outputString, 0, -1);
            $outputString .= "]}";
        } else {
            $outputString = "Nothing to display";
        }

        //Close the connection
        $db->close();
    }

    echo "{$outputString}";
?>