var User = Backbone.Model.extend({
    initialize: function(options) {
        this.url = options.login_url;
        console.log(options);
        this.save({id: options.id, fname: options.fname, lname: options.lname});
    }
})

var AppView = Backbone.View.extend({
    initialize: function(args) {
        console.log('appview');
        var that = this
        this.url = args.url

        console.log(this.url)
        _500px.init({
            sdk_key: '5318bce8cc510bcc7f48a74feab6d6bc18d7d944'
        });

        _500px.ensureAuthorization(function () {
            _500px.api('/users', function (response) {
                console.log(response.data.user)
                var user_id = response.data.user.id;
                var user_firstname = response.data.user.firstname;
                var user_lastname = response.data.user.lastname;
                console.log(user_id, user_firstname, user_lastname)

                _500px.api('/users/:',user_id,'/followers', function (response) {
                    console.log(response);


                })

                // var user = new User({id: user_id, fname: user_firstname, lname: user_lastname, login_url: that.url});
            });
        });
    }
});
