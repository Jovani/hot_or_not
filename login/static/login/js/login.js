$(document).ready(function() {
    _500px.init({
        sdk_key: '5318bce8cc510bcc7f48a74feab6d6bc18d7d944'
    });

    _500px.on('authorization_obtained', function() {
        $('#not_logged_in').hide();
        // $('#logged_in').show();
    })
    _500px.getAuthorizationStatus();

    $('#login').click(_500px.login);
});
