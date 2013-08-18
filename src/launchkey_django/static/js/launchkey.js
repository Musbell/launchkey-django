(function() {
  'use strict';

  var LaunchKey = function() {};

  LaunchKey.prototype = {
    poll: function(options) {
      options = options || {};
      
      var interval = options.interval || 2000,
          url = options.url || window.location.href,
          authorized = options.authorized || function() {},
          expired = options.expired || function() {};

      if (this._poller) {
        clearInterval(this._poller);
        this._poller = null;
      }

      var launchkey = this;

      this._poller = setInterval(function() {
        launchkey._request(url, 'GET', function(xhr) {
          var response = JSON.parse(xhr.responseText);

          if (!response.pending) {
            clearInterval(launchkey._poller);
          }

          if (response.authorized) {
            return authorized();
          }

          if (response.expired) {
            return expired();
          }
        });
      }, interval);
    },
    _request: function(url, method, success) {
      method = method || 'GET';

      var xhr = new XMLHttpRequest();

      xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status == 200) {
          success(xhr);
        }
      };

      xhr.open(method, url, true);
      xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
      xhr.send();
    }
  };

  window.launchkey = window.launchkey || new LaunchKey();
})();
