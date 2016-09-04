(function () {
    var app = angular.module('accounting');

    var mainController = function($scope,$http){

        var onComplete = function (response) {
            $scope.msg = response;

        };

        var onError = function (response) {
            $scope.msg = "error";
        };

        $scope.msg = "aaa";
        $http.get("ajax/actualcounterparty/").then(onComplete,onError);

    };

    app.controller('mainController',mainController);
}());


