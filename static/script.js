// script.js

    // create the module and name it scotchApp
        // also include ngRoute for all our routing needs
    var junostyApp = angular.module('junostyApp', ['ngRoute']);

    // configure our routes
    junostyApp.config(function($routeProvider) {
        $routeProvider

            // Ruta para el perfil
            .when('/perfil', {
                templateUrl : 'pages/perfil.html',
                controller  : 'perfilController'
            })

            // Ruta para calendario
            .when('/calendario', {
                templateUrl : 'pages/calendario.html',
                controller  : 'calendarioController'
            })

						// Ruta para horario
            .when('/horario', {
                templateUrl : 'pages/horario.html',
                controller  : 'horarioController'
            })

						// Ruta para alertas
            .when('/alertas', {
                templateUrl : 'pages/alertas.html',
                controller  : 'alertasController'
            })

            // Ruta para el login
            .when('/login', {
                templateUrl : 'pages/login.html',
                controller  : 'loginController'
            })

            // Ruta para el registro
            .when('/registro', {
                templateUrl : 'pages/registro.html',
                controller  : 'registroController'
            })

            // Ruta para el materias
            .when('/materias', {
                templateUrl : 'pages/materias.html',
                controller  : 'materiasController'
            });
    });

    // crea el controlador e inyecta las vistas de angular
    junostyApp.controller('perfilController', function($scope) {
        // Un mensaje para mostrar en nuestra vista
        $scope.message = 'Perfil';
    });

    junostyApp.controller('calendarioController', function($scope) {
        // Un mensaje para mostrar en nuestra vista
        $scope.message = 'Calendario';
    });

    junostyApp.controller('horarioController', function($scope) {
        // Un mensaje para mostrar en nuestra vista
        $scope.message = 'Horario';
    });

    junostyApp.controller('alertasController', function($scope) {
        // Un mensaje para mostrar en nuestra vista
        $scope.message = 'Alertas';
    });

    junostyApp.controller('materiasController', function($scope) {
        // Un mensaje para mostrar en nuestra vista
        $scope.message = 'Materias';
    });

    junostyApp.controller('loginController', function($scope) {
        // Un mensaje para mostrar en nuestra vista
        $scope.message = 'Inicio de sesión';
    });

    junostyApp.controller('registroController', function($scope) {
        // Un mensaje para mostrar en nuestra vista
        $scope.message = 'Registro';
    });
