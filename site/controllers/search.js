var mongoose = require('mongoose');

var host = 'localhost';
var port = '27017';
var database = 'leakChecker';

exports.searchOne = function (req, res) {

    var query = req.params.query;

    mongoose.connect('mongodb://'+host+':'+port+'/'+database);
    var db = mongoose.connection;
    var dumpItemsSchema = mongoose.Schema({
        mail : String
    });

    var dumpItems = db.model('dumpItems', dumpItemsSchema,'dumpItems');

    dumpItems.count({mail : query}).exec(function (err,item) {
        if(err)
            console.error(err);
        console.log(item);
        res.send(item.length > 0);
        db.close();
    });
};


exports.search = function (req, res) {

    var query = req.params.query;

    mongoose.connect('mongodb://'+host+':'+port+'/'+database);
    var db = mongoose.connection;
    var dumpItemsSchema = mongoose.Schema({
        mail : String
    });

    var dumpItems = db.model('dumpItems', dumpItemsSchema,'dumpItems');

    dumpItems.find({mail : RegExp(query)}).limit(10).exec(function (err,items) {
        if(err)
            console.error(err);
        res.send(items);
        db.close();
    });
};