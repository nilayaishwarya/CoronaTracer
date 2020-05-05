//var sheet = SpreadsheetApp.getActive();
//ScriptApp.newTrigger("exportEventsToMongoDB")
  //.forSpreadsheet(sheet)
  //.onFormSubmit()
  //.create();

  function exportEventsToMongoDB() {
    var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = spreadsheet.getSheetByName("Form Responses 1");
    var headerRows = 1;  // Number of rows of header info (to skip)
    var range = sheet.getDataRange(); // determine the range of populated data
    var numRows = range.getNumRows(); // get the number of rows in the range
    var data = range.getValues(); // get the actual data in an array data[row][column]
    
    for (var i=headerRows; i<numRows; i++) {
      var IdCell = range.getCell(i+1,20);
      
      var idcheck = data[i][19];
      if (!idcheck) {
        continue;
      }
      //var desc = data[i][columns.Timestamp];
      //var date_start = Utilities.formatDate(new Date(data[i][columns.date_start]), "GMT", "yyyy-MM-dd'T'HH:mm:ss'Z'");
      //var date_end = Utilities.formatDate(new Date(data[i][columns.date_end]), "GMT", "yyyy-MM-dd'T'HH:mm:ss'Z'");   
      var Timestamp = data[i][0];
      var Age = data[i][1];
      var Gender = data[i][2];
      var Weight =  data[i][3];
      var BloodGroup = data[i][4];
      if(data[i][5]=='Yes'){
        var PastResp = true; 
      }
      else{
        var PastResp = false;
      }
      
      if(data[i][6]){
        var PastRespDesc = data[i][6];
      }
      else{
        var PastRespDesc = "";
      }
      
      if(data[i][7]=='Yes'){
        var PastCardio = true; 
      }
      else{
        var PastCardio = false;
      }
      
      var PastCardioDesc = data[i][8];
      
      if(data[i][9]=='Yes'){
        var Diabetic = true; 
      }
      else{
        var Diabetic = false;
      }
      
      var lat = data[i][10];
      var long = data[i][11];
      
      var city = data[i][12];
      var locality = data[i][13];
      var state = data[i][14];
      var country = data[i][15];
      if(data[i][16]=='Yes'){
        var travelled = true; 
      }
      else{
        var travelled = false;
      }
      
      var travelleddesc = data[i][17];
      var email= data[i][18];
      
      
      // Make a POST request with form data.
      var formData = {
        'Timestamp':Timestamp,
        'Age': Age,
        'Gender': Gender,
        'Weight': Weight,
        'BloodGroup': BloodGroup,
        'PastResp': PastResp,
        'PastRespDesc': PastRespDesc,
        'PastCardio': PastCardio,
        'PastCardioDesc': PastCardioDesc,
        'Diabetic':Diabetic,
        'lat':lat,
        'long':long,
        'city':city,
        'locality':locality,
        'state':state,
        'country':country,
        'travelled':travelled,
        'travelleddesc':travelleddesc,
        'email':email 
      };
       
      var options = {
        'method' : 'post',
        'Content-Type' : 'application/json',
        'payload' : formData
      };
      Logger.log('enteredno');
      if (!idcheck) {
        Logger.log('entered');
        var insertID = UrlFetchApp.fetch('<link hidden>', options);
        IdCell.setValue(insertID); // Insert the new event ID
     }
    }
    
  }