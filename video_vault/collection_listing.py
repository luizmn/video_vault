import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Films Vault</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-color: black;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 580px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .film-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .film-tile:hover {
            background-color: #bebebe;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: black;
        }
        /* Add a gray color and text to the footer */
        footer {
            background-color: #e5e5e5;
            padding: 18px;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.film-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the films when the page loads
        $(document).ready(function () {
          $('.film-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
        // Show storyline when the mouse is over the title
        // Function copied from W3Schools.com (https://www.w3schools.com/bootstrap/bootstrap_popover.asp)
        $(document).ready(function(){
            $('[data-toggle="popover"]').popover({
                placement : 'top',
                trigger : 'hover'
            });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true"> 
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-default navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="collection_listing.html">
            <!-- Icon on the left of site name -->
              <img src="http://www.free-icons-download.net/images/movie-icon-72062.png" 
                 alt="" width="25" height="25" />  Films Vault - Trailers and Information</a>
          </div>
        </div>
      </div>

    <!-- Begin two columns design -->
    <div class="container">
        <div class="row">
            <div class="col-xs-7 col-sm-6 col-lg-8" style="background-color:red;">
                {film_tiles}
            </div>
            <div class="col-xs-5 col-sm-6 col-lg-4" style="background-color:lavender;">
                Movies Search
            </div>
    </div>
  
    </div>
    <!-- End two columns design -->
    
    <!-- <div class="container text-center"> -->   
    <!--  {film_tiles} -->
    <!-- </div> -->


</div>
 
    <!-- Here goes the code for the footer -->
    <div>
       <footer class="container-fluid text-center">
         <p>Project Movie site <span class="glyphicon glyphicon-film"></span> | User: luiz_mn</p>
       </footer>
    </div>
    <!-- Footer code end-->    
  </body>
</html>
'''


# A single film entry html template
film_tile_content = '''
<!-- <div class="col-md-5 col-lg-4 film-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer"> -->
<div class="col-sm-6 film-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster}" width="220" height="342">
    <a href="#" data-toggle="popover" title="Release year: {film_release}" data-content="{film_storyline}"><h2>{film_title}</h2></a>
</div>
'''


def create_film_tiles_content(films):
    # The HTML content for this section of the page
    content = ''
    for film in films:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', film.trailer)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', film.trailer)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the film with its content filled in
        content += film_tile_content.format(
            film_title=film.title,
            film_storyline=film.storyline,
            poster=film.poster,
            trailer_youtube_id=trailer_youtube_id,
            film_release=film.release
        )
    return content


def open_films_page(films):
    # Create or overwrite the output file
    output_file = open('collection_listing.html', 'w')

    # Replace the film tiles placeholder generated content
    rendered_content = main_page_content.format(
        film_tiles=create_film_tiles_content(films))
    
    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
