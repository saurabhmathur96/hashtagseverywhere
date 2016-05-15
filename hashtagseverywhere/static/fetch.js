function fetch(options, callback) {
  var xhr = new XMLHttpRequest();
  xhr.onload = function() {
    if (4 == xhr.readyState) {
      var response = {
        status: xhr.status,
        text: xhr.responseText
      }
      return callback(null, response);
    }
    callback(new Error('unable to fetch data'));
  }
  xhr.open(options.method, options.url, true);
  xhr.send(null || options.data);
}
