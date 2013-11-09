var xbmc = angular.module('xbmc', ['ngResource', 'utility']);

xbmc.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol("{/");
    $interpolateProvider.endSymbol("/}");
});

xbmc.factory('XbmcApi', function($resource) {
    return $resource(
        '/api/v1/:type/:id/',
        {
            id: '@id',
            limit: 20,
            offset: 0,
            callback: 'JSON_CALLBACK'
        },
        {
            get:{
                method: 'JSONP'
            }
        }
    );
});

xbmc.filter('thumb', function() {
        return function(html) {
            return html.replace(/<thumb.*>(.*)<\/thumb>/, "$1");
        }
    });

xbmc.controller('MovieCtrl', function ($scope, XbmcApi) {
    $scope.movies = XbmcApi.get({
        type: 'movie'
    }, function(value, responseHeaders) {
        $scope.movies.meta.offset = value.objects.length;
    }, function(httpResponse) {
        console.log("Didn't get movies");
    });
    
    $scope.more = function() {
        results = XbmcApi.get({
            type: 'movie',
            offset: $scope.movies.meta.offset
        }, function(value, responseHeaders) {
            for (var i=0, l=value.objects.length; i<l; ++i) {
                $scope.movies.objects.push(value.objects[i]);
                $scope.movies.meta.offset += l;
            }
        }, function(httpResponse) {
            console.log("Didn't get more movies");
        });
    }
});

xbmc.controller('TvShowCtrl', function ($scope, XbmcApi) {
    $scope.tvshows = XbmcApi.get({
        type: 'tvshow'
    }, function(value, responseHeaders) {
        $scope.tvshows.meta.offset = value.objects.length;
    }, function(httpResponse) {
        console.log("Didn't get tvshows");
    });

    $scope.more = function() {
        results = XbmcApi.get({
            type: 'tvshow',
            offset: $scope.tvshows.meta.offset
        }, function(value, responseHeaders) {
            for (var i=0, l=value.objects.length; i<l; ++i) {
                $scope.tvshows.objects.push(value.objects[i]);
                $scope.tvshows.meta.offset += l;
            }
        }, function(httpResponse) {
            console.log("Didn't get more tvshows");
        });
    }
});

xbmc.controller('EpisodeCtrl', function ($scope, XbmcApi) {
    $scope.episodes = XbmcApi.get({
        type: 'episode',
    }, function(value, responseHeaders) {
        $scope.episodes.meta.offset = value.objects.length;
        for (var i=0, l=$scope.episodes.objects.length; i < l; ++i) {
            $scope._loadTvShow($scope.episodes.objects[i]);
        }
    }, function(httpResponse) {
        console.log("Didn't get episodes");
    });

    $scope.more = function() {
        results = XbmcApi.get({
            type: 'episode',
            offset: $scope.episodes.meta.offset
        }, function(value, responseHeaders) {
            for (var i=0, l=value.objects.length; i<l; ++i) {
                $scope._loadTvShow(value.objects[i]);
                $scope.episodes.objects.push(value.objects[i]);
                $scope.episodes.meta.offset += l;
            }
        }, function(httpResponse) {
            console.log("Didn't get more episodes");
        });
    }
    
    $scope._loadTvShow = function(episode) {
        episode.tvshow = XbmcApi.get({
            type: 'tvshow',
            id: episode.show.replace(/.*\/tvshow\/(\d+)\/.*/, "$1")
        });
    }
});
