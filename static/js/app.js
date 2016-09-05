(function () {

    'use strict';
    var app = angular.module('accounting', ['ngRoute', 'ngAnimate', 'ngSanitize', 'mgcrea.ngStrap', 'ui.grid']);

    app.config(function ($routeProvider) {
        $routeProvider
            .when("/", {
                templateUrl: "static/template/mainPage.html",
                controller: "mainController"
            })
            .when("/counterGrid", {
                templateUrl: "static/template/grid/counter.html"
            })
            .when("/addCounterParty", {
                templateUrl: 'static/template/addCounterParty.html',
                controller: "addCounterPartyController"
            });
    }).config(function ($modalProvider) {
        angular.extend($modalProvider.defaults, {
            html: true
        });
    });


}());

