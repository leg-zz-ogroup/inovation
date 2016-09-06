(function () {
    var app = angular.module('accounting');

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

    app.controller('main-controller', main_controller);
}());
