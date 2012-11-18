var App = {}

var User = Backbone.Model.extend({
    initialize: function(options) {
        this.url = App.url;
        this.fname = options.firstname;
        this.lname = options.lastname;
        this.id = options.id;
        // console.log('options');
        // console.log(options);
        this.save({id: this.id, fname: this.fname, lname: this.lname});
    }
})

var Users = Backbone.Collection.extend({
    model: User
})

var AppView = Backbone.View.extend({
    initialize: function(args) {
        var that = this

        this.url = args.url
        App.url = this.url

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

                _500px.api('/users/'+user_id+'/followers', function (response) {
                    var followers = response.data.followers
                    this.followers = new Users;
                    this.followers.reset(followers)
                    // console.log(followers);
                    // followers.each(this.getPhotos)
                })
            });
        });
    },
});
