'''

Phase two: Routing + Controllers

On Modern web sites we drop the .html for things, and it is more action based.

In your browser a user would request <your site.com> + 

/ 
/about
/blog
/blog/1

1) Add two new functions index_page and about_page

2) Create a hash called urls that maps between a http request like "/" and call index_page(), 
   "/about" calls about_page()

3) Move your file reading code into both of those functions, so index_page reads index.html and
   returns that data, about_page() the same but for about.html


'''

