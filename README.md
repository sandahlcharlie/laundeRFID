# laundeRFID
A rfid reader that scans clothes to track when they are worn.

## Goals
- I want to make a system where I can scan the clothes I am wearing daily and store the activity.
- I want to make scanning simple, so I want to keep the tag in the same ish spot for tops and bottoms.
- I want to make the rifd reader simple looking and wall mountable
- I want to put the circle tags that have better durablity into pouchs to keep the tags

In the future, maybe a portable one for traveling?

## Equipment
### Scanner
3D Printer
1x RC522
1x ESP32-s3 zero

### Tag
(This is for each item of clothing)
1x pouch (made out of reused fabric)
1x NTAG213 - 14 mm circle

I am thinking of adding them to the right side of my tops and left side of bottoms? Maybe keeping them on the side too for easier scanning?

## Database
### Store What?
- date
- time?
- clothing type
- clothing brand
- price bought
- times worn
- calculated price per wear 

### Future
- a photo of each garment
- 'frequently worn with'
- weather that day

## Program
I want to also make a front end that is simple. I want to have a front page with all the articles of clothing. I want to make it so you can click on each one and see the times worn and cost per wear.

### Future
I would like to be able to sort by brand or type of garment or cost per wear.
