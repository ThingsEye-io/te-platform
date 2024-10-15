//Version: 0.1
// decode payload to string
var payloadStr = decodeToString(payload);

// decode payload to JSON
var objdata = {}
var obj1 = {}
var data = decodeToJson(payload);
var deviceName = data.IMEI;
delete data.IMEI;
var modelname = "Dragino "+data.Model
//var mod = data.mod
delete data.Model
//delete data.mod
var timestamp = new Date().getTime();
for (var key in data) {
    //objdata[key] = data[key]
    if(Number(key)){
        obj1[key]=data[key]
        obj1[key][obj1[key].length-1]=Number(new Date(obj1[key][obj1[key].length-1]))
        
    }
    else{
    objdata[key] = data[key]
}}
var listdata = [{"ts":timestamp,"values":objdata}]
for (var key1 in obj1){
    if (modelname=="Dragino RS485-NB"){
        listdata.push({"ts":obj1[key1][obj1[key1].length-1],
        "values":{"Payload":obj1[key1][0],
        }
    })
    }
    else{
        listdata.push({"ts":obj1[key1][obj1[key1].length-1],
        "values":{"values":obj1[key1]},
        })}
}
   var result = {

    deviceName: deviceName,
    deviceType: modelname,
    attributes: {
        model: modelname,
        //customerName: "NB-CB",
        //groupName: "NB-CB",
        //integrationName: metadata['integrationName']

    },
    telemetry: listdata
} 

function decodeToString(payload) {
    return String.fromCharCode.apply(String, payload);
}

function decodeToJson(payload) {
    // covert payload to string.
    var str = decodeToString(payload);

    // parse string to JSON
    var data = JSON.parse(str);
    return data;
}

return result;