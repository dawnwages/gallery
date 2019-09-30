##Notes (WIP)
####Django + React is good, but Vue is Great
I'd like to use django instead of a plain old react app because of the search functionality with the API. I have experience with Wagtail from tutorials I've attended of Tom's going to Wagtail Space in Arnhem Netherlands 2019 and Philadelphia 2018. With the short time I had to work on the app this week, I was not able to incorporate any of the UI benefits that Vue would have provided.
Django is good at filters, pagination, APIs and editing the content. Django was the clear choice especially knowing that ITHAKA works on django and I've been working with django for a number of years.
I know I should wireframe first but its such a simple app, I'm going to start with initiating the app in Wagtail. In all tutorials it starts with initiating the app, but in large scale teams I always feel like starting a project works best with wireframe.

####Code roadblocks
- description has an object with it's content name has a leading underscore so a custom filter is now necessary in order to display.
- (TODO) Some of the images return with 404 errors, its needed to return a default image if there's an error.
- (TODO) characters in the description need to add escape strings for rendering character texts
- (TODO) The search could happen with django filtering and template tags or it could be done with django rest framework and query url, both of which feel out of scope right now for the time I have left. Since I'm more comfortable with DRF than creating custom django views and because the fields do need to be editable anyway, I'm going to move forward with getting the json data into the SQLite db.

###Additional Features
Looking at the JSON gives me great ideas on what additional features I could add because there is more information about the origins of the dataset, but unfortunately with time as a freelancer, devoting more time this project wasn't feasible for me.

I hope to talk through next steps in improving the app when we speak after submission.
