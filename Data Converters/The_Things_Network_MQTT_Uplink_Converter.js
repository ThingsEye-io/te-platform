////Version: 0.1
var data = decodeToJson(payload);
var deviceName = data.end_device_ids.device_id;
var deviceType = data.end_device_ids.application_ids.application_id;
var model = {};
var data2 = data.uplink_message.decoded_payload;
var flg = data.uplink_message.f_port
for (var key in data2) {
    model[key] = data2[key];
}
var obj =  {"devid":deviceName}
var result = {
    deviceName: deviceName,
    deviceType: deviceType,
    telemetry: model,
    groupName: "Case Study",
    attributes:{"devid":deviceName,
        "timevalue":"test",
        "inactivityTimeout":1260000
    }
};
function decodeToString(payload) {
    return String.fromCharCode.apply(String, payload);
}function decodeToJson(payload) {
    var str = decodeToString(payload);
    var data = JSON.parse(str);
    return data;
}
if (flg===2){
return result;
}
