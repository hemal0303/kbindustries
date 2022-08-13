var myApp = angular.module("myModule", []);

var myController = function ($scope) {
  $scope.message = "Hello from AngularJS";

  $scope.ok = function () {
    $.post(
      "all_cats/",
      {
        name: JSON.stringify([{ id: 1, name: "Butt" }]),
      },
      function (response) {
        $scope.cat_data = response;
        console.log("full data", $scope.cat_data);
      }
    );
  };
};

myApp.controller("myController", myController);
