<!DOCTYPE html>
<html>
    <head>
        <title>The Home of the Minivan Master</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="css/jquery-ui.min.css" rel="stylesheet" type="text/css"/>
        <link href="https://fonts.googleapis.com/css?family=Patua+One&display=swap" rel="stylesheet">        
        <link href="css/standard.css" rel="stylesheet" type="text/css"/>
        <script src="https://code.jquery.com/jquery-3.4.1.js"></script>
        <script src="js/jquery-ui.min.js" type="text/javascript"></script>
        <script src="js/canvasjs.min.js" type="text/javascript"></script>
        <script src="js/standard.js" type="text/javascript"></script>
        <script src="js/meter.js" type="text/javascript"></script>
        <script src="js/calculator.js" type="text/javascript"></script>
    </head>    
    <body  onload="start()"> 
        <header>
            <h1>Welcome to the Minivan Master's Lair!</h1>
        </header>
        <main>
            <input type="button" id="btnGithub" value="Check out my GitHub!" />
            <div id="tabbedPanels">
                <ul>
                    <li><a href="#dvAbout">About</a></li>
                    <li><a href="#dvUsefulCharts">Useful Charts</a></li>
                    <li><a href="#dvJsThing">Cool JavaScript Thing</a></li>
                    <li><a href="#dvUnixClock">Unix Time Now</a></li>
                    <li><a href="#dvWorldClock">World Clock</a></li>
                    <li><a href="#dvWeather">Weather</a></li>
                    <li><a href="#dvBulletinBoard">Bulletin Board</a></li>
                    <li><a href="#dvCalculator">Calculator</a></li>
                </ul>
                <div id="dvAbout">
                    <h2>Welcome!</h2>
                    <h3>About Me</h3>
                    <p>I am an unidentified human being located on planet 
                        Earth. I live at an unnamed address, work at a nonspecific 
                        business, and go to a certain school. My coordinates 
                        are 41.9779° N, 91.6656° W. That might seem rather 
                        vague, but that's your problem not mine.</p>
                    <br />
                    <h3>Why did I make this website?</h3>
                    <p>It just seemed like a good winter break project lol</p>
                    <br />
                    <h3>View Counter</h3>
                    <?php
                    //Declare variables
                    $db = mysqli_connect('localhost', 'web', 'webaccess', 'bulletinBoard');
                    $query = "CALL bulletinBoard.sp_get_views();";

                    //Test for any connection errors
                    if (mysqli_connect_errno()) {
                        echo "Connection failure";
                    } else {

                        //Query the results
                        $result = $db->query($query);

                        //Test to see if there are any results
                        if ($result->num_rows > 0) {

                            //Access the results and append to the page
                            $outputString = "";
                            while ($row = $result->fetch_assoc()) {
                                $views = $row['views'];
                                $outputString = "<p id='viewCounter'>";
                                $outputString .= $views;
                                $outputString .= "</p>";
                            }
                            echo $outputString;
                        }
                    }
                    ?>
                </div>
                <div id="dvUsefulCharts">
                    <div id="dvUsefulChartContainer">
                        <h3>Electricity Consumption in Europe</h3>
                        <div id="dvAccordionEurope">
                            <div id="dvEuropeElectricity"></div>
                        </div>
                        <h3>Average Relative Humidity Aboard the Titanic</h3>
                        <div id="dvAccordionTitanic">
                            <div id="dvTitanicHumidity"></div>
                        </div>
                        <h3>Homemade Tow Trucks in my Friend's Yard</h3>
                        <div id="dvAccordionTowTrucks">
                            <div id="dvTowTrucks"></div>
                        </div>
                        <h3>Total Number of Calculators I Own</h3>
                        <div id="dvAccordionPersonalCalculators">
                            <div id="dvPersonalCalculators"></div>
                        </div>
                        <h3>Number of Programming Languages I Know</h3>
                        <div id="dvAccordionNumberOfProgrammingLanguages">
                            <div id="dvNumberOfProgrammingLanguages"></div>
                        </div>
                        <h3>Sixty Watt Light Bulbs</h3>
                        <div id="dvAccordionSixtyWattLightBulbs">
                            <div id="dvSixtyWattLightBulbs"></div>
                        </div>
                        <h3>How the Weather Feels in Iowa</h3>
                        <div id="dvAccordionIowaWeather">
                            <div id="dvIowaWeather"></div>
                        </div>
                    </div>
                </div>
                <div id="dvJsThing">
                    <canvas id="cvsMainCanvas" width="500" height="500"></canvas>
                    <br />
                    <input type="button" id="btnUp" value="  +  " onclick="clickUp()"/>
                    <input type="button" id="btnDown" value="  -  " onclick="clickDown()"/>                                    
                </div>  
                <div id="dvUnixClock">
                    <p id="clockNumber">000</p>
                </div>
                <div id="dvWorldClock">
                    <table>
                        <tr>
                            <td>
                                <canvas class="worldClock" 
                                        id="cvWorldClockLocal"
                                        width="400" height="400"></canvas>
                                <p>Local</p></td>
                            <td>
                                <canvas class="worldClock" 
                                        id="cvWorldClockUTC"
                                        width="400" height="400"></canvas>
                                <p>UTC</p></td>
                            <td>
                                <canvas class="worldClock" 
                                        id="cvWorldClockBerlin"
                                        width="400" height="400"></canvas>
                                <p>Berlin</p></td>
                            <td>
                                <canvas class="worldClock" 
                                        id="cvWorldClockCapeTown"
                                        width="400" height="400"></canvas>
                                <p>Cape Town</p></td>
                        </tr>                    
                        <tr>
                            <td>
                                <canvas class="worldClock" 
                                        id="cvWorldClockMoscow"
                                        width="400" height="400"></canvas>
                                <p>Moscow</p></td>
                            <td>
                                <canvas class="worldClock" 
                                        id="cvWorldClockDubai"
                                        width="400" height="400"></canvas>
                                <p>Dubai</p></td>
                            <td>
                                <canvas class="worldClock" 
                                        id="cvWorldClockBangkok"
                                        width="400" height="400"></canvas>
                                <p>Bangkok</p></td>
                            <td>
                                <canvas class="worldClock" 
                                        id="cvWorldClockShanghai"
                                        width="400" height="400"></canvas>
                                <p>Shanghai</p></td>
                        </tr>
                        <tr>
                            <td>
                                <canvas class="worldClock" 
                                        id="cvWorldClockTokyo"
                                        width="400" height="400"></canvas>
                                <p>Tokyo</p></td>
                            <td>
                                <canvas class="worldClock" 
                                        id="cvWorldClockSydney"
                                        width="400" height="400"></canvas>
                                <p>Sydney</p></td>
                            <td>
                                <canvas class="worldClock" 
                                        id="cvWorldClockHonolulu"
                                        width="400" height="400"></canvas>
                                <p>Honolulu</p></td>
                            <td>
                                <canvas class="worldClock" 
                                        id="cvWorldClockAnchorage"
                                        width="400" height="400"></canvas>
                                <p>Anchorage</p></td>
                        </tr>
                        <tr>
                            <td>
                                <canvas class="worldClock" 
                                        id="cvWorldClockLosAngeles"
                                        width="400" height="400"></canvas>
                                <p>Los Angeles</p></td>
                            <td>
                                <canvas class="worldClock" 
                                        id="cvWorldClockDenver"
                                        width="400" height="400"></canvas>
                                <p>Denver</p></td>
                            <td>
                                <canvas class="worldClock" 
                                        id="cvWorldClockChicago"
                                        width="400" height="400"></canvas>
                                <p>Chicago</p></td>
                            <td>
                                <canvas class="worldClock" 
                                        id="cvWorldClockNewYorkCity"
                                        width="400" height="400"></canvas>
                                <p>New York</p></td>
                        </tr>
                        <tr>
                            <td>
                                <canvas class="worldClock" 
                                        id="cvWorldClockHalifax"
                                        width="400" height="400"></canvas>
                                <p>Halifax</p></td>
                            <td>
                                <canvas class="worldClock" 
                                        id="cvWorldClockRioDeJaneiro"
                                        width="400" height="400"></canvas>
                                <p>Rio De Janeiro</p></td>                            
                        </tr>
                    </table>
                </div>
                <div id="dvWeather">
                    <div id="dvWeatherFormWindow">
                        <h2>Enter Coordinates</h2>
                        <form action="index.php" method="GET">							
                            <input type="text" id="txtLatitiude" name="latitude" />
                            <label for="txtLatitude">&degN </label>

                            <input type="text" id="txtLongitiude" name="longitude" />
                            <label for="txtLongitude">&degW	</label>

                            <input type="submit" id="btnSubmitWeather" />                            
                        </form>
                        <p></p>
                    </div>
                    <div id="dvWeatherWindow">
                        <?php
                        //Get arguments
                        $latitude = isset($_GET["latitude"]) ? $_GET["latitude"] : "";
                        $longitude = isset($_GET["longitude"]) ? $_GET["longitude"] : "";

                        //Sanitize inputs and pass to server side script
                        if ($latitude == "" && $longitude == "") {
                            echo "";
                        } else if ($latitude == "") {
                            displayError("Latitude field is blank");
                        } else if ($longitude == "") {
                            displayError("Longitude field is blank");
                        } else if (!is_numeric($latitude)) {
                            displayError("Latitude Field is not numeric");
                        } else if (!is_numeric($longitude)) {
                            displayError("Longitude Field is not numeric");
                        } else {
                            echo shell_exec("python python/weather.py "
                                    . $latitude . " " . $longitude);
                        }

                        function displayError($message) {
                            echo "<h3>Error</h3>";
                            echo "<p>" . $message . "</p>";
                        }
                        ?>
                    </div>                    
                </div>    
                <div id="dvBulletinBoard">
                    <input type='button' id='btnAddPost' value='Add a Post' />					
                    <?php
                    //Declare variables
                    $db = mysqli_connect('localhost', 'web', 'webaccess', 'bulletinBoard');
                    $query = "CALL bulletinBoard.sp_select_all_posts();";

                    //Test for any connection errors
                    if (mysqli_connect_errno()) {
                        echo "Connection failure";
                    } else {

                        //Query the results
                        $result = $db->query($query);

                        //Test to see if there are any results
                        if ($result->num_rows > 0) {

                            //Loop through the results and append to the page
                            $outputString = "";
                            while ($row = $result->fetch_assoc()) {
                                $name = $row['UserName'];
                                $content = $row['Content'];
                                $date = $row['PostDate'];
                                $owner = $row['IsOwner'];

                                $name = str_replace("<", "&#60", $name);
                                $content = str_replace("<", "&#60", $content);

                                $outputString = printResult($name, $content,
                                                $date, $owner) . $outputString;
                            }
                            echo $outputString;
                        } else {
                            echo "<p>No posts</p>";
                        }

                        //Close the connection
                        $db->close();
                    }

                    function printResult($name, $content, $date, $owner) {

                        $output = "";

                        $output .= "<div class='bulletinBoardPost'
                            style='border: 1px solid #c5c5c5; 
                            margin: 5px 0px 5px 0px; 
                            padding: .5em;
                            border-radius: 10px;
                            background-color: #f6f6f6'>";
                        if ($owner) {
                            $output .= "<h3 style='color: blue;'>" . $name .
                                    " On " . $date . "</h3>";
                        } else {
                            $output .= "<h3>" . $name . " On " . $date . "</h3>";
                        }
                        $output .= "<p>" . $content . "</p>";
                        $output .= "</div>";
                        return $output;
                    }
                    ?>
                    <div id="dvAddPost">
                        <form action="php/addpost.php" method="GET" id="frmSubmitPost">                            
                            <input type="text" name="name" id="txtName" 
                                   placeholder="Enter your name" />
                            <br />

                            <textarea name="content" id="txtaContent"
                                      placeholder="Enter content here" 
                                      name="content" ></textarea>
                            <br />

                            <input type="submit" value="Submit" id="btnSubmitPost"/>
                        </form>
                        <p>WARNING: Posts are for public viewing and are 
                            liable to be removed at administrator discretion</p>
                    </div>
                </div>                
                <div id="dvCalculator">
                    <input type="text" value="0" id="calcOutput" disabled/>
                    <table width="300">
                        <tr>
                            <td>
                                <input type="button" id="calcBtnPi" value="π" class="calcConst"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtnSqrRoot" value="√" class="calcEval"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtnSin" value="sin" class="calcEval"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtnClr" value="C" class="calcOther"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtnClra" value="CE" class="calcOther"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtnBK" value="<-" class="calcOther"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtnDiv" value="/" class="calcOperator"/>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <input type="button" id="calcBtnE" value="e" class="calcConst"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtnSqr" value="x²" class="calcEval"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtnCos" value="cos" class="calcEval"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtn7" value="7" class="calcNumber"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtn8" value="8" class="calcNumber"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtn9" value="9" class="calcNumber"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtnMult" value="x" class="calcOperator"/>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <input type="button" id="calcBtnFact" value="!" class="calcEval"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtnCub" value="x³" class="calcEval"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtnTan" value="tan" class="calcEval"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtn4" value="4" class="calcNumber"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtn5" value="5" class="calcNumber"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtn6" value="6" class="calcNumber"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtnSub" value="-" class="calcOperator"/>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <input type="button" id="calcBtnAbs" value="abs" class="calcEval"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtnPwr" value="^" class="calcOperator"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtnMod" value="%" class="calcOperator"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtn1" value="1" class="calcNumber"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtn2" value="2" class="calcNumber"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtn3" value="3" class="calcNumber"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtnAdd" value="+" class="calcOperator"/>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <input type="button" id="calcBtnRound" value="round" class="calcEval"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtnNtLog" value="ln" class="calcEval"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtnLog" value="log" class="calcEval"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtnNegative" value="±" class="calcNumMod"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtn0" value="0" class="calcNumber"/>
                            </td>
                            
                            <td>
                                <input type="button" id="calcBtnDecimal" value="." class="calcNumMod"/>
                            </td>
                            <td>
                                <input type="button" id="calcBtnEval" value="=" class="calcOther"/>
                            </td>
                        </tr>
                    </table>
                </div>               
            </div>            
        </main>
    </body>
</html>
