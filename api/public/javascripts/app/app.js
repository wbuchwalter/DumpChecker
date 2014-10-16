'use strict'

angular.module('DumpChecker', [
  'DumpChecker.controllers',
  'DumpChecker.filters',
  'DumpChecker.services',
  'DumpChecker.directives'
]).
config(function ($routeProvider, $locationProvider) {
  $routeProvider.
    when('/', {
      templateUrl: 'partials/index',
      controller: 'AppCtrl'
    }).
    when('/analytics', {
      templateUrl: 'partials/analytics',
      controller: 'analyticsCtrl'
    }).
    otherwise({
      redirectTo: '/'
    });

  $locationProvider.html5Mode(true);
});
