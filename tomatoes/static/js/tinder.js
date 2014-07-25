$(document).ready(function(){

//    $.ajax({
//        url: 'http://api.rottentomatoes.com/api/public/v1.0/movies/769959054/similar.json?apikey=88a8qpv9kwg657jxb97ma5nn&limit=3',
//        type: 'GET',
//        dataType: 'jsonp',
//        success: function(response){
//            console.log(response);
//        },
//        error: function(response){
//            console.log(response);
//        }
//    })
    var myApiKey = 'dnpgk8svhpk3zcr564z6ydhw';


    var movie_list = [];
    $('#searchButton').on('click', function(){

        var searchQuery = $('#search').val();
        var pageLimit = 1;
        var movieID;
        $.ajax({
            url: 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=' + myApiKey + '&q=' + searchQuery + '&page_limit=' + pageLimit,
            type: 'GET',
            dataType: 'jsonp',
            success: function(response){
                console.log(response.movies[0].id);
                movieID = response.movies[0].id
            },
            error: function(response){
                console.log(response)
            }
        }).complete(function(){
            $.ajax({
                url: 'http://api.rottentomatoes.com/api/public/v1.0/movies/'+movieID+'/similar.json?apikey='+myApiKey+'&limit=5',
                type: 'GET',
                dataType: 'jsonp',
                success: function(response){
                    console.log(response);
                    for(i=0; i<response.movies.length; i++ ){
                        movie = response.movies[i];
                        movieInfo = {};
                        movieInfo.title=movie.title;
                        movieInfo.poster=movie.posters.original;
                        movieInfo.identifier=movie.id;
//                        movieInfo.selfLink=movie.movie.links.self;
                        var movieLink = response.movies[i].links.self;
                        movie_list.push(movieInfo);
                         $('#recommended').append("<div class='recMovie'><p>"+response.movies[i].title +"</p>" +
                             "<div><p><button class='learnMore' data-link="+movieLink+">Learn More</button></p></div>" +
                             "<p><button class='favoriteBtn' data-id="+i+">Favorite It</button></p></div>");
                        console.log(movieLink)

                    }


                },
                error: function (response) {
                    console.log(response)
                }
            })
        })

    });

    $(document).on('click', '.learnMore', function(){
        console.log('got the button');
//        var selfId = $(this).data('id');
        var selfLink = $(this).data('link');
        var synopDest = $(this).parent().parent();
        console.log(selfLink);
        $.ajax({
            url: selfLink + '?apikey='+myApiKey,
            type: 'GET',
            dataType: 'jsonp',
            success: function(response){
                console.log(response);
                console.log(response.synopsis);
                var test = $(this).parent();
                console.log(test);
                synopDest.append("<p>"+response.synopsis+"</p>");
                synopDest.append("<img src='"+response.posters.original+"'>");

            },
            error: function(response){
                console.log(response)
            }
        })
    });

    $(document).on('click', '.favoriteBtn', function(){
        var favID = $(this).data('id');
        var favMovie = movie_list[favID];
        console.log(favMovie);
        favMovie = JSON.stringify(favMovie);
        $.ajax({
            url:'/new_favorite/',
            type: 'POST',
            dataType: 'html',
            data: favMovie,
            success: function(response){
                console.log(response)
            },
            error: function(response){
                console.log(response)
            }
        })
    })



});