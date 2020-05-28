var imageRadius = 250;
var numberOfPoints = 10;
var baseImage = "<svg height='500' width='500'>\n\
<line x1='250' y1='0' x2='250' y2='500' style='stroke:rgb(0,0,0);stroke-width:2' />\n\
<line x1='0' y1='250' x2='500' y2='250' style='stroke:rgb(0,0,0);stroke-width:2' />\n\
";

$(document).ready(function() {
    
    plotAxis();    
    $("#dvPlotterOutput").html(baseImage + "</svg>");     
    
    $("#btnPlot").click(function() {
       
        var image = "";
        var inputText = $("#txtPlotterInput").val().split(" ").join("");        
        
        try {
            if($("#txtPlotterInput").val() === "") {
                throw "";
            }
            if(true) {
                if(inputText.indexOf("²") > -1) {
                    image = plotQuadraticFunction(inputText);
                } else {
                    image = plotLinearFunction(inputText);
                }
            }        
            $("#dvPlotterOutput").html(image + plotScale() + "</svg>");
            $("#pPlotterError").html("");
        } catch(err) {
            $("#pPlotterError").html("Input text is incorrectly formed");
        }    
    });
});

function plotAxis() {
            
    for(var i = 0; i <= imageRadius * 2; i += imageRadius / numberOfPoints) {
        baseImage += "<circle cx='" + i + "' cy='" + 
        imageRadius + "' r='3' stroke='black' fill='black' />";
    }
    
    for(var i = 0; i <= imageRadius * 2; i += imageRadius / numberOfPoints) {
        baseImage += "<circle cx='" + imageRadius + 
        "' cy='" + i + "' r='3' stroke='black' fill='black' />";
    }    
    
    for(var i = 0; i <= imageRadius * 2; i += imageRadius / numberOfPoints) {
        baseImage += "<line x1='" + i + "' y1='0' x2='" + i + "' y2='" + 
        (imageRadius * 2) + "' style='stroke:rgb(50,50,50);stroke-width:.5' />";
    }
    
    for(var i = 0; i <= imageRadius * 2; i += imageRadius / numberOfPoints) {
        baseImage += "<line x1='0' y1='" + i + "' x2='" + (imageRadius * 2) + 
        "' y2='" + i + "' style='stroke:rgb(50,50,50);stroke-width:.5' />";
    }
}

function plotScale() {
    
    var Xmin = $("#numPlotterZoom").val() * -1;
    var Xmax = $("#numPlotterZoom").val();
    var output = "<text x='" 
        + ((imageRadius * 2) - (imageRadius / numberOfPoints) - 
        (imageRadius / numberOfPoints / 3)) + "' y='" + (imageRadius - 
        (imageRadius / numberOfPoints / 2)) + 
        "' fill='black'>" + (Xmax - (Xmax / 10)) + "</text>";
    output += "<text x='" 
        + ((imageRadius / numberOfPoints) - (imageRadius / numberOfPoints / 3)) 
        + "' y='" + (imageRadius - (imageRadius / numberOfPoints / 2)) 
        + "' fill='black'>" + (Xmin + (Xmax / 10)) +"</text>";
    output += "<text x='" 
        + (imageRadius + (imageRadius / numberOfPoints / 3)) + "' y='"
        + ((imageRadius / numberOfPoints) + (imageRadius / numberOfPoints / 3)) 
        + "' fill='black'>" + (Xmax - (Xmax / 10)) + "</text>";
    output += "<text x='" 
        + (imageRadius + (imageRadius / numberOfPoints / 3))  
        + "' y='" + ((imageRadius * 2) - (imageRadius / numberOfPoints)) 
        + "' fill='black'>" + (Xmin + (Xmax / 10)) +"</text>";
    return output;
}

function plotLinearFunction(inputText) {
    
    var negative = false;
    if(inputText.indexOf("-") === 0) {
        inputText = inputText.substring(1, inputText.length);
        negative = true;
    }
    
    var m = inputText.substr(0, inputText.indexOf("x"));
    var b = inputText.substr(inputText.indexOf("+") + 1, inputText.length - 1);    
    var Xmin = $("#numPlotterZoom").val();
    var Xmax = $("#numPlotterZoom").val() * -1;
    
    if(inputText.indexOf("-") > -1) {
        b = inputText.substr(inputText.indexOf("-") + 1, inputText.length - 1) * -1;
    }
    
    if(inputText === "x") {
        b = 0;
        m = 1;
    } else if(inputText.indexOf("x") === 0) {
        m = 1;
    } else if(inputText.indexOf("+") === -1 && inputText.indexOf("-") === -1) {
        b = 0;
    }
        
    if(!negative) {
        m = m * -1;
    }        
    
    var x2 = imageRadius * 2;    
    var y1 = imageRadius - ((m * Xmin) * (imageRadius / numberOfPoints)) + 
        ((-b / Xmin * 10) * imageRadius / numberOfPoints);
    var y2 = imageRadius - ((m * Xmax) * (imageRadius / numberOfPoints)) + 
        ((-b / Xmin * 10) * imageRadius / numberOfPoints);
    
    if(isNaN(y1) || isNaN(y2)) {
        throw "";
    }
    
    var image = "";
    if(baseImage.indexOf("</svg>") > -1) {
        image = baseImage.substr(0, baseImage.length - 6);
    } else {
        image = baseImage;
    }
    image += "<line x1='0' y1='" + y1 + "' x2='" + x2 + "' y2='" + y2 + 
        "' style='stroke:rgb(0,0,255);stroke-width:2' />";
    return image;
}

function plotQuadraticFunction(inputText) {
    
    var zoom = $("#numPlotterZoom").val();
    var lastNegative = false;
    if(inputText.lastIndexOf("-") > inputText.lastIndexOf("x")) {
        lastNegative = true;
    }
    
    var negative = false;
    if(inputText.indexOf("-") === 0) {
        negative = true;
        inputText = inputText = inputText.substring(1, inputText.length);
    }  
    if(inputText.indexOf("x") === 0) {
        inputText = "1" + inputText;
    }
    var a = inputText.substring(0, inputText.indexOf("x")) * 1;
    inputText = inputText.substring(inputText.indexOf("x") + 2, inputText.length);
    if(negative) {
        a = a * -1;
    }     
    negative = false;
    
    var b = 0;    
    if(inputText.indexOf("-") === 0) {
        negative = true;
    }
    inputText = inputText.substring(1, inputText.length);    
    if(inputText.indexOf("x") > -1) {
        if(inputText.indexOf("x") === 0) {
            inputText = "1" + inputText;
        }
        b = inputText.substring(0, inputText.indexOf("x")) * 1;
    }    
    if(negative) {
        b = b * -1;
    }
    negative = false;
    
    if(inputText.length > 1) {
        inputText = inputText.substring(inputText.indexOf("x") + 2, inputText.length);
    }
    var c = 0;
    if(inputText * 1 !== "NaN") {
        c = inputText * 1;
    }
    if(lastNegative) {
        c = c * -1;
    }       
    
    if(isNaN(a) || isNaN(b) || isNaN(c)) {
        throw "";
    }
    
    var vx = (-b / (2 * a));
    var vy = (a * (vx * vx)) + (b * vx) + c;
    var Xmax = zoom;
    var Xmin = zoom * -1;
    var Y = (a * (Xmax * Xmax)) + (b * Xmax) + c;    
        
    vy = vy + (-1 * Y / 2);
    vx = (vx * (imageRadius / zoom)) + imageRadius;
    vy = imageRadius - (vy * (imageRadius / zoom * 2));
    Xmax = (Xmax * (imageRadius / zoom)) + imageRadius;
    Xmin = imageRadius - (-1 * Xmin * (imageRadius / zoom));
    Y = imageRadius - (Y * (imageRadius / zoom));    
    
    var image = baseImage + 
        "<path d='M" + Xmin + "," + Y + " Q" + vx + "," + vy + " " + Xmax + 
        "," + Y + "' stroke='blue' stroke-width='2' fill='none' />";
    return image;
}