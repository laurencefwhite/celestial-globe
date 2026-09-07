# Celestial Globe

An interactive globe of the sky: stars to eighth magnitude, the constellations, the brighter deep-sky
objects, the Sun, Moon and planets with their moons, the larger asteroids and the brighter satellites,
all placed for a chosen observer and moment, with the horizon drawn on the sphere.

**Live:** https://laurencefwhite.github.io/celestial-globe/

## What it does

- **A globe you can turn and zoom**, from the whole sky down to a field a few arcseconds wide. Drag to
  turn it, scroll or pinch to zoom, double-click to zoom in on a point, click an object to fly to it.
- **Two ways of looking at it.** By default you look at the celestial sphere from outside, as at a
  classical celestial globe, so east is to the right. The *From inside* switch turns it inside out, as
  the sky appears from Earth, with east to the left.
- **An observer.** Melbourne to begin with; pick any of 700-odd cities, type a latitude and longitude,
  or use the device's location. The horizon is drawn as a line on the sphere with the cardinal points
  and the zenith marked, the part of the sky below the horizon is shaded, and an altitude–azimuth grid
  can be switched on. The masthead shows the observer's local time, local sidereal time and UTC.
- **Coordinates on labels.** Two switches add altitude and azimuth, or right ascension and declination
  (J2000), under the name of every labelled object. Hovering anything gives both, with magnitude,
  distance, size and phase where they apply.
- **41,000 stars** from the HYG database, coloured by B−V, with IAU proper names and Bayer and
  Flamsteed designations. Fainter stars appear as you zoom in.
- **The 88 constellations**: stick figures, names and the IAU boundaries. The Milky Way is drawn as
  five brightness contours.
- **About 900 deep-sky objects**, the Messier catalogue and the brighter NGC, IC and Collinder
  objects, drawn as icons by type at their real angular size. With *Pictures* on, each object's
  Wikipedia picture is fetched and shown in place of the icon once it would be more than a few
  pixels across.
- **The Sun, Moon and planets** from JPL's approximate elements, within a few arcminutes; the Moon
  from mean elements with the main perturbations, to about three arcminutes, corrected for the
  observer's parallax. The Moon, Mercury, Venus and Mars show their phase with the bright limb
  turned the right way; Saturn's rings are drawn at their real tilt; discs are drawn at their real
  angular size once you are zoomed in far enough to see it.
- **22 planetary moons** at their actual positions: Phobos and Deimos; Io, Europa, Ganymede and
  Callisto; Mimas, Enceladus, Tethys, Dione, Rhea, Titan, Hyperion and Iapetus; Miranda, Ariel,
  Umbriel, Titania and Oberon; Triton and Proteus; Charon. Each orbit is a Kepler ellipse fitted to
  three years of JPL Horizons positions, which puts the Galilean moons within a few arcseconds of
  the ephemeris across 2025–2028.
- **Asteroids and dwarf planets** over a chosen size (100 to 900 km): 247 bodies with elements from
  JPL's Small-Body Database, including Ceres, Vesta, Pallas, Hygiea, Eris, Makemake, Haumea,
  Gonggong, Quaoar, Sedna and Orcus.
- **Satellites** as seen from the observer, propagated with SGP4 from CelesTrak elements: the space
  stations, the brightest hundred-odd, the science missions, or the navigation constellations. Each
  can carry a track across the sky, dashed for the recent past and solid for the minutes ahead, and
  is shown dimmed when it is in Earth's shadow. Elements are refreshed from CelesTrak on each visit
  and a snapshot is embedded for when that is not possible.
- **A time scrubber.** Drag the time and date sliders or press play; *Hold the horizon still* keeps
  the horizon fixed while the sky turns past it.
- **Night vision**: a red-on-black rendering of the whole page, for use at the telescope. The `n`
  key toggles it.
- **Layers you can switch on and off:** stars, star names, star designations, constellation figures,
  names and boundaries, Milky Way, deep-sky objects, Sun, Moon and planets, planetary moons,
  asteroids, pictures, satellites, satellite tracks, horizon, shading below the horizon, horizon
  grid, celestial grid, equator and tropics, ecliptic, galactic equator, the two coordinate labels,
  inside view, hold horizon, slow spin and night vision.

## Running it

Open `index.html` in a browser. That is the whole procedure.

It is a single self-contained file of about 1.3 MB, with the star catalogue and everything else
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
but not nutation, aberration or refraction, so they are good to about a quarter of a degree of arc at
worst, and much better than that above the horizon. Planet positions are from the JPL approximate
Keplerian elements (valid 1800–2050) and land within about two arcminutes for the inner planets and
five for Saturn; Uranus, Neptune and Pluto are within an arcminute. The Moon is within about three
arcminutes. Planetary moons are placed relative to their planet to a few arcseconds within the fitted
span, 2025–2028, and degrade slowly outside it. Asteroid positions are two-body from the epoch
elements and are good to a few arcminutes for the main belt.

## Refreshing the data

`build/build_data.py` rebuilds the data block inside `index.html` from the sources below, downloading
what it needs into `build/cache`. Run it with `--refresh` to fetch new satellite elements and asteroid
elements; the moon orbits are re-fitted from JPL Horizons at the same time.

## Data and credits

| | |
|---|---|
| Stars | [HYG database](https://github.com/astronexus/HYG-Database) v4.1, David Nash, CC BY-SA 4.0 |
| Star names, constellations, deep-sky objects, Milky Way, planetary elements | [d3-celestial](https://github.com/ofrohn/d3-celestial), Olaf Frohn, BSD-3 |
| Planetary moons and asteroids | [JPL Solar System Dynamics](https://ssd.jpl.nasa.gov): Horizons and the Small-Body Database |
| Satellites | [CelesTrak](https://celestrak.org) general perturbations elements |
| Pictures | [Wikipedia](https://en.wikipedia.org), via the page-summary API |
| Cities | Natural Earth populated places, from the sibling world clock |
| Rendering | [d3-geo](https://d3js.org/d3-geo) (ISC) and [satellite.js](https://github.com/shashwatak/satellite-js) (MIT) |

The HYG database carries the Creative Commons Attribution-ShareAlike licence, which requires attribution,
given on the page and here.
