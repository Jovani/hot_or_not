$(function() {
    _500px.init({
        sdk_key: '5318bce8cc510bcc7f48a74feab6d6bc18d7d944'
    });

    // _500px.on('authorization_obtained', function() {
    //     // window.location.href = 'http://www.google.ca'
    //     console.log(self);
    //     _500px.api('/users', function (response) {
    //     	console.log(response.user);
    //     });

    // });
    _500px.getAuthorizationStatus();

    $('#login').click(_500px.login(function (status) {
    	if (status === 'authorized') {
			_500px.api('/users', function (response) {
				console.log(response.user);
			});
    	} else {
    		console.log('Not logged in');
    	}


    }));
});
