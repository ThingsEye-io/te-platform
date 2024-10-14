//Version: 0.1
function hexToBase64(hexString) {
    var bytes = hexString.match(/.{2}/g);
    var binaryString = bytes.map(function(byte) {
        return String.fromCharCode(parseInt(byte, 16));
    }).join('');

    return btoa(binaryString);
}
var flg = "shared_value" in metadata
var value2 = parseInt(metadata.ss_timevalue).toString(16)if (value2.length==1){
    value2 = "00000"+parseInt(metadata.ss_timevalue).toString(16)
}
else if (value2.length==2){
    value2 = "0000"+parseInt(metadata.ss_timevalue).toString(16)
}
else if (value2.length==3){
    value2 = "000"+parseInt(metadata.ss_timevalue).toString(16)
}
else if (value2.length==4){
    value2 = "00"+parseInt(metadata.ss_timevalue).toString(16)
}
else if (value2.length==5){
    value2 = "0"+parseInt(metadata.ss_timevalue).toString(16)
}
else {
    value2 = value2
}
var data = "01"+value2
if (flg === true){
data = {
        downlinks: [{
            f_port: 1,
            confirmed: false,
            frm_payload: hexToBase64(metadata.shared_value),
            priority: "NORMAL"
        }]
    };
}
else{
  data = {
        downlinks: [{
            f_port: 1,
            confirmed: false,
            frm_payload: hexToBase64(data),
            priority: "NORMAL"
        }]
    };
}
var result = {
    contentType: "JSON",
    data: JSON.stringify(data),
    metadata: {
        devId: metadata.ss_devid
    }
};
if (metadata.shared_timevalue!=="test" || metadata.ss_timevalue!=="test"){
return result;
}
