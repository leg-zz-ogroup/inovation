(function () {

    /*var myModel = angular.module('accounting', []).controller('mainController',mainController);
     myModel.config(function($interpolateProvider) {
     $interpolateProvider.startSymbol('{[{');
     $interpolateProvider.endSymbol('}]}');
     });*/
    var app = angular.module('accounting', ["ngRoute"]);

    app.config(function ($routeProvider) {
        $routeProvider
            .when("/", {
                templateUrl: 'static/template/mainPage.html',
                controller: "main-controller"
            })
            .when("/add-counterparty", {
                templateUrl: 'static/template/addCounterparty.html',
                controller: "counterparty-controller"
            })
            .otherwise({
                templateUrl: 'static/template/mainPage.html',
                controller: "main-controller"
            });
    });

}());