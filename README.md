This is a practice project for applying to FLE dev team and not suitable for
production environments as it is. Its a Django based one-page application.

* The data is fetched from `data/movies.json` placed in `static` directory,
  eventually call to this file needs to be replaced by an actual API call to
  Rotten Tomatoes.

* The search functionality provided is very basic as of now. To search for a
  word, its presence is checked in all movie titles as substrings. This can be
  improved upon a lot.

* Current layout works for low number of movies but when the number of movies
  will become large, we'll either need to paginate results or lazily load those.

* For additional information on the cast, detailed results can be fetched from
  Rotten Tomatoes API.
