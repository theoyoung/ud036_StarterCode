import fresh_tomatoes
import media

copying_beethoven = media.Movie("Copying Beethoven"
                        , "A story of Conflict and empathy between Beethoven and his student, a fictional character"
                        ,"https://upload.wikimedia.org/wikipedia/en/3/3e/CopyingbeethovenNEW.jpg"
                        ,"https://www.youtube.com/watch?v=ROsbGWFltU0")

farinelli = media.Movie("Farinelli"
                        , "The life and career of Farinelli, considered the greatest castrato singer of all time."
                        ,"https://upload.wikimedia.org/wikipedia/en/4/46/Farinelli.jpg"
                        ,"https://www.youtube.com/watch?v=tY9blMDJAVc")

amadeus = media.Movie("Amadeus"
                        , "Salieri's confession about his relationship with Mozart"
                        ,"https://upload.wikimedia.org/wikipedia/en/thumb/2/2f/Amadeusmov.jpg/220px-Amadeusmov.jpg"
                        ,"https://www.youtube.com/watch?v=3qikgX4rlG4")


the_mission = media.Movie("The Mission"
                        , "A story of Father Gabriel who enters the South American jungle to evangelize."
                        ,"https://upload.wikimedia.org/wikipedia/en/5/5a/The_mission.jpg"
                        ,"https://www.youtube.com/watch?v=LXHr0Vn7sow")


four_minutes = media.Movie("Four Minutes"
                        , "The empathy between a piano teacher and imprisoned girl through music."
                        ,"https://upload.wikimedia.org/wikipedia/en/0/06/Film_vier_minuten.jpg"
                        ,"https://www.youtube.com/watch?v=OoZU8mU0kVE")

manon = media.Movie("Manon of the Spring"
                        , "A long-running feud between two families over the spring"
                        ,"https://upload.wikimedia.org/wikipedia/en/thumb/7/7b/Manon_des_Sources_ver2.jpg/220px-Manon_des_Sources_ver2.jpg"
                        ,"https://www.youtube.com/watch?v=BxScSXKXwPc")

movies = [copying_beethoven, farinelli, amadeus, the_mission, four_minutes, manon]
fresh_tomatoes.open_movies_page(movies)


