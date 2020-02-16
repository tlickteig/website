/*
 * AUTHOR: Timothy Lickteig
 * DATE: 2019-12-16
 *  Main JS file for the website
 */

$(document).ready(function() {
        
    startjQueryUI();
    renderCharts();
    switchTabs();
    setInterval(runClock, 1);
    setInterval(runWorldClock, 1000);
});

function startjQueryUI() {
    
    $("#tabbedPanels").tabs();
        
    $("input[type='button'], input[type='submit']").each(function() {
        ($(this)).button();
    });
    
    $("#btnGithub").click(function() {
        window.location.href = "http://www.github.com/tlickteig";        
    });
    
    $("img").click(function() {
        $("#imgCurrentMeme").attr("src", $(this).attr("src"));        
        $("#dvViewMeme").dialog("open");
    });
    
    $("#dvUsefulChartContainer").accordion({
        active: false,
        collapsible: true
    });
    
    $("#dvAddPost").dialog({
        autoOpen: false,
        modal: true,
        title: "Add Post"
    });
    
    $("#btnAddPost").click(function() {
        $("#dvAddPost").dialog("open");
    });
}

function renderCharts() {
    
    var europeElectricity = new CanvasJS.Chart("dvEuropeElectricity", {
        
        title: {
            text: "Electricity Consumption in Europe, 1500s"
        },
        data: [{
            type: "column",
            dataPoints: [
                {label: "1500", y: 0},
                {label: "1510", y: 0},
                {label: "1520", y: 0},
                {label: "1530", y: 0},
                {label: "1540", y: 0},
                {label: "1550", y: 0},
                {label: "1560", y: 0},
                {label: "1570", y: 0},
                {label: "1580", y: 0},
                {label: "1590", y: 0}
            ]
        }],
        axisX: {
            title: "Year"
        },
        axisY: {
            title: "Kilowatts"
        },
        width: 800
    });
    europeElectricity.render();
    
    var titanicHumidity = new CanvasJS.Chart("dvTitanicHumidity", {
        
        title: {
            text: "Average Relative Humidity Aboard the Titanic, 1900s"
        },
        data: [{
            type: "column",
            dataPoints: [                
                {label: "1900", y: 5},
                {label: "1910", y: 10},
                {label: "1920", y: 100},
                {label: "1930", y: 100},
                {label: "1940", y: 100},
                {label: "1950", y: 100},
                {label: "1960", y: 100},
                {label: "1970", y: 100},
                {label: "1980", y: 100},
                {label: "1990", y: 100}
            ]
        }],
        axisX: {
            title: "Year"
        },
        axisY: {
            title: "Relative Humidity(%)",
            maximum: 110
        },
        width: 800
    });
    titanicHumidity.render();
    
    var towTrucks = new CanvasJS.Chart("dvTowTrucks", {
        
        title: {
            text: "Number of Homemade Tow Trucks in my Friend's Yard"
        },
        data: [{
            type: "column",
            dataPoints: [                
                {label: "2017", y: 0},
                {label: "2018", y: 0},
                {label: "2019", y: 1},
                {label: "2020", y: 1}
            ]
        }],
        axisX: {
            title: "Year"
        },
        axisY: {
            title: "Number of Tow Trucks",
            maximum: 2,
            interval: 1
        },        
        width: 800
    });
    towTrucks.render();
 
    var personalCalculators = new CanvasJS.Chart("dvPersonalCalculators", {
        
        title: {
            text: "Number of Personal Calculators I own, Yearly"
        },
        data: [{
            type: "column",
            dataPoints: [
                {label: "2017", y: 1},
                {label: "2018", y: 1},
                {label: "2019", y: 3},
                {label: "2020", y: 5}
            ]
        }],
         axisX: {
            title: "Year"
        },
        axisY: {
          title: "Number of Calculators"  
        },
        width: 800
    });
    personalCalculators.render();
    
    var iowaWeather = new CanvasJS.Chart("dvIowaWeather", {
        
        title: {
          text: "How the Weather Feels in Iowa"  
        },
        data: [{
            type: "pie",
            startAngle: 338,
            yValueFormatString: "##0\"%\"",
            indexLabel: "{label} {y}",
            dataPoints: [
                {label: "Too Hot", y: 49, color: "crimson"},
                {label: "Too Cold", y: 49, color: "cornflowerblue"},
                {label: "Just Right", y: 2, color: "darkorange"}
            ]
        }],
        width: 800
    });
    iowaWeather.render();
}

function runClock() {
    
    var element = document.getElementById("clockNumber");
    var seconds = (new Date().getTime() / 1000);
    element.innerHTML = seconds;
}

function runWorldClock() {
    
    //Declare variables
    var now = new Date(new Date().getTime());
    var utc = new Date(new Date().getTime() + (now.getTimezoneOffset() * 60000));
    var cities = [
        {id: "cvWorldClockLocal", offset: 0},
        {id: "cvWorldClockUTC", offset: (now.getTimezoneOffset() / 60)},
        {id: "cvWorldClockBerlin", offset: (now.getTimezoneOffset() / 60) + 1},
        {id: "cvWorldClockCapeTown", offset: (now.getTimezoneOffset() / 60) + 2},
        {id: "cvWorldClockMoscow", offset: (now.getTimezoneOffset() / 60) + 3},
        {id: "cvWorldClockDubai", offset: (now.getTimezoneOffset() / 60) + 4},
        {id: "cvWorldClockBangkok", offset: (now.getTimezoneOffset() / 60) + 7},
        {id: "cvWorldClockShanghai", offset: (now.getTimezoneOffset() / 60) + 8},
        {id: "cvWorldClockTokyo", offset: (now.getTimezoneOffset() / 60) + 9},
        {id: "cvWorldClockSydney", offset: (now.getTimezoneOffset() / 60) + 11},
        {id: "cvWorldClockHonolulu", offset: (now.getTimezoneOffset() / 60) - 10},
        {id: "cvWorldClockDenver", offset: (now.getTimezoneOffset() / 60) - 7},
        {id: "cvWorldClockAnchorage", offset: (now.getTimezoneOffset() / 60) - 9},
        {id: "cvWorldClockLosAngeles", offset: (now.getTimezoneOffset() / 60) - 8},
        {id: "cvWorldClockChicago", offset: (now.getTimezoneOffset() / 60) - 6},
        {id: "cvWorldClockNewYorkCity", offset: (now.getTimezoneOffset() / 60) - 5},
        {id: "cvWorldClockHalifax", offset: (now.getTimezoneOffset() / 60) - 4},
        {id: "cvWorldClockRioDeJaneiro", offset: (now.getTimezoneOffset() / 60) - 3}
    ];
    
    
    for(var i = 0; i < cities.length; i++) {
                
        //Declare variables and reset canvas
        var city = cities[i];
        var clock = document.getElementById(city.id);
        var ctx = clock.getContext("2d");
        var radius = clock.height / 2;
        clock.width = clock.width;
        
        //Draw body
        ctx.translate(radius, radius);
        radius = radius * .90;
        ctx.arc(clock.width / 2 - (radius / .9), 0, radius, 0, 2 * Math.PI);
        ctx.fillStyle = "black";
        ctx.lineWidth = 5;
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(0, 0, radius * 0.05, 0, 2 * Math.PI);
        ctx.fill();
        
        //Draw numbers
        ctx.font = radius * 0.15 + "px cursive";
        ctx.textBaseline = "middle";
        ctx.textAlign = "center";
        for(var num = 1; num < 13; num++){
            var ang = num * Math.PI / 6;
            ctx.rotate(ang);
            ctx.translate(0, -radius * 0.85);
            ctx.rotate(-ang);
            ctx.fillText(num.toString(), 0, 0);
            ctx.rotate(ang);
            ctx.translate(0, radius * 0.85);
            ctx.rotate(-ang);
        }
        
        //Get the time
        var time = new Date(new Date().getTime());
        var time = new Date(new Date().getTime() + 
                (utc.getTimezoneOffset() + (city.offset * 60) * 60000));
        var hour = time.getHours();
        var minute = time.getMinutes();
        var second = time.getSeconds();
        var pm = hour >= 12;
                       
        //Map the numbers to the face of the clock.
        hour = hour % 12;
        hour = (hour * Math.PI / 6) + (minute * Math.PI / (6 * 60));
        minute = (minute * Math.PI / 30);
        
        //Draw the hour hand
        ctx.beginPath();
        ctx.lineWidth = 3;
        ctx.moveTo(0, 0);
        ctx.rotate(hour);
        ctx.lineTo(0, -120);
        ctx.stroke();
        ctx.rotate(-hour);
        
        //Draw the minute hand
        ctx.beginPath();
        ctx.lineWidth = 3;
        ctx.moveTo(0, 0);
        ctx.rotate(minute);
        ctx.lineTo(0, -160);
        ctx.stroke();
        ctx.rotate(-minute);
        
        //Draw the AM/PM marker
        ctx.font = 50 + "px arial";
        ctx.textBaseline = "middle";
        ctx.textAlign = "center";
        ctx.translate(0, 75, 0);
        ctx.fillText(pm ? "PM" : "AM", 0, 0);
    }
}

function switchTabs() {
        
    if($("#dvWeatherWindow").html().length > 65) {
        $("#tabbedPanels").tabs("option", "active", 5);
		$("#dvWeatherWindow").slideDown();
    } 
}