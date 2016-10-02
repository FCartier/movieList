import media
import fresh_tomatoes

now_you_see_me = media.Movie("Now You See Me",
                             "An FBI agent and an Interpol detective track a team of illusionists "
                             "who pull off bank heists during their performances and reward their audiences with the money.",
                             "http://fontmeme.com/images/Now-You-See-Me-Poster.jpg",
                             "https://www.youtube.com/watch?v=4OtM9j2lcUA")

focus = media.Movie("Focus",
                    "In the midst of veteran con man Nicky's latest scheme, a woman from his past "
                    "- now an accomplished femme fatale - shows up and throws his plans for a loop.",
                    "http://image.tmdb.org/t/p//original/g2j0t85HdkaYvPTM572NZcADyiZ.jpg",
                    "https://www.youtube.com/watch?v=MxCRgtdAuBo")


the_shining = media.Movie("The Shining",
                          "A family heads to an isolated hotel for the winter where an evil and "
                          "spiritual presence influences the father into violence, while his psychic "
                          "son sees horrific forebodings from the past and of the future.",
                          "http://moviefiles.alphacoders.com/123/poster-123.jpg",
                          "https://www.youtube.com/watch?v=5Cb3ik6zP2I")

buried = media.Movie("Buried",
                     "Paul is a U.S. truck driver working in Iraq. After an attack by a group "
                     "of Iraqis he wakes to find he is buried alive inside a coffin. With only a "
                     "lighter and a cell phone it's a race against time to escape this claustrophobic death trap.",
                     "https://fanart.tv/fanart/movies/26388/movieposter/buried-5370f7cb2797e.jpg",
                     "https://www.youtube.com/watch?v=aRQ0oqFBoP4")

intouchables = media.Movie("The Intouchables",
                           "After he becomes a quadriplegic from a paragliding accident, an aristocrat "
                           "hires a young man from the projects to be his caregiver.",
                           "http://www.babel-web.eu/wp-content/uploads/2016/04/The-Intouchables-poster.jpg",
                           "https://www.youtube.com/watch?v=34WIbmXkewU")

catch_me_if_you_can = media.Movie("Catch me if you can",
                                  "The true story of Frank Abagnale Jr. who, before his 19th birthday, "
                                  "successfully conned millions of dollars' worth of checks as a Pan Am "
                                  "pilot, doctor, and legal prosecutor.",
                                  "http://images.moviepostershop.com/catch-me-if-you-can-movie-poster-2002-1020233910.jpg",
                                  "https://www.youtube.com/watch?v=71rDQ7z4eFg")

idiocracy = media.Movie("Idiocracy",
                        "Private Joe Bauers, the definition of 'average American', is selected by "
                        "the Pentagon to be the guinea pig for a top-secret hibernation program. "
                        "Forgotten, he awakes five centuries in the future. He discovers a society "
                        "so incredibly dumbed down that he's easily the most intelligent person alive.",
                        "http://ct.politicomments.com/ol/pc/sw/i57/2/4/3/pc_2d133fd1167cb8402f332d8492d26244.jpg",
                        "https://www.youtube.com/watch?v=BBvIweCIgwk")

# Create a list which contains all the movies we've created
movies = [now_you_see_me, focus, the_shining, buried,
          intouchables, catch_me_if_you_can, idiocracy]

# Launch the website
fresh_tomatoes.open_movies_page(movies)
