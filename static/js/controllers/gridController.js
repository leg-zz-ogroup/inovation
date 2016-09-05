(function () {
    var app = angular.module('accounting');

    var counterGridController = function ($scope, $http) {

        var onComplete = function (response) {
            $scope.myData = response.data;
        };

        var onError = function (response) {
            $scope.myData = "error";
        };

        $http.get("ajax/grid/actualCounterParty/").then(onComplete, onError);

    };

    var counterGroupController = function ($scope, $http) {
        var onComplete = function (response) {
            $scope.myData = response.data;
        };

        var onError = function (response) {
            $scope.myData = "error";
        };
        $http.get("ajax/grid/counterGroup/").then(onComplete, onError);
    };
    app.controller('counterGroupController', counterGroupController);

    app.controller('counterGridController', counterGridController);

}());