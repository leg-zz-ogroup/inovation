(function () {
    var app = angular.module('accounting');

    var counterparty_controller = function ($scope) {
        $scope.msg = 'counterparty'
    };
    app.controller('counterparty-controller', counterparty_controller);
}());
