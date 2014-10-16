'use strict'

angular.module('DumpChecker.directives',[]).
    directive('appVersion', function (version) {
        return function(scope, elm, attrs) {
            elm.text(version);
        };
    });