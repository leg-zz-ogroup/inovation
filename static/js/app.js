(function () {


    /*var myModel = angular.module('accounting', []).controller('mainController',mainController);
     myModel.config(function($interpolateProvider) {
     $interpolateProvider.startSymbol('{[{');
     $interpolateProvider.endSymbol('}]}');
     });*/

    var app = angular.module('accounting', ["ngRoute"]);

    app.config(function ($routeProvider) {
        $routeProvider
            .when("/main", {
                templateUrl: '../../template/index.html',
                controller: "main-controller"
            })
            .when("/add-counterparty", {
                templateUrl: '../../template/counterpart-list.html',
                controller: "counterparty-controller"
            })
            .otherwise({
                templateUrl: '../../template/index.html',
                controller: "main-controller"
            });
    });

    var main_controller = function ($scope, $http) {
        var onComplete = function (response) {
            $scope.msg = response;
        };

        var onError = function (response) {
            $scope.msg = 'Error; response = ' + response;
        };

        $scope.msg = 'aaa';
        $http.get('ajax/actualcounterparty/').then(onComplete, onError);

    };

    var counterparty_controller = function ($scope, $http) {
        $scope.msg = 'counterparty'
    };

    app.controller('main-controller', main_controller);
    app.controller('counterparty-controller', counterparty_controller);

}());