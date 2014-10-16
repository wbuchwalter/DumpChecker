'use strict'

angular.module('DumpChecker', [
  'DumpChecker.controllers',
  'DumpChecker.filters',
  'DumpChecker.services',
  'DumpChecker.directives',
  'ngRoute'
]).
config(function ($routeProvider, $locationProvider) {
  $routeProvider.
    when('/', {
      templateUrl: 'partials/index',
      controller: 'AppCtrl'
    }).
    when('/analytics', {
      templateUrl: 'partials/analytics',
      controller: 'AnalyticsCtrl'
    }).
    otherwise({
      redirectTo: '/'
    });

  $locationProvider.html5Mode(true);
});
