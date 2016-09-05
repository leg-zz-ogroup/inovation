(function () {
    var app = angular.module('accounting');

    var mainController = function($scope,$http){
        $scope.msg = "Main Page";

    };

    app.controller('mainController',mainController);

}());


