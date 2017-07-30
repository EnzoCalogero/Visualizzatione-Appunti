// static/js/script.js
var API_URL = 'http://127.0.0.1:8000/api';

var displayJSON = function(query) {

    d3.json(API_URL + query, function(error, data) {

        // log any error to the console as a warning
        if(error){
            return console.warn(error);
        }

        d3.select('#query pre').html(query); 
        d3.select('#data pre').html(JSON.stringify(data, null, 4));
        console.log(data);
    });
};

var query = 'api/winners?where=' + JSON.stringify({ 
    "country": {"$gt":2000},
    "France": "female"
});

displayJSON(query);