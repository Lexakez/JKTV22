var worldApp = angular.module("worldApp",[])

worldApp.controller("countryCtrl", function ($scope, $http){
    $http({
        method: 'GET',
        url: 'js/country.json'
    }).then(function (response){
        $scope.countryList = response.data;
        //console.log($scope.countryList);
    })
})