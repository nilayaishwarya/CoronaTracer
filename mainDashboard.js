var responseStateAll;
fetchStateAll();

async function fetchStateAll() {
  var responseStateAll = await fetch('<link hidden>', {
    method: 'GET'
  }).then(x => x.json())
  console.log(responseStateAll.data[0]);
  document.getElementById('mainMeterTotal').innerHTML= responseStateAll.data[0][1];
  document.getElementById('mainMeterActive').innerHTML= responseStateAll.data[0][4];
  document.getElementById('mainMeterRec').innerHTML= responseStateAll.data[0][2];
  document.getElementById('mainMeterDec').innerHTML= responseStateAll.data[0][3];
  document.getElementById('mainMeterTotalDelta').innerHTML= responseStateAll.data[0][7];
  document.getElementById('mainMeterActiveDelta').innerHTML= responseStateAll.data[0][7];
  document.getElementById('mainMeterRecDelta').innerHTML= responseStateAll.data[0][8];
  document.getElementById('mainMeterDecDelta').innerHTML= responseStateAll.data[0][9];
  debugger;
  generateTableHead(StateALLtable, responseStateAll.columns);
  generateTable(StateALLtable, responseStateAll.data);

  ///chart 
  await plotter(responseStateAll.chartTotal);

  document.getElementById('chartloading').style.display= "none";
  document.getElementById('chartenable').style.display= "block";
  console.log(responseStateAll.data[0][1]);
}

function fetchcheck(){
  debugger;
  fetchStateAll();
  debugger;
  console.log(responseStateAll)

} 


function generateTableHead(table, column) {
  let thead = table.createTHead();
  let row = thead.insertRow();
  var i = 0;
  for (i; i<5; i++) {
    let th = document.createElement("th");
    let text = document.createTextNode(column[i]);
    th.appendChild(text);
    row.appendChild(th);
  }
}

function generateTable(table, data) {
  var i = 0;
  for (i ; i<data.length ; i++) {
    let row = table.insertRow();
    var j = 0;
    for (j ; j<6 ; j++) {
       if((j!=5)&&(j!=6)){
       let cell = row.insertCell();
       var Confirmed =data[i][j]+" +"+data[i][j+6];
       if((j==0)||(j==4))
       {
        Confirmed = data[i][j];
       }
       let text = document.createTextNode(Confirmed);
       text.className = "testrowback";
       cell.appendChild(text);
    }
    }
  }
}

function ShowStateResult(){
  debugger;
  
  document.getElementById('StateTable').style.display = "none";
  var state = document.getElementById('ShowState').style.backgroundColor
}
async function Login(){
  debugger;
  document.getElementById('warningregister').style.display="none";
  resetlogin();
email= document.getElementById('emailinput').value;
email = email.toLowerCase();
var responselogin = await fetch('<link hidden>', {
    method: 'POST',
    body: JSON.stringify({email : email}),
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    
  }).then(x => x.json())

  ////Res_state
  if(responselogin.res_state.data != undefined){

    document.getElementById('idState').innerHTML = responselogin.res_state.data[0][0];
    document.getElementById('mainMeterTotState').innerHTML = responselogin.res_state.data[0][1];
    document.getElementById('mainMeterRecState').innerHTML = responselogin.res_state.data[0][2];
    document.getElementById('mainMeterDecState').innerHTML = responselogin.res_state.data[0][3];
  }
  else{
    //document.getElementById('idState').innerHTML = "-User Not Registered-";
    document.getElementById('welcomenotify').innerHTML = "<b>-User Not Registered-</b>";
    document.getElementById('warningregister').style.display ="block";
    document.getElementById('mainMeterTotState').innerHTML = "-";
    document.getElementById('mainMeterRecState').innerHTML = "-";
    document.getElementById('mainMeterDecState').innerHTML = "-";
    return false;
  }

  document.getElementById('warningregister').style.display="block";

  ////Res_city
  if(responselogin.result_city.data != undefined){
    debugger;
    var im =0;
    document.getElementById('idCity').innerHTML = responselogin.result_city.city;
    //document.getElementById('idState').innerHTML = responselogin.res_state.data[0][0];
    
    for(im = 0 ; im<responselogin.result_city.data.length;im++){
      if(responselogin.result_city.index[im] == "Hospitalized"){
        document.getElementById('mainMeterHosCity').innerHTML = responselogin.result_city.data[im];
      }

      if(responselogin.result_city.index[im] == "Recovered"){
        document.getElementById('mainMeterRecCity').innerHTML = responselogin.result_city.data[im];
      }

      if(responselogin.result_city.index[im] == "Deceased"){
        document.getElementById('mainMeterDecCity').innerHTML = responselogin.result_city.data[im];
      }
    } 

  }

  ///Self Assessment
  if((responselogin.dailyassess.daily_prep_score != undefined) && (responselogin.infoUserjson.data != undefined) ){
    selfassessment(responselogin.dailyassess,responselogin.infoUserjson,responselogin.scoreneighborhood);
  }

  if(responselogin.dailyassess.daily_prep_score != undefined){
    console.log("success");
  }
  else{
    console.log("fail");
  }
  successlogin();
}

async function plotter(inp) {
  debugger;
  var index = inp.index ;
  var datay=[];
  var datadeltatot=[];
  var datadeltarec=[];
  var datarec=[];
  var datadeltadec=[];
  var datadec=[];
  var datadate=[];
  var i=0;
  for(i; i<inp.data.length; i++){
    datay[i] = inp.data[i][2];
    datadeltatot[i] = inp.data[i][1];
    datadeltarec[i] = inp.data[i][3];
    datarec[i] = inp.data[i][4];
    datadeltadec[i] = inp.data[i][5];
    datadec[i] = inp.data[i][6];
    datadate[i]= inp.data[i][0];
  }


		var config = {
			type: 'line',
			data: {
				labels: datadate,
				datasets: [{
					label: 'Total',
					backgroundColor: window.chartColors.red,
					borderColor: window.chartColors.red,
					data: datay,
					fill: false,
        },
        {
					label: 'Delta Total',
					backgroundColor: window.chartColors.orange,
					borderColor: window.chartColors.orange,
					data: datadeltatot,
					fill: false,
        },
        {
					label: 'Recovery',
					backgroundColor: window.chartColors.green,
					borderColor: window.chartColors.green,
					data: datarec,
					fill: false,
        },
        {
					label: 'Delta Recovery',
					backgroundColor: '#0D400B' ,
					borderColor: '#0D400B',
					data: datadeltarec,
					fill: false,
        },
        {
					label: 'Deceased',
					backgroundColor: window.chartColors.grey,
					borderColor: window.chartColors.grey,
					data: datadec,
					fill: false,
        },
        {
					label: 'Delta Deceased',
					backgroundColor: window.chartColors.black,
					borderColor: window.chartColors.blank,
					data: datadeltadec,
					fill: false,
				}]
			},
			options: {
				responsive: true,
				title: {
					display: true,
					text: 'COVID-19 Case Chart (Customize using the legends)'
				},
				tooltips: {
					mode: 'index',
					intersect: false,
				},
				hover: {
					mode: 'nearest',
					intersect: true
				},
				scales: {
					xAxes: [{
						display: true,
						scaleLabel: {
              display: true
              // ,
							// labelString: ''
						}
					}],
					yAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Cases'
						}
					}]
				}
			}
    };
    
    var ctx = document.getElementById('canvas').getContext('2d');
   window.myLine = new Chart(ctx, config);

}

function selfassessment(item1,item2,item3){
  var dailyhealth = item1.risk_daily_health_score;
  var dailyprep = item1.daily_prep_score;
  var pasthealth = item2.data;

  var dailyhealthNB = item3.scoredailysoc;
  var dailyprepNB = item3.prepscoresoc;
  var pasthealthNB = item3.scorebasicsoc;
  var locality =  item3.locality;

  document.getElementById('idSympTot').innerHTML = dailyhealth;
  document.getElementById('idInv').innerHTML = dailyprep;
  document.getElementById('idPastHealth').innerHTML = pasthealth;

  //Neighbourhood
  document.getElementById('idSympTotNB').innerHTML = dailyhealthNB;
  document.getElementById('idInvNB').innerHTML = dailyprepNB;
  document.getElementById('idPastHealthNB').innerHTML = pasthealthNB;
  document.getElementById('locality').innerHTML = locality;
  //color code start
  
  if(parseFloat(dailyhealth)<=3){
    document.getElementById('colSym').style.backgroundColor = "Green";
  }
  else if(parseFloat(dailyhealth)<=6){
    document.getElementById('colSym').style.backgroundColor = "Coral";
  }
  else{
    document.getElementById('colSym').style.backgroundColor = "Red";
  }

  if(parseFloat(dailyprep)<=3){
    document.getElementById('colInv').style.backgroundColor = "Red";
  }
  else if(parseFloat(dailyprep)<=6){
    document.getElementById('colInv').style.backgroundColor = "Coral";
  }
  else{
    document.getElementById('colInv').style.backgroundColor = "Green";
  }

  if(parseFloat(pasthealth)<=3){
    document.getElementById('colPast').style.backgroundColor = "Green";
  }
  else if(parseFloat(pasthealth)<=6){
    document.getElementById('colPast').style.backgroundColor = "Coral";
  }
  else{
    document.getElementById('colPast').style.backgroundColor = "Red";
  }


  ////Neighbourhood
  if(parseFloat(dailyhealthNB)<=3){
    document.getElementById('colSymNB').style.backgroundColor = "Green";
  }
  else if(parseFloat(dailyhealthNB)<=6){
    document.getElementById('colSymNB').style.backgroundColor = "Coral";
  }
  else{
    document.getElementById('colSymNB').style.backgroundColor = "Red";
  }

  if(parseFloat(dailyprepNB)<=3){
    document.getElementById('colInvNB').style.backgroundColor = "Red";
  }
  else if(parseFloat(dailyprepNB)<=6){
    document.getElementById('colInvNB').style.backgroundColor = "Coral";
  }
  else{
    document.getElementById('colInvNB').style.backgroundColor = "Green";
  }

  if(parseFloat(pasthealthNB)<=3){
    document.getElementById('colPastNB').style.backgroundColor = "Green";
  }
  else if(parseFloat(pasthealthNB)<=6){
    document.getElementById('colPastNB').style.backgroundColor = "Coral";
  }
  else{
    document.getElementById('colPastNB').style.backgroundColor = "Red";
  }

  


}

function resetlogin(){
    document.getElementById('welcomenotify').innerHTML = "<b>LOGGING IN - COMPUTING YOUR SCORE</b>";
    document.getElementById('warningregister').style.display ="none";
    document.getElementById('PersonalStats').style.display="none";
    document.getElementById('mainMeterTotState').innerHTML = "-";
    document.getElementById('mainMeterRecState').innerHTML = "-";
    document.getElementById('mainMeterDecState').innerHTML = "-";
    document.getElementById('mainMeterHosCity').innerHTML = "-";
    document.getElementById('mainMeterRecCity').innerHTML = "-";
    document.getElementById('mainMeterDecCity').innerHTML = "-";
    document.getElementById('idSympTot').innerHTML = "-";
    document.getElementById('idInv').innerHTML = "-";
    document.getElementById('idPastHealth').innerHTML = "-";
    document.getElementById('colSym').style.backgroundColor = "Pink";
    document.getElementById('colInv').style.backgroundColor = "Pink";
    document.getElementById('colPast').style.backgroundColor = "Pink";
    ///Neighborhood
    document.getElementById('idSympTotNB').innerHTML = "-";
    document.getElementById('idInvNB').innerHTML = "-";
    document.getElementById('idPastHealthNB').innerHTML = "-";
    document.getElementById('colSymNB').style.backgroundColor = "Pink";
    document.getElementById('colInvNB').style.backgroundColor = "Pink";
    document.getElementById('colPastNB').style.backgroundColor = "Pink";
    document.getElementById('locality').innerHTML = "Neighborhood";

    
} 

function successlogin(){
  document.getElementById('welcomenotify').innerHTML = "<b>WELCOME</b>";
  document.getElementById('warningregister').style.display ="none";
  document.getElementById('PersonalStats').style.display="block";
}


