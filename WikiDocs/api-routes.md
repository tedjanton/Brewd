## Index
* ```GET /``` - populate all instruments

## Sessions
User authorization
* ```GET /api/session``` - get/restore current session
* ```POST /api/session``` - login user via credentials
* ```DELETE /api/session``` - logout user/clear session user

## Users
* ``` POST /api/users``` - signup/create new user
* ``` GET /api/users/:id/sips``` - get sips

## Sips
* ```GET /api/sips``` - get all sips (The Coffee House)
* ```POST /api/sips``` - create a new sip
* ```POST /api/sips/:id``` - edit your sip
* ```DELETE /api/sips/:id``` - delete a sip (including comments and like on sip)
* ```POST /api/sips/:id/comment``` - create a new comment on a sip

## Coffees
* ```GET /api/coffees``` - get all coffees on Top Rated feed
* ```GET /api/coffees/:id``` - get a single coffee's details

## Shops
* ```GET /api/shops/:id``` - get shop details
