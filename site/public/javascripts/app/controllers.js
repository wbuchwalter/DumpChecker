'use strict';

angular.module('DumpChecker.controllers', []).
  controller('AppCtrl', function ($scope, $http) {
    $scope.data = {criteria:''};
    $scope.isLoading = false;

    $http.get('/api/count').
        success(function (data) {
            $scope.nbIdLeaked = data;
        })

    $scope.search = function () {
        $scope.response = {};
        $scope.isLoading = true;
        $http.get('/api/search/' + $scope.data.criteria).
        success(function(data) {
                $scope.isLoading = false;
                $scope.response.isHacked = data;
            });
    };

  }).
  controller('AnalyticsCtrl', function ($scope) {


  });
