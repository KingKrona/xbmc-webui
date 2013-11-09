var utility =  angular.module('utility', []);

utility.filter('pad', function() {
        return function(input, length, symbol) {
            n = parseInt(input, 10);
            l = parseInt(length, 10);
            symbol = symbol || ' ';
            
            if (isNaN(n) || isNaN(l)) {
                return n;
            }
            
            n = ''+n;
            while(n.length < l) {
                n = symbol + n;
            }
            
            return n;
        }
    });
    
