'use strict';

angular.module('DumpChecker.controllers', []).
  controller('AppCtrl', function ($scope) {

    $scope.mail = '';
    $scope.searchMail = function () {
      $http.get('/api/searchMail/' + $scope.mail).
        success(function(data) {

        });
    };

  }).
  controller('AnalyticsCtrl', function ($scope) {


  });
