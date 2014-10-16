'use strict';

angular.module('DumpChecker.controllers', []).
  controller('AppCtrl', function ($scope, $http) {

    $scope.data = {mail:'enter email'};

    $scope.search = function () {
        $http.get('/api/search/' + $scope.data.mail).
        success(function(data) {
                $scope.response = data;
            });
    };

  }).
  controller('AnalyticsCtrl', function ($scope) {


  });
