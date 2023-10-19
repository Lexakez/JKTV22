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

worldApp.controller("cityCtrl",function ($scope, $http){
    $http.get('js/databaseCity.php')
    .then(function (response){$scope.cityList= response.data.records;
        console.log($scope.cityList);
    });
})