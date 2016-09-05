(function (){

    var app = angular.module('accounting');


    var modalController = function ($scope, $modal) {

        var MyModalController = function ($scope) {
            $scope.title = 'Some Title';
            $scope.content = 'Hello Modal<br />This is a multiline message from a controller!';
        };

        $scope.modal = {title: 'Title', content: 'Hello Modal<br />This is a multiline message!'};
        // Controller usage example
          //

          var myModal = $modal({controller: MyModalController ,templateUrl: '../static/template/modal/test.tpl.html', show: false});
          $scope.showModal = function() {
            myModal.$promise.then(myModal.show);
          };
          $scope.hideModal = function() {
            myModal.$promise.then(myModal.hide);
          };
    };

    app.controller('modalController', modalController);

}());

