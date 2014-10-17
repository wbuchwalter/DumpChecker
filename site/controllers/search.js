var mongoose = require('mongoose');

exports.search = function (req, res) {

    var query = req.params.query;

    mongoose.connect('mongodb://localhost:27017/leakChecker');
    var db = mongoose.connection;
    var dumpItemsSchema = mongoose.Schema({
        mail : String
    });

    var dumpItems = db.model('dumpItems', dumpItemsSchema,'dumpItems');

    dumpItems.find({mail : query}).limit(1).exec(function (err,item) {
        if(err)
            console.error(err);
        console.log(item);
        res.send(item.length > 0);
        db.close();
    });
};