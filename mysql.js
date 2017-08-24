var mysql = require('mysql');
var MYSQL_HOST = '10.103.13.63';
var MYSQL_USERNAME = 'stat_anal';
var MYSQL_PASSWORD = '33gIK3fPxhhS';
var MYSQL_REAL = 'stat';

//var MYSQL_HOST = '10.10.116.33';
//var MYSQL_USERNAME = 'root';
//var MYSQL_PASSWORD = '123456';
//var MYSQL_REAL = 'lcj';

// init and connect to mysql;
var client = mysql.createConnection({
    host: MYSQL_HOST,
    user: MYSQL_USERNAME,
    password: MYSQL_PASSWORD,
    database: MYSQL_REAL,
});

// function to get list of realvv
exports.get_realvv = function(queryDatas, callback) {

    var _deviceType = queryDatas['device_type'] == undefined ? "-1" : queryDatas['device_type'];
    var _osId = queryDatas['os_id'] == undefined ? "-1" : queryDatas['os_id'];
    var _ver = queryDatas['ver'] == undefined ? "-1" : queryDatas['ver'];
    var _businessType = queryDatas['business_type'] == undefined ? "2" : queryDatas['business_type'];


    console.log('tiaoshitiaoshi:');
    console.log(_businessType);




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
