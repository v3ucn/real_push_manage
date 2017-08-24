var fs = require('fs');

var hashMap = {};
var query = {};

var io = require('socket.io').listen(3000);
io.sockets.on('connection', function(client) {
    console.log('Client connected'); 


    // 向客户端主动推送数据
    try {


        client.emit('real_push', '123');
        
            console.log("channel:" + channel + ", msg:"+message);
       
    }
    catch(e) {
        console.log("error:" + e);
    }
});
