// function to get list of realvv
exports.get_realvv = function(queryDatas, callback) {

    var _deviceType = queryDatas['device_type'] == "" ? "-1" : queryDatas['device_type'];
    var _osId = queryDatas['os_id'] == "" ? "-1" : queryDatas['os_id'];
    var _ver = queryDatas['ver'] == "" ? "-1" : queryDatas['ver'];
    var _businessType = queryDatas['business_type'] == "" ? "2" : queryDatas['business_type'];

    if(_ver == "-1"){
    
    client.query("select date,sum(vv) as allvv,sum(uv) as alluv,ver from stat_real_vv where device_type = ? and os_id = ? and ver = ? and business_type = ? and sdate>=(select date_add(max(sdate),interval -29 minute) from stat_real_vv) group by date",[_deviceType, _osId, _ver, _businessType],function(err, results, fields) {
        // callback function returns realvv array
        callback(results);
    });
    
    }else{

    client.query("select date,sum(vv) as allvv,sum(uv) as alluv,ver from stat_real_vv where device_type = ? and os_id = ? and ver != '-1' and business_type = ? and sdate>=(select date_add(max(sdate),interval -29 minute) from stat_real_vv) group by date,ver",[_deviceType, _osId, _businessType],function(err, results, fields) {
        // callback function returns realvv array
        callback(results);
        });
    }
}
