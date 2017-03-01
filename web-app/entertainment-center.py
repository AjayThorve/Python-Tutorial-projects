import media
import fresh_tomatoes



dangal=media.Movie("Dangal","Three friends decide to turn their fantasy vacation into reality after one of their number becomes engaged","https://i.ytimg.com/vi/x_7YlGv9u1g/hqdefault.jpg?custom=true&w=336&h=188&stc=true&jpg444=true&jpgq=90&sp=68&sigh=sI6CaV98ft12vEnAJ6viK4_0CMc","https://www.youtube.com/watch?v=x_7YlGv9u1g")

fan=media.Movie("Fan","","https://i.ytimg.com/vi/nkS_Ar0Yad0/hqdefault.jpg?custom=true&w=336&h=188&stc=true&jpg444=true&jpgq=90&sp=68&sigh=lsb_NR5Lq0AzLnxjGzDsqhjIc5A","https://www.youtube.com/watch?v=nkS_Ar0Yad0")
movies=[dangal,fan]

fresh_tomatoes.open_movies_page(movies)
#print media.Movie.__module__