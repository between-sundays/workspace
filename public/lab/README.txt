LAB — loose page candidates from any agent/tool.
Drop review images here named:  BetweenSundays-Issue001-Page{NN}-{Anything}.png|jpg
(optionally a matching between-sundays-page-{NN}.html)
Then run:  python3 build_compare.py  &&  vercel deploy --prod --yes public
They appear automatically as an extra variant in that page's row on /compare.html
