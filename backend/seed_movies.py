from app.database import SessionLocal
from app.models import Movie, Genre

movies = [
    {
        "title": "The Dark Knight",
        "year": 2008,
        "rating": 9.0,
        "description": "Batman faces a criminal mastermind who plunges Gotham into chaos.",
        "poster_url": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
    },
    {
        "title": "Inception",
        "year": 2010,
        "rating": 8.8,
        "description": "A thief who steals corporate secrets through dream-sharing technology is given a difficult task.",
        "poster_url": "https://image.tmdb.org/t/p/w500/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg",
    },
    {
        "title": "Fight Club",
        "year": 1999,
        "rating": 8.8,
        "description": "An office worker and a soap maker form an underground fight club.",
        "poster_url": "https://image.tmdb.org/t/p/w500/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg",
    },
    {
        "title": "Forrest Gump",
        "year": 1994,
        "rating": 8.8,
        "description": "The life story of a kind-hearted man who witnesses several defining historical events.",
        "poster_url": "https://image.tmdb.org/t/p/w500/arw2vcBveWOVZr6pxd9XTd1TdQa.jpg",
    },
    {
        "title": "The Matrix",
        "year": 1999,
        "rating": 8.7,
        "description": "A hacker discovers that the world he knows is a simulated reality.",
        "poster_url": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
    },
    {
        "title": "Gladiator",
        "year": 2000,
        "rating": 8.5,
        "description": "A former Roman general seeks revenge against the emperor who betrayed him.",
        "poster_url": "https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg",
    },
    {
        "title": "The Prestige",
        "year": 2006,
        "rating": 8.5,
        "description": "Two rival magicians become obsessed with creating the ultimate illusion.",
        "poster_url": "https://image.tmdb.org/t/p/w500/bdN3gXuIZYaJP7ftKK2sU0nPtEA.jpg",
    },
    {
        "title": "Whiplash",
        "year": 2014,
        "rating": 8.5,
        "description": "A young drummer is pushed to his limits by a demanding music instructor.",
        "poster_url": "https://image.tmdb.org/t/p/w500/7fn624j5lj3xTme2SgiLCeuedmO.jpg",
    },
    {
        "title": "Joker",
        "year": 2019,
        "rating": 8.4,
        "description": "A struggling comedian slowly descends into isolation and violence.",
        "poster_url": "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg",
    },
    {
        "title": "Parasite",
        "year": 2019,
        "rating": 8.5,
        "description": "A struggling family becomes involved with a wealthy household in unexpected ways.",
        "poster_url": "https://image.tmdb.org/t/p/w500/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg",
    },
    {
        "title": "Dune",
        "year": 2021,
        "rating": 8.0,
        "description": "A young noble travels to the most dangerous planet in the universe.",
        "poster_url": "https://image.tmdb.org/t/p/w500/d5NXSklXo0qyIYkgV94XAgMIckC.jpg",
    },
    {
        "title": "Oppenheimer",
        "year": 2023,
        "rating": 8.3,
        "description": "The story of physicist J. Robert Oppenheimer and the development of the atomic bomb.",
        "poster_url": "https://image.tmdb.org/t/p/w500/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
    },
    {
        "title": "Blade Runner 2049",
        "year": 2017,
        "rating": 8.0,
        "description": "A young blade runner uncovers a secret that could change society.",
        "poster_url": "https://image.tmdb.org/t/p/w500/gajva2L0rPYkEWjzgFlBXCAVBE5.jpg",
    },
    {
        "title": "Mad Max: Fury Road",
        "year": 2015,
        "rating": 8.1,
        "description": "Survivors flee across a wasteland while being pursued by a tyrannical ruler.",
        "poster_url": "https://image.tmdb.org/t/p/w500/hA2ple9q4qnwxp3hKVNhroipsir.jpg",
    },
    {
        "title": "The Social Network",
        "year": 2010,
        "rating": 7.8,
        "description": "The story behind the creation of Facebook and the conflicts that followed.",
        "poster_url": "https://image.tmdb.org/t/p/w500/n0ybibhJtQ5icDqTp8eRytcIHJx.jpg",
    },
    {
        "title": "Arrival",
        "year": 2016,
        "rating": 7.9,
        "description": "A linguist attempts to communicate with mysterious visitors from another world.",
        "poster_url": "https://image.tmdb.org/t/p/w500/x2FJsf1ElAgr63Y3PNPtJrcmpoe.jpg",
    },
    {
        "title": "The Wolf of Wall Street",
        "year": 2013,
        "rating": 8.2,
        "description": "The rise and fall of a wealthy stockbroker caught in corruption and excess.",
        "poster_url": "https://image.tmdb.org/t/p/w500/34m2tygAYBGqA9MXKhRDtzYd4MR.jpg",
    },
    {
        "title": "Shutter Island",
        "year": 2010,
        "rating": 8.2,
        "description": "A U.S. marshal investigates the disappearance of a patient from a remote institution.",
        "poster_url": "https://image.tmdb.org/t/p/w500/4GDy0PHYX3VRXUtwK5ysFbg3kEx.jpg",
    },
    {
        "title": "The Grand Budapest Hotel",
        "year": 2014,
        "rating": 8.1,
        "description": "A hotel concierge becomes involved in a bizarre inheritance dispute.",
        "poster_url": "https://image.tmdb.org/t/p/w500/eWdyYQreja6JGCzqHWXpWHDrrPo.jpg",
    },
    {
    "title": "Pulp Fiction",
    "year": 1994,
    "rating": 8.9,
    "description": "The lives of several criminals intertwine in a series of violent and unexpected events.",
    "poster_url": "https://image.tmdb.org/t/p/w500/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg",
},
{
    "title": "Se7en",
    "year": 1995,
    "rating": 8.6,
    "description": "Two detectives hunt a serial killer who uses the seven deadly sins as his motives.",
    "poster_url": "https://image.tmdb.org/t/p/w500/6yoghtyTpznpBik8EngEmJskVUO.jpg",
},
{
    "title": "The Silence of the Lambs",
    "year": 1991,
    "rating": 8.6,
    "description": "A young FBI trainee seeks help from an imprisoned psychiatrist to catch a serial killer.",
    "poster_url": "https://image.tmdb.org/t/p/w500/uS9m8OBk1A8eM9I042bx8XXpqAq.jpg",
},
{
    "title": "Goodfellas",
    "year": 1990,
    "rating": 8.7,
    "description": "A young man rises through the ranks of organized crime.",
    "poster_url": "https://image.tmdb.org/t/p/w500/aKuFiU82s5ISJpGZp7YkIr3kCUd.jpg",
},
{
    "title": "The Green Mile",
    "year": 1999,
    "rating": 8.6,
    "description": "A prison guard encounters an inmate with an extraordinary gift.",
    "poster_url": "https://image.tmdb.org/t/p/w500/8VG8fDNiy50H4FedGwdSVUPoaJe.jpg",
},
{
    "title": "Saving Private Ryan",
    "year": 1998,
    "rating": 8.6,
    "description": "A group of soldiers searches for a paratrooper during World War II.",
    "poster_url": "https://image.tmdb.org/t/p/w500/uqx37cS8cpHg8U35f9U5IBlrCV3.jpg",
},
{
    "title": "The Departed",
    "year": 2006,
    "rating": 8.5,
    "description": "An undercover officer and a police informant attempt to identify each other.",
    "poster_url": "https://image.tmdb.org/t/p/w500/nT97ifVT2J1yMQmeq20Qblg61T.jpg",
},
{
    "title": "Django Unchained",
    "year": 2012,
    "rating": 8.5,
    "description": "A freed slave joins a bounty hunter on a mission across the American South.",
    "poster_url": "https://image.tmdb.org/t/p/w500/7oWY8VDWW7thTzWh3OKYRkWUlD5.jpg",
},
{
    "title": "The Intouchables",
    "year": 2011,
    "rating": 8.5,
    "description": "An unlikely friendship develops between a wealthy man and his caregiver.",
    "poster_url": "https://image.tmdb.org/t/p/w500/1QU7HKgsQbGpzsJbJK4pAVQV9F5.jpg",
},
{
    "title": "The Pianist",
    "year": 2002,
    "rating": 8.5,
    "description": "A Polish pianist struggles to survive the destruction of Warsaw during World War II.",
    "poster_url": "https://image.tmdb.org/t/p/w500/2hFvxCCWrTmCYwfy7yum0GKRi3Y.jpg",
},
{
    "title": "Memento",
    "year": 2000,
    "rating": 8.4,
    "description": "A man with short-term memory loss searches for the person responsible for his wife's death.",
    "poster_url": "https://image.tmdb.org/t/p/w500/yuNs09hvpHVU1cBTCAk9zxsL2oW.jpg",
},
{
    "title": "The Truman Show",
    "year": 1998,
    "rating": 8.2,
    "description": "A man slowly discovers that his entire life is part of a television show.",
    "poster_url": "https://image.tmdb.org/t/p/w500/vuza0WqY239yBXOadKlGwJsZJFE.jpg",
},
{
    "title": "Gone Girl",
    "year": 2014,
    "rating": 8.1,
    "description": "A woman's disappearance puts her husband at the center of a media investigation.",
    "poster_url": "https://image.tmdb.org/t/p/w500/ts996lKsxvjkO2yiYG0ht4qAicO.jpg",
},
{
    "title": "Prisoners",
    "year": 2013,
    "rating": 8.2,
    "description": "A father takes matters into his own hands after his daughter disappears.",
    "poster_url": "https://image.tmdb.org/t/p/w500/uhviyknTT5cEQXbn6vWIqfM4vGm.jpg",
},
{
    "title": "The Imitation Game",
    "year": 2014,
    "rating": 8.0,
    "description": "Mathematician Alan Turing works to break the German Enigma code during World War II.",
    "poster_url": "https://image.tmdb.org/t/p/w500/zSqJ1qFq8NXFfi7JeIYMlzyR0dx.jpg",
},
{
    "title": "Nightcrawler",
    "year": 2014,
    "rating": 7.8,
    "description": "A driven man enters the dangerous world of crime journalism in Los Angeles.",
    "poster_url": "https://image.tmdb.org/t/p/w500/j9HrX8f7GbZQm1BrBiR40uFQZSb.jpg",
},
{
    "title": "La La Land",
    "year": 2016,
    "rating": 8.0,
    "description": "An aspiring actress and a jazz musician pursue their dreams in Los Angeles.",
    "poster_url": "https://image.tmdb.org/t/p/w500/uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg",
},
{
    "title": "1917",
    "year": 2019,
    "rating": 8.2,
    "description": "Two soldiers race across enemy territory to deliver a message that could save hundreds of lives.",
    "poster_url": "https://image.tmdb.org/t/p/w500/iZf0KyrE25z1sage4SYFLCCrMi9.jpg",
},
{
    "title": "Ford v Ferrari",
    "year": 2019,
    "rating": 8.1,
    "description": "Engineers and drivers attempt to build a racing car capable of defeating Ferrari.",
    "poster_url": "https://image.tmdb.org/t/p/w500/dR1Ju50iudrOh3YgfwkAU1g2HZe.jpg",
},
{
    "title": "Jojo Rabbit",
    "year": 2019,
    "rating": 7.9,
    "description": "A young boy in wartime Germany begins to question the beliefs surrounding him.",
    "poster_url": "https://image.tmdb.org/t/p/w500/7GsM4mtM0worCtIVeiQt28HieeN.jpg",
},
{
    "title": "Knives Out",
    "year": 2019,
    "rating": 7.9,
    "description": "A detective investigates the mysterious death of a wealthy novelist.",
    "poster_url": "https://image.tmdb.org/t/p/w500/pThyQovXQrw2m0s9x82twj48Jq4.jpg",
},
{
    "title": "Everything Everywhere All at Once",
    "year": 2022,
    "rating": 7.8,
    "description": "A woman becomes caught in an adventure spanning multiple versions of reality.",
    "poster_url": "https://image.tmdb.org/t/p/w500/w3LxiVYdWWRvEVdn5RYq6jIqkb1.jpg",
},
{
    "title": "The Batman",
    "year": 2022,
    "rating": 7.8,
    "description": "Batman investigates a series of crimes uncovering corruption throughout Gotham.",
    "poster_url": "https://image.tmdb.org/t/p/w500/74xTEgt7R36Fpooo50r9T25onhq.jpg",
},
{
    "title": "Top Gun: Maverick",
    "year": 2022,
    "rating": 8.2,
    "description": "A veteran naval aviator returns to train a group of elite pilots for a dangerous mission.",
    "poster_url": "https://image.tmdb.org/t/p/w500/62HCnUTziyWcpDaBO2i1DX17ljH.jpg",
},
{
    "title": "Dune: Part Two",
    "year": 2024,
    "rating": 8.5,
    "description": "Paul Atreides joins forces with the Fremen while seeking revenge against those who destroyed his family.",
    "poster_url": "https://image.tmdb.org/t/p/w500/1pdfLvkbY9ohJlCjQH2CZjjYVvJ.jpg",
},
{
    "title": "Poor Things",
    "year": 2023,
    "rating": 7.8,
    "description": "A young woman embarks on an unusual journey of discovery and independence.",
    "poster_url": "https://image.tmdb.org/t/p/w500/kCGlIMHnOm8JPXq3rXM6c5wMxcT.jpg",
},
{
    "title": "The Holdovers",
    "year": 2023,
    "rating": 7.9,
    "description": "A teacher remains at a boarding school over the holidays with a small group of students.",
    "poster_url": "https://image.tmdb.org/t/p/w500/VHSzNBTwxV8vh7wylo7O9CLdac.jpg",
},
{
    "title": "Anatomy of a Fall",
    "year": 2023,
    "rating": 7.7,
    "description": "A writer becomes the main suspect after the mysterious death of her husband.",
    "poster_url": "https://image.tmdb.org/t/p/w500/kQs6keheMwCxJxrzV83VUwFtHkB.jpg",
},
{
    "title": "Past Lives",
    "year": 2023,
    "rating": 7.8,
    "description": "Two childhood friends reunite years after their lives took them in different directions.",
    "poster_url": "https://image.tmdb.org/t/p/w500/k3waqVXSnvCZWfJYNtdamTgTtTA.jpg",
},
{
    "title": "The Banshees of Inisherin",
    "year": 2022,
    "rating": 7.7,
    "description": "A friendship on a remote Irish island suddenly comes to an unexpected end.",
    "poster_url": "https://image.tmdb.org/t/p/w500/4yFG6cSPaCaPhyJ1vtGOtMD1lgh.jpg",
}
]

movie_genres = {
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Inception": ["Sci-Fi", "Action", "Thriller"],
    "Fight Club": ["Drama", "Thriller"],
    "Forrest Gump": ["Drama", "Comedy", "Romance"],
    "The Matrix": ["Sci-Fi", "Action"],
    "Gladiator": ["Action", "Drama"],
    "The Prestige": ["Drama", "Mystery", "Thriller"],
    "Whiplash": ["Drama", "Music"],
    "Joker": ["Drama", "Crime", "Thriller"],
    "Parasite": ["Drama", "Thriller"],
    "Dune": ["Sci-Fi", "Adventure"],
    "Oppenheimer": ["Drama", "History"],
    "Blade Runner 2049": ["Sci-Fi", "Drama"],
    "Mad Max: Fury Road": ["Action", "Adventure"],
    "The Social Network": ["Drama"],
    "Arrival": ["Sci-Fi", "Drama"],
    "The Wolf of Wall Street": ["Drama", "Comedy", "Crime"],
    "Shutter Island": ["Thriller", "Mystery"],
    "The Grand Budapest Hotel": ["Comedy", "Drama"],
"Pulp Fiction": ["Crime", "Drama"],
"Se7en": ["Crime", "Drama", "Thriller"],
"The Silence of the Lambs": ["Crime", "Thriller"],
"Goodfellas": ["Crime", "Drama"],
"The Green Mile": ["Drama", "Fantasy"],
"Saving Private Ryan": ["Drama", "War"],
"The Departed": ["Crime", "Drama", "Thriller"],
"Django Unchained": ["Drama", "Western"],
"The Intouchables": ["Comedy", "Drama"],
"The Pianist": ["Drama", "History", "War"],
"Memento": ["Mystery", "Thriller"],
"The Truman Show": ["Comedy", "Drama"],
"Gone Girl": ["Drama", "Mystery", "Thriller"],
"Prisoners": ["Crime", "Drama", "Thriller"],
"The Imitation Game": ["Drama", "History"],
"Nightcrawler": ["Crime", "Drama", "Thriller"],
"La La Land": ["Drama", "Romance", "Music"],
"1917": ["Drama", "War"],
"Ford v Ferrari": ["Drama", "Action"],
"Jojo Rabbit": ["Comedy", "Drama", "War"],
"Knives Out": ["Comedy", "Crime", "Mystery"],
"Everything Everywhere All at Once": ["Action", "Comedy", "Sci-Fi"],
"The Batman": ["Action", "Crime", "Drama"],
"Top Gun: Maverick": ["Action", "Drama"],
"Dune: Part Two": ["Sci-Fi", "Adventure", "Drama"],
"Poor Things": ["Comedy", "Drama", "Fantasy"],
"The Holdovers": ["Comedy", "Drama"],
"Anatomy of a Fall": ["Drama", "Mystery"],
"Past Lives": ["Drama", "Romance"],
"The Banshees of Inisherin": ["Comedy", "Drama"],
}

def seed_movies():
    db = SessionLocal()

    try:
        genre_names = set()

        for genres in movie_genres.values():
            genre_names.update(genres)

        genres_by_name = {}

        for genre_name in genre_names:
            genre = (
                db.query(Genre)
                .filter(Genre.name == genre_name)
                .first()
            )

            if genre is None:
                genre = Genre(name=genre_name)
                db.add(genre)
                db.flush()

            genres_by_name[genre_name] = genre

        for movie_data in movies:
            movie = (
                db.query(Movie)
                .filter(
                    Movie.title == movie_data["title"]
                )
                .first()
            )

            if movie is None:
                movie = Movie(**movie_data)
                db.add(movie)
                db.flush()

                print(
                    f"Adding movie: {movie.title}"
                )
            else:
                print(
                    f"Movie already exists: {movie.title}"
                )

            genres_for_movie = movie_genres.get(
                movie.title,
                []
            )

            for genre_name in genres_for_movie:
                genre = genres_by_name[genre_name]

                if genre not in movie.genres:
                    movie.genres.append(genre)

        db.commit()

        print("Movies and genres added successfully.")

    except Exception as error:
        db.rollback()

        print(f"Error: {error}")

    finally:
        db.close()


if __name__ == "__main__":
    seed_movies()