$(function() {
    _500px.init({
        sdk_key: '5318bce8cc510bcc7f48a74feab6d6bc18d7d944'
    });

    _500px.ensureAuthorization(function () {
        _500px.api('/users', function (response) {
            console.log("Your username is " + response.user);
        });
    });
});
