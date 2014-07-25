$(document).ready(function(){

    var myApiKey = 'dnpgk8svhpk3zcr564z6ydhw';

//  ajax request of rottentomatoes api

    $('#getMovie').on('click', function() {
        var searchQuery = $('#searchValue').val();
        var pageLimit = $('#arrayLimit').val();

        $.ajax({
            url: 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=' + myApiKey + '&q=' + searchQuery + '&page_limit=' + pageLimit,
            type: 'GET',
            dataType: 'jsonp',
            success: function (movie_response) {
                var movies = movie_response.movies;
                var movie_list = [];
                $('.favoritesDiv').hide();
                $('.searchResults').html("<h2 style='text-align:center'>Search Results</h2>").show();
                //creates movieInfo objects for each movie in search results, pushes to an array
                //Adds in appropriate movie information onto HTML page
                for(i=0; i<movies.length; i++){
                    var movie = movies[i];
                    var movieInfo = {};
                    movieInfo.title = movie.title;
                    movieInfo.release_year = movie.year;
                    movieInfo.critic_rating = movie.ratings.critics_score;
                    movieInfo.poster = movie.posters.original;
                    movieInfo.mpaa_rating = movie.mpaa_rating;
                    movieInfo.runtime = movie.runtime;
                    movieInfo.audience_score = movie.ratings.audience_score;
                    movieInfo.synopsis = movie.synopsis;
                    movie_list.push(movieInfo);
                    $('.searchResults').append("<div class='movieItem'>" +
                        "<h4 class='movieTitle'>"+movieInfo.title+"</h4>"+
                        "<img class='moviePoster'src="+movieInfo.poster+
                        "><p class='movieScore'>Movie Score: "+(movieInfo.critic_rating+movieInfo.audience_score)/2.0+
                        "</p><p class='favorited'><button class='favoriteBtn' data-id="+i+">Favorite This Movie</button></p>" +
                        "<button class='moreInfoBtn'>More Information</button>" +
                        "<div class='moreInfo' style='display:none;'><p class='mpaaRating'>MPAA Rating: "+movieInfo.mpaa_rating+
                        "</p><p class='runtime'>Runtime: "+movieInfo.runtime+"</p>" +
                        "<p class='synopsis'>"+movieInfo.synopsis+"</div></div><hr>");
                }

                //Toggles More Info Button
                $('.moreInfoBtn').on('click', function(){

                    $(this).text(function(i,text){
                        return text === "More Information" ? "Less Info" : "More Information";
                    });
                    $(this).siblings('.moreInfo').toggle()
                });


                //Saves favorite movie to database, changes button to star
                $('.favoriteBtn').on('click', function(){

                   var movie_id = $(this).data('id');
                   var movie=movie_list[movie_id];
                   $(this).parent().html("<img src='http://png-1.findicons.com/files/icons/2198/dark_glass/128/keditbookmarks.png' height=50 width=50>" );
                   movieInfo = JSON.stringify(movie);
                   $.ajax({
                        url:'/new_movie_template/',
                        type: 'POST',
                        dataType: 'html',
                        data: movieInfo,
                        success: function(movie_response) {
                            console.log(movie_response);

                        },
                        error: function(error_response){
                            console.log(error_response);
                        }
                   });
                });
            },
            error: function (error_response) {
                console.log(error_response);
            }
        });
    });


    //Hides search results, and shows the favorite movies
    $('#viewFavorites').on('click', function(){
        $.ajax({
            url:'/favorites/',
            type: 'GET',
            dataType: 'html',
            success: function(response){

                $('.searchResults').hide();
                $('.favoritesDiv').html(response).show();



                $('.removeFavorite').on('click', function(){

                    $(this).text('Deleted');

                    var movieTitle = $(this).data('title');
                    movieTitle = JSON.stringify(movieTitle);
                    //deletes selected movie from database and favorites list
                    $.ajax({
                        url:'/delete_favorite/',
                        type: 'POST',
                        dataType: 'html',
                        data: movieTitle,
                        success: function(response){
                            console.log(response);

                        },
                        error: function(error_response){
                            console.log(error_response);

                        }
                    })
                })
            },
            error: function(error_response){
                console.log(error_response)
            }
        }).complete(function(){
            $('#accordion').accordion({active: 0});
        })

    })


});








