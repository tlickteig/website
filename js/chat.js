$(document).ready(function () {

    $("#btnSendMessage").click(function () {
        if($("#txtChatName").val() === "") {
            $("#pChatError").text("Please enter your name");
        } else if($("#txtChatMessage").val() === "") {
            $("#pChatError").text("Please enter your message");
        }else {            
            sendChat();
            $("#txtChatMessage").val("");
        }
    });
    
    getChat();
    scrollToBottom();    
    setInterval(getChat, 500);   
    
    setInterval(function() {
        if($("#chkAutoScroll").is(":checked")) {
            scrollToBottom();
        }
    }, 20);
});

function getChat() {

    if ($("#dvChat").is(":visible")) {
        const xhr = new XMLHttpRequest();
        xhr.open('get', './php/getchat.php');

        xhr.onload = () => {
            printChat(JSON.parse(xhr.response));            
        };

        xhr.send();
    }
}

function sendChat() {

    const xhr = new XMLHttpRequest();
    xhr.open('get', './php/addchat.php?name=' +
            $("#txtChatName").val() +
            "&" + "message=" + $("#txtChatMessage").val());

    xhr.onload = () => {
        $("#pChatError").text("");  
        scrollToBottom();
    };

    xhr.send();
}

function printChat(json) {
    
    var messages = json.messages;
    var text = "";
    for(var i = 0; i < messages.length; i++) {
        
        var message = messages[i];
        
        text += "\n";        
        if(message.isOwner === "true") {
            text += "[OWNER]";
        }
        text += "[" + message.date + " " + message.time + "]";
        text += "\n" + message.name + ": " + message.message;
        text += "\n";
    }
    
    $("#txtaChatWindow").val(text);
}

function scrollToBottom() {
    
    var chatWindow = $("#txtaChatWindow");
    chatWindow.scrollTop(chatWindow[0].scrollHeight);
}