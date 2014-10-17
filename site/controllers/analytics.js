/**
 * Created by Will on 14-10-16.
 */

var mongoose = require('mongoose');

exports.countLeakedIdentities = function (req, res) {
    mongoose.connect('mongodb://localhost:27017/leakChecker');
    db = mongoose.connection;

    var dumpItemsSchema = mongoose.Schema({
        mail : String
    });

    var dumpItems = db.model('dumpItems', dumpItemsSchema,'dumpItems');

    dumpItems.count().exec(function (err,count) {
        if(err)
            console.error(err);

        res.send(count.toString());
        db.close();
    });


};