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
        "Description": "US Army Ranger Jackson Briggs travels with Lulu, a military dog, to the funeral of her handler. During their journey, the duo breaks laws and leaves no stone unturned in annoying each other.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/c_dog.jpg",
        "Category": C_COMEDY,
        "Views": 5,
        "Year": 2022,
        "Director": "Channing Tatum",
        "Cast": "Channing Tatum, Ethan Suplee, Kevin Nash"
        },
        {
        "ID": 2,
        "Name": "The Home Alone",
        "Description": "A married couple triy to steal back a valuable heirloom from a troublesome 10-year-old kid while his parents are away.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/c_home_alone.jpg",
        "Category": C_COMEDY,
        "Views": 3,
        "Year": 2021,
        "Director": "Dan Mazer",
        "Cast": "Archie Yates, Devin Ratray, Ellie Kemper"
        },
        {
        "ID": 3,
        "Name": "The Bubble",
        "Description": "Sneaking out. Hooking up. Melting down. The cast and crew of a blockbuster action franchise attempt to shoot a sequel while quarantining at a posh hotel.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/c_the_bubble.jpg",
        "Category": C_COMEDY,
        "Views": 4,
        "Year": 2021,
        "Director": "Judd Apatow",
        "Cast": "Maria Bakalova, Pedro Pascal, Karen Gillan"
        },
        {
        "ID": 4,
        "Name": "Sonic The Hedgehog",
        "Description": "An extraterrestrial hedgehog is discovered by a scientist with evil intentions and plans to use his superpowers for his selfish needs.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/c_sonic_the_hedgehog.jpg",
        "Category": C_COMEDY,
        "Views": 5,
        "Year": 2020,
        "Director": "Jeff Fowler",
        "Cast": "Jim Carrey, Ben Schwartz, James Marsden"
        },
        {
        "ID": 5,
        "Name": "The lost city",
        "Description": "Fictional writer Loretta's reality transforms into a dreadful adventure when she finds herself abducted on a doomed island.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/c_the_lost_city.jpg",
        "Category": C_COMEDY,
        "Views": 5,
        "Year": 2022,
        "Director": "Aaron Nee",
        "Cast": "Sandra Bullock, Channing Tatum, Brad Pitt"
        },
        {
        "ID": 6,
        "Name": "The Moon Knight",
        "Description": "Steven Grant and mercenary Marc Spector investigate the mysteries of the Egyptian gods from inside the same body.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/s_moonknight.jpg",
        "Category": C_SERIALS,
        "Views": 5,
        "Year": 2022,
        "Director": "Disney",
        "Cast": "Oscar Isaac, May Calamawy , Ethan Hawke"
        },
        {
        "ID": 7,
        "Name": "Power Book IV",
        "Description": "Tommy Egan leaves New York behind and soon finds himself in Chicago's drug game.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/s_powerbook.jpg",
        "Category": C_SERIALS,
        "Views": 5,
        "Year": 2022,
        "Director": "Robert Munic",
        "Cast": "Joseph Sikora, Lili Simmons, Audrey Esparza"
        },
        {
        "ID": 8,
        "Name": "The Young Rock",
        "Description": "Dwayne Johnson recounts his childhood and formative years in a humorous way while running for the President of the United States in 2032.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/s_young_rock.jpg",
        "Category": C_SERIALS,
        "Views": 5,
        "Year": 1995,
        "Director": "Nahnatchka Khan",
        "Cast": "Uli Latukefu, Bradley Constant, Stacey Leilua"
        },  
        {
        "ID": 9,
        "Name": "The Squid Game",
        "Description": "Hundreds of cash-strapped contestants accept an invitation to compete in children's games for a tempting prize, but the stakes are deadly.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/s_squidgame.jpg",
        "Category": C_SERIALS,
        "Views": 5,
        "Year": 2021,
        "Director": "Hwang Dong",
        "Cast": "HoYeon Jung, Lee Jung-jae"
        },  
        {
        "ID": 10,
        "Name": "The Black List",
        "Description": "A wanted fugitive mysteriously surrenders himself to the FBI and offers to help them capture deadly criminals. His sole condition is that he will work only with the new profiler, Elizabeth Keen.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/s_blacklist.jpg",
        "Category": C_SERIALS,
        "Views": 5,
        "Year": 2013,
        "Director": "Bill Roe",
        "Cast": "Megan Boone, James Spader, Ryan Eggold"
        },  
        {
        "ID": 11,
        "Name": "The 1883",
        "Description": "A prequel to Yellowstone, 1883 follows the Dutton family as they flee poverty in Texas and embark on a journey through the Great Plains to seek a better future in Montana. Real-life couple Tim McGraw and Faith Hill star as James and Margaret Dutton, while Sam Elliott portrays Shea Brennan, a tough cowboy who has sadness in his past. Other cast members include Isabel May, LaMonica Garrett and Dawn Olivieri. Billy Bob Thornton will guest star and Tom Hanks makes a cameo in a Civil War flashback scene.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/s_1883.jpg",
        "Category": C_SERIALS,
        "Views": 5,
        "Year": 2021,
        "Director": "Taylor Sheridan",
        "Cast": "Isabel May, Tim McGraw, Sam Elliott"
        },  
        {
        "ID": 12,
        "Name": "The Billions",
        "Description": "Chuck Rhoades, a sincere but ruthless US attorney, engages in an egoistic battle with hedge fund kingpin Bobby 'Axe' Axelrod as they try to outdo each other in the competitive financial market.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/s_billions.jpg",
        "Category": C_SERIALS,
        "Views": 5,
        "Year": 2016,
        "Director": "Brian Koppelman",
        "Cast": "Damian Lewis, Maggie Siff, Paul Giamatti"
        },  
        {
        "ID": 13,
        "Name": "The Peaky Blinders",
        "Description": "Tommy Shelby, a dangerous man, leads the Peaky Blinders, a gang based in Birmingham. Soon, Chester Campbell, an inspector, decides to nab him and put an end to the criminal activities.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/s_peakyblinders.jpg",
        "Category": C_SERIALS,
        "Views": 5,
        "Year": 2013,
        "Director": "Otto Bathurst",
        "Cast": "Cillian Murphy, Paul Anderson, Joe Cole"
        },  
        {
        "ID": 14,
        "Name": "The Superman & Lois",
        "Description": "After years of facing supervillains, monsters and alien invaders, the world's most famous superhero, The Man of Steel aka Clark Kent and comic books' famed journalist Lois Lane come face to face with one of their greatest challenges ever -- dealing with being working parents in today's society.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/s_superman.jpg",
        "Category": C_SERIALS,
        "Views": 5,
        "Year": 2021,
        "Director": "Amy Jo Johnson",
        "Cast": "Tyler Hoechlin, Jordan Elsass, Bitsie Tulloch"
        },  
        {
        "ID": 15,
        "Name": "The Batman",
        "Description": "Batman is called to intervene when the mayor of Gotham City is murdered. Soon, his investigation leads him to uncover a web of corruption, linked to his own dark past.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_batman.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 2022,
        "Director": "Matt Reeves",
        "Cast": "Robert Pattinson, Zoë Kravitz, Zoë Kravitz"
        },
        {
        "ID": 16,
        "Name": "The Coda",
        "Description": "Ruby is the only hearing member of a deaf family from Gloucester, Massachusetts. At 17, she works mornings before school to help her parents and brother keep their fishing business afloat. But in joining her high school's choir club, Ruby finds herself drawn to both her duet partner and her latent passion for singing.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_coda.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 1995,
        "Director": "Sian Heder",
        "Cast": "Emilia Jones, Daniel Durant, Troy Kotsur"
        },
        {
        "ID": 17,
        "Name": "The Death on the Nile",
        "Description": "Kenneth Branagh",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_death_onthenile.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 2022,
        "Director": "Kenneth Branagh",
        "Cast": "Kenneth Branagh, Armie Hammer, Gal Gadot"
        },
        {
        "ID": 18,
        "Name": "Don't Look Up",
        "Description": "Adam McKay",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_dont_lookup.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 2021,
        "Director": "Adam McKay",
        "Cast": "Jennifer Lawrence, Leonardo DiCaprio, Cate Blanchett"
        },
        {
        "ID": 19,
        "Name": "The Dune",
        "Description": "Paul Atreides arrives on Arrakis after his father accepts the stewardship of the dangerous planet. However, chaos ensues after a betrayal as forces clash to control melange, a precious resource.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_dune.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 2021,
        "Director": "Denis Villeneuve",
        "Cast": "Timothée Chalamet, Zendaya, Rebecca Ferguson"
        },
        {
        "ID": 20,
        "Name": "The Free Guy",
        "Description": "When a bank teller discovers he's actually a background player in an open-world video game, he decides to become the hero of his own story -- one that he can rewrite himself. In a world where there's no limits, he's determined to save the day his way before it's too late, and maybe find a little romance with the coder who conceived him.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_free_guy.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 2021,
        "Director": "Shawn Levy",
        "Cast": "Ryan Reynolds, Jodie Comer, Joe Keery"
        },
        {
        "ID": 21,
        "Name": "The Matrix Resurrections",
        "Description": "Thomas Anderson's seemingly ordinary life ends when he accepts Morpheus's offer, only to wake up to a new, more secure and much more dangerous Matrix.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_matrix.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 2021,
        "Director": "Lana Wachowski",
        "Cast": "Keanu Reeves, Jessica Henwick, Carrie-Anne Moss"
        },
        {
        "ID": 22,
        "Name": "The Morbius",
        "Description": "Determined to cure the disease that has plagued him his entire life, Morbius conducts a drastic experiment, which bears unforeseen consequences.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_morbius.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 2022,
        "Director": "Daniel Espinosa",
        "Cast": "Jared Leto, Matt Smith, Adria Arjona"
        },
        {
        "ID": 23,
        "Name": "The Spider-Man: No Way Home",
        "Description": "Spider-Man seeks the help of Doctor Strange to forget his exposed secret identity as Peter Parker. However, Strange's spell goes horribly wrong, leading to unwanted guests entering their universe.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_spider_man.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 2021,
        "Director": "Jon Watts",
        "Cast": "Tom Holland, Tobey Maguire, Andrew Garfield"
        },
        {
        "ID": 24,
        "Name": "The Texas Chainsaw Massacre",
        "Description": "Influencers who want to revitalise a deserted Texas town go against the infamous serial murderer Leatherface, who hides his face under a human skin mask.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_texas_chainsaw_massacre.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 2022,
        "Director": "David Blue Garcia",
        "Cast": "Elsie Fisher, Elsie Fisher, Olwen Fouéré"
        },
        {
        "ID": 25,
        "Name": "The Contractor",
        "Description": "Upon joining an underground military force, a former sergeant's first successful mission earns him trouble. So, he must strive to unearth the truth about his new employer.",
        "Picture": "http://amirhusseinsoori.ir/data/movie/images/p_the_contractor.jpg",
        "Category": C_POPULAR,
        "Views": 5,
        "Year": 2022,
        "Director": "Tarik Saleh",
        "Cast": "Chris Pine, Gillian Jacobs,Ben Foster"
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
