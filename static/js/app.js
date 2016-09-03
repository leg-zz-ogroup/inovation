(function () {


/*var myModel = angular.module('accounting', []).controller('mainController',mainController);
myModel.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});*/

var app = angular.module('accounting', ["ngRoute"]);

app.config(function ($routeProvider) {
    $routeProvider.when("/main",{
        templateUrl: '../../template/index.html',
        controller: "mainController"
    });
});

var mainController = function($scope){
    alert();
    $scope.msg = 'aaa';
};

}());