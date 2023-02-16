C_ALL = "All"
C_ACTION = "Action"
C_SERIALS = "Serial"
C_COMEDY = "Comedy"
C_DRAMA = "Drama"
C_POPULAR = "Popular"
C_HORROR = "Horror"
C_FANTASY="Fantasy"


def getVideoList():
    list = [
        {
        "ID": 1,
        "Name": "The Dog",
        "Description": "Reid Carolin",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/c_dog.jpg",
        "Category": C_COMEDY,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },
        {
        "ID": 2,
        "Name": "The Home Alone",
        "Description": "Dan Mazer",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/c_home_alone.jpg",
        "Category": C_COMEDY,
        "Views": 3,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },
        {
        "ID": 3,
        "Name": "The Bubble",
        "Description": "Judd Apatow",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/c_the_bubble.jpg",
        "Category": C_COMEDY,
        "Views": 4,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },
        {
        "ID": 4,
        "Name": "sonic The Hedgehog",
        "Description": "Jeff Fowler",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/c_sonic_the_hedgehog.jpg",
        "Category": C_COMEDY,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },
        {
        "ID": 5,
        "Name": "The lost city",
        "Description": "The Aaron Nee",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/c_the_lost_city.jpg",
        "Category": C_COMEDY,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },
        {
        "ID": 6,
        "Name": "The Moon Knight",
        "Description": "Marvel",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/s_moonknight.jpg",
        "Category": C_SERIALS,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },
        {
        "ID": 7,
        "Name": "The Power Book",
        "Description": "Bart Wenrich",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/s_powerbook.jpg",
        "Category": C_SERIALS,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },
        {
        "ID": 8,
        "Name": "The Young Rock",
        "Description": "Nahnatchka Khan",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/s_young_rock.jpg",
        "Category": C_SERIALS,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },  
        {
        "ID": 9,
        "Name": "The Squid Game",
        "Description": "DC",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/s_squidgame.jpg",
        "Category": C_SERIALS,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },  
        {
        "ID": 10,
        "Name": "The Black List",
        "Description": "Joe Carnahan",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/s_blacklist.jpg",
        "Category": C_SERIALS,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },  
        {
        "ID": 11,
        "Name": "The 1883",
        "Description": "Taylor Sheridan",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/s_1883.jpg",
        "Category": C_SERIALS,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },  
        {
        "ID": 12,
        "Name": "The Billions",
        "Description": "Brian Koppelman",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/s_billions.jpg",
        "Category": C_SERIALS,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },  
        {
        "ID": 13,
        "Name": "The Peaky Blinders",
        "Description": "Historical fiction",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/s_peakyblinders.jpg",
        "Category": C_SERIALS,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },  
        {
        "ID": 14,
        "Name": "The super man",
        "Description": "Spencer Gordon Bennet",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/s_superman.jpg",
        "Category": C_SERIALS,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },  
        {
        "ID": 15,
        "Name": "The Batman",
        "Description": "Matt Reeves",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_batman.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },
        {
        "ID": 16,
        "Name": "The Coda",
        "Description": "Sian Heder",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_coda.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },
        {
        "ID": 17,
        "Name": "The Death onThebile",
        "Description": "Kenneth Branagh",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_death_onthenile.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },
        {
        "ID": 18,
        "Name": "The Dont LookUp",
        "Description": "Adam McKay",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_dont_lookup.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },
        {
        "ID": 19,
        "Name": "The Dune",
        "Description": "Denis Villeneuve",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_dune.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },
        {
        "ID": 20,
        "Name": "The Free Guy",
        "Description": "Shawn Levy",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_free_guy.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },
        {
        "ID": 21,
        "Name": "The Matrix",
        "Description": "Lana Wachowski",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_matrix.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },
        {
        "ID": 22,
        "Name": "The Morbius",
        "Description": "Daniel Espinosa",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_morbius.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },
        {
        "ID": 23,
        "Name": "The Spider Man No Way home",
        "Description": "Marvel",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_spider_man.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },
        {
        "ID": 24,
        "Name": "The Texas Chainsaw Massacre",
        "Description": "David Blue Garcia",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_texas_chainsaw_massacre.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },
        {
        "ID": 25,
        "Name": "The Contractor",
        "Description": "Tarik Saleh",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_the_contractor.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 1995,
        "Director": " ",
        "Cast": " "
        },
           ]
    return list


def getVideoHeaders():
    list = [
        {
        "ID": 1,
        "ID_VIDEO": 1,
        "Name": "john Wick 4",
        "Description": "This is video 111.",
        "Picture": "https://amirhusseinsoori.ir/data/movie/images/b_free_guy.jpg",
        },
        {
        "ID": 2,
        "ID_VIDEO": 2,
        "Name": "Free Guy",
        "Description": "This is video 222.",
        "Picture": "https://amirhusseinsoori.ir/data/movie/images/b_coda.jpg",
        },
        {
        "ID": 3,
        "ID_VIDEO": 4,
        "Name": "spider man no away home",
        "Description": "This is video 333.",
        "Picture": "https://amirhusseinsoori.ir/data/movie/images/b_spider_man.jpg",
        },
        {
        "ID": 4,     
        "ID_VIDEO": 10,
        "Name": "No time to die movie",
        "Description": "This is video 444.",
        "Picture": "https://amirhusseinsoori.ir/data/movie/images/b_peakyblinders.jpg",
        },
    ]
    return list
