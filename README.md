# Celestial Globe

An interactive globe of the sky: stars to eighth magnitude, the constellations, the brighter deep-sky
objects, the Sun, Moon and planets with their moons, the larger asteroids, the brighter comets, the
meteor radiants and the satellites, all placed for a chosen observer and moment, with the horizon
drawn on the sphere.

**Live:** https://laurencefwhite.github.io/celestial-globe/

## What it does

- **A globe you can turn and zoom**, from the whole sky down to a field a few arcseconds wide. Drag to
  turn it, scroll or pinch to zoom, double-click to zoom in on a point, hover an object for its
  details and click it to fly to it. On a touch screen a tap selects an object and shows its details,
  a second tap (or the card's *Fly to* button) flies there, and a tap on empty sky clears the
  selection; the panels fold into the corners and a tap on the globe folds an open one.
- **Two ways of looking at it.** By default you look at the celestial sphere from outside, as at a
  classical celestial globe: north is up, east is to the right, and the constellations are the mirror
  image of the sky. The *From inside* switch turns it inside out, as the sky appears from Earth, like
  a planisphere held overhead. A chart held overhead depends on which way you face, so a *Facing*
  control puts that direction at the bottom of the screen: facing north (the default south of the
  equator) has south at the top and east on the right, and the Sun crosses from right to left; facing
  south (the default north of the equator) has north at the top and east on the left. In both views
  the horizon is held still by default and the sky turns past it as time runs; switch *Hold the
  horizon still* off to fix the stars instead and let the horizon move.
- **Point the phone at the sky.** On a phone the globe follows wherever the phone is aimed from the
  moment it opens, tilted to match how the phone is held, so the screen shows the patch of sky behind
  it. A **Freeze** pill beside the folded Layers pill holds the sky still while you read it and lets
  it follow again, and the screen is kept awake while you are out under it. Where the browser insists on being
  asked first, as Safari does, the pill reads *Point at sky* until you tap it once.
- **An observer.** Melbourne to begin with; pick any of 700-odd cities, type a latitude and longitude,
  or use the device's location. The horizon is drawn as a line on the sphere with the zenith marked,
  the cardinal points sit just outside the globe (or at the edge of the screen when you are zoomed
  in), the part of the sky below the horizon is shaded, and an altitude–azimuth grid can be switched
  on. The masthead shows the observer's local time, local sidereal time and UTC, the state of the
  twilight, and today's rising and setting of the Sun and Moon.
- **Rise, transit and set** for anything you hover or tap, worked out for the observer's own day:
  when it rises, when it is highest and how high, and when it sets, or that it never rises or never
  sets.
- **Coordinates on labels.** Two switches add altitude and azimuth, or right ascension and declination
  (J2000), under the name of every labelled object. Hovering anything gives both, with magnitude,
  distance, size and phase where they apply.
- **41,000 stars** from the HYG database, coloured by B−V, with IAU proper names and Bayer and
  Flamsteed designations. Each star's card gives its spectral type in words, its distance in light
  years and, for the 1,869 variables, the range it varies over. Fainter stars appear as you zoom in.
- **The 88 constellations**: stick figures, names and the IAU boundaries. The Milky Way is drawn as
  five brightness contours.
- **About 900 deep-sky objects**, the Messier catalogue and the brighter NGC, IC and Collinder
  objects, drawn as icons by type at their real angular size. With *Pictures* on, each object's
  Wikipedia picture is fetched and shown in place of the icon once it would be more than a few
  pixels across.
- **The Sun, Moon and planets** from JPL's approximate elements; the Moon from mean elements with the
  main perturbations, corrected for the observer's parallax. The Moon, Mercury, Venus and Mars show
  their phase with the bright limb turned the right way; Saturn's rings are drawn at their real tilt;
  discs are drawn at their real angular size once you are zoomed in far enough to see it.
- **22 planetary moons** at their actual positions, with the events they make: a moon crossing the
  face of Jupiter or Saturn is drawn dark against the disc, its shadow as a black dot beside it, and
  a moon behind the planet or inside its shadow is not drawn at all. The card says which is happening.
- **Asteroids and dwarf planets** over a chosen size (100 to 900 km): 247 bodies with elements from
  JPL's Small-Body Database, including Ceres, Vesta, Pallas, Hygiea, Eris, Makemake, Haumea,
  Gonggong, Quaoar, Sedna and Orcus.
- **104 comets** that come within reach of a small telescope, drawn with a coma and a tail turned away
  from the Sun whose length stands for the brightness. Fainter ones appear as you zoom in.
- **The 27 major meteor showers**, with the radiant drawn where it stands on the night shown and sized
  and brightened by the rate the shower is actually running at. That rate is estimated from the peak
  rate and each shower's own published season, so the Quadrantids are a spike a day wide and the
  Taurids a plateau lasting weeks, rather than both being treated the same. A shower still a
  fortnight off is drawn faintly with the days to its peak. The card gives the peak date for that
  year, the rate overhead now, what you would actually see once the radiant's height is allowed for
  (nothing at all while it is below the horizon), the rate at its best, the speed of the meteors,
  the comet or asteroid the debris came from, and a warning when the Moon is up to spoil it.
- **Satellites** as seen from the observer, propagated with SGP4 from CelesTrak elements: the space
  stations, the brightest hundred-odd, the science missions, or the navigation constellations. Each
  can carry a track across the sky, dashed for the recent past and solid for the minutes ahead, and
  is shown dimmed when it is in Earth's shadow. Elements are refreshed from CelesTrak on each visit
  and a snapshot is embedded for when that is not possible.
- **Paths through the stars.** *Paths* draws each moving body's track over the weeks or months around
  the moment shown, with a tick at each month (or each day for the Moon), so retrograde loops and the
  pace of the motion can be read straight off the globe. Hover one body and only its path is drawn.
- **Daylight and twilight.** The sky above the horizon brightens as the Sun climbs through the
  twilights and washes out the fainter stars, and refraction lifts everything near the horizon by up
  to half a degree. Both can be switched off.
- **An eyepiece field circle** at the centre of the view, at binocular, finder or eyepiece sizes, for
  planning what will fit in one look.
- **Time and date scrubbers** under the clocks. The time track runs from midnight to midnight in the
  observer's zone and the date track half a year either side of today, each with a tick at the
  present; arrows step ten minutes or one day (hold to repeat), play runs the clock at about 36
  minutes a second and rolls into the next day at midnight, and the date's play steps a day at a
  time. The day can be a solar day (24 hours, so the Sun and the clock come back to the same place
  and the stars slip a degree westward) or a sidereal day (23 h 56 m 4 s, so the stars come back to
  the same place and the Sun, Moon and planets drift through them). The clocks turn blue when the
  moment shown is in the future and amber when it is in the past; *Now* returns the time of day to
  the present and *Today* returns the date.
- **Search** by name or catalogue number, over stars, constellations, deep-sky objects, planets and
  their moons, asteroids, comets, meteor showers and satellites. Ctrl-F (⌘F on a Mac) opens it, and
  it takes Greek letters spelled out or typed, with or without the spaces: *alpha cen*, *α Cen*,
  *omega centauri*, *M31*, *ngc253*, *ISS*, *25544*.
- **A link back to any view.** The address bar always holds the observer, the moment, the view and
  every layer, and *Copy link* puts it on the clipboard, so a particular sky can be bookmarked or
  handed to someone else.
- **Save the sky as a picture**, captioned with the place and the moment.
- **Reset view, Keys, Copy link and Save image** sit together above the layers. When the sidebar is
  folded away, Reset view and Freeze come out and sit in a row beside the folded pill, running
  towards the middle of the screen, so they land in the same place relative to it whichever corner
  the panel folds into.
- **Night vision**: a red-on-black rendering of the whole page, for use at the telescope. The `n`
  key toggles it. Press `?` for the other keys.

## Running it

Open `index.html` in a browser. That is the whole procedure.

It is a single self-contained file of about 1.7 MB, with the star catalogue and everything else
embedded. Three things come from the network, and each fails quietly rather than breaking the page:

- **Fonts** (Inter and Spectral) from Google Fonts.
- **Satellite elements** from CelesTrak, cached in the browser for six hours. Offline, the embedded
  snapshot is used; satellite positions drift as the elements age, so a snapshot more than a week or
  two old is indicative only.
- **Pictures** from Wikipedia, with the picture URLs cached in the browser for a month. Offline, the
  drawn icons are used instead. Pictures are shown in whatever orientation Wikipedia has them, so a
  galaxy's tilt on the globe is not its real position angle.

## Accuracy

Right ascension and declination are given for J2000. Altitude and azimuth use precession to the date
but not nutation or aberration; refraction is added for display and can be switched off. Planet
positions are from the JPL approximate Keplerian elements (valid 1800–2050) and land within about two
arcminutes for the inner planets and five for Saturn; Uranus, Neptune and Pluto are within an
arcminute. The Moon is within about three arcminutes. Planetary moons are placed relative to their
planet to a few arcseconds within the fitted span, 2025–2028, and degrade slowly outside it. Asteroid
and comet positions are two-body from the epoch elements: good to a few arcminutes for the main belt,
rougher for a comet far from its epoch. Comet brightness comes from each comet's own magnitude law
and is a rough guide only.

Rise, transit and set are found by sampling the body's altitude every ten minutes through the
observer's day and refining each crossing, using the conventional horizon of −50′ for stars and
planets, −0.833° for the Sun's centre and +0.125° for the Moon's. Checked against JPL Horizons for
Melbourne on 7 September 2026, the Sun, Moon and Jupiter all rise and set within a minute of the
ephemeris.

Meteor shower radiants and rates follow the IAU Meteor Data Center shower list and the International
Meteor Organization's working list of visual showers; the radiant is drifted with the Sun's longitude
away from the peak. The rate away from the peak is an estimate, not published data: it falls by a
factor of ten every so many degrees of solar longitude, with that width taken from each shower's own
activity period on the assumption that the season ends where the rate has fallen to a twentieth of
the peak, and the two sides of the peak are treated separately. What you would see is that rate
multiplied by the sine of the radiant's altitude, which assumes a dark, clear sky and an observer
who catches everything.

## Refreshing the data

`build/build_data.py` rebuilds the data block inside `index.html` from the sources below, downloading
what it needs into `build/cache`. Run it with `--refresh` to fetch new satellite elements, asteroid
elements and comet elements; the moon orbits are re-fitted from JPL Horizons at the same time.

## Data and credits

| | |
|---|---|
| Stars | [HYG database](https://github.com/astronexus/HYG-Database) v4.1, David Nash, CC BY-SA 4.0 |
| Star names, constellations, deep-sky objects, Milky Way, planetary elements | [d3-celestial](https://github.com/ofrohn/d3-celestial), Olaf Frohn, BSD-3 |
| Planetary moons, asteroids and comets | [JPL Solar System Dynamics](https://ssd.jpl.nasa.gov): Horizons and the Small-Body Database |
| Meteor showers | [IAU Meteor Data Center](https://www.ta3.sk/IAUC22DB/MDC2022/) and the [IMO](https://www.imo.net) working list |
| Satellites | [CelesTrak](https://celestrak.org) general perturbations elements |
| Pictures | [Wikipedia](https://en.wikipedia.org), via the page-summary API |
| Cities | Natural Earth populated places, from the sibling world clock |
| Rendering | [d3-geo](https://d3js.org/d3-geo) (ISC) and [satellite.js](https://github.com/shashwatak/satellite-js) (MIT) |

The HYG database carries the Creative Commons Attribution-ShareAlike licence, which requires attribution,
given on the page and here.
