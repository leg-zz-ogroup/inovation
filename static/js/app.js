(function () {

var app = angular.module('accounting', ["ngRoute"]);

app.config(function ($routeProvider) {
    $routeProvider
        .when("/", {
            templateUrl: "static/template/mainPage.html",
            controller: "mainController"
        })
        .when("/addCounterParty",{
            templateUrl: 'static/template/addCounterParty.html',
            controller: "addCounterPartyController"
        });
});


}());