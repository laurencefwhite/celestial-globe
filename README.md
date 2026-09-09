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
- **Five views, and no more.** There are five ways of looking at this and everything else is a
  variant of one of them, so they are five buttons: **Celestial sphere**, **Sky view**,
  **Planisphere**, **Astrolabe**, **Astronomical clock**. The five are also pills down the left edge
  of the screen, and the three chart weights pills down the right, so neither has to be dug out of a
  panel. They sit at the edges when the panels are folded and just inboard of them when they are not,
  which is where the other floating pills already live; on a phone, where an open panel is a sheet
  across the whole screen, they wait until it is folded away. What each fixes and what it leaves to you
  is not arbitrary. A globe from outside is orthographic and mirrored by its nature — that is what a
  sphere seen from without does to the sky — so it has no variants and both menus grey out. The
  other four all have a real choice of layout and can be turned whichever way up you like.

  An astrolabe is stereographic by definition, that being the projection the instrument is built on,
  but equal spacing is worth having on it anyway, because the difference is instructive rather than
  decorative. The ecliptic ring is a circle *only* under stereographic — that is the theorem the
  instrument rests on, and why the ring on a brass rete can be struck with a compass. Under equal
  spacing the same curve comes out an oval, missing a fitted circle by thirteen pixels, and the near
  tropic moves from 159 pixels out to 217: the whole rete changes shape. So the band is struck as an
  arc where it may be and traced where it must be, and the pointers find their feet on it either way.
  What survives the change is the frame: the ecliptic still touches the near tropic at one solstice
  and the rim at the other, to within a thousandth of a pixel under both, because tangency is a fact
  about the sphere and any projection about the pole keeps the tropics as circles.

  Naming them made an old combination vanish, which was worth losing. Looking from inside with the
  globe layout, in the mirrored pairing, *was* the outside view exactly — the same projection, the
  same roll, the same handedness, every visible star in the same pixel, measured. Two names for one
  picture. Turned the other way it was a globe seen from infinity with the handedness of standing
  inside it, which is not a thing. The globe layout now belongs to the globe.

- **Two ways of looking at it.** By default you look at the celestial sphere from outside, as at a
  classical celestial globe: north is up, east is to the right, and the constellations are the mirror
  image of the sky. The *From inside* switch turns it inside out, as the sky appears from Earth, like
  a planisphere held overhead.
- **How the sky is laid out** is a choice, in the inside view. A globe seen from outside crowds at its
  limb, because a sphere does, and that is right for the outside view. From inside there is no sphere
  to look at, only the sky, and crowding the horizon hides the very things that happen there. So the
  inside view uses **stereographic** by default, the projection of planispheres and of Stellarium,
  which keeps constellation shapes true and gives the horizon room: an object 5° up sits 8% of the way
  in from the horizon rather than the 0.4% a globe allows. **Equal spacing** is the alternative, where
  height reads straight off the radius, 5° up being one eighteenth of the way in. Both reach past the
  horizon, so the sky fills the window with the ground beyond the horizon circle rather than stopping
  at a rim, and you can pan anywhere without meeting an edge. The **Globe** layout is there if you want
  the view from infinity inside as well. A chart held overhead depends on which way you face, so a *Facing*
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
- **A planisphere, an astrolabe and an astronomical clock**, one press each. All three are
  instruments rather than views: the
  sky about the pole that stands above you, laid flat inside a rim that bounds the card, with
  everything past the rim simply not there. What makes each one itself is where that rim falls and
  what is drawn inside it.

  The **planisphere** runs out to the farthest point the horizon ever reaches, declination
  90 − |latitude| on the far side of the pole, so every star that ever rises where you are is on the
  one card and the horizon aperture just touches the edge. It is drawn in **azimuthal equidistant**,
  as most modern planispheres are: measuring a real one (a BBC *Sky at Night* card for 50° N) gives a
  horizon aperture whose near edge is 0.43 of its far edge, against 0.40 predicted for equidistant,
  0.23 for stereographic and 0.50 for equal-area. Stereographic keeps the constellation shapes true
  but makes the horizon sky four or five times over-size, which is why the cheap cards give it up;
  switch the projection to stereographic for the older kind. Two scales ring the card. The inner one
  turns with the stars and carries the calendar, each date set at the right ascension the Sun has on
  it; the outer one is fixed to the observer and carries the clock. Today's date lines up against the
  current time on its own, to within the equation of time, which is the real instrument's own error:
  +2 minutes on 7 September, +16 in early November, −11 in early March.

  The **astrolabe** is stereographic by definition — projected from the far celestial pole onto the
  plane of the equator — and stops at the far tropic, declination 23.4° past the equator, because
  that projection sends the opposite pole to infinity and brass has to stop somewhere. The room left
  over carries the **tympan**, the altitude and azimuth circles cut for one latitude and drawn only
  above the horizon, under a **rete** whose ecliptic is a circle offset from the centre, since
  stereographic projection turns every circle on the sphere into a circle on the plate. The limb is
  graduated in hours of hour angle. Change the observer and the tympan is recut, which on a real one
  meant swapping a plate.

  **Planet hands** join them, one for each of the seven, drawn thinner so the Sun and the Moon still
  read as the two a clock is told by, and each carrying its own symbol at the rim. Their colours are
  not the ones the markers use: those are what a body looks like through a telescope, and three of
  them are much the same pale straw. A hand is a line two pixels wide that has to be told from eight
  others at a glance, so each is its planet's colour pushed until it is its own — Mars orange-red,
  Jupiter a banded tan, Saturn pale straw, Uranus cyan, Neptune deep blue, Venus a bright cream,
  Mercury grey. Pluto has no hand, on the grounds that it has no business being there.

  The symbols are drawn with a variation selector to ask for the text form, and checked against a
  private-use codepoint before use: without that, half of them arrive from a colour emoji font and
  sit on the brass like stickers, which is what happened to the zodiac the first time round.

  The **astronomical clock** is the astrolabe with hands, as at Prague. A gilt **sun hand** and a
  **moon hand** run from the pole at the centre out to the rim, each with a bead on it where the body
  actually is, and between them lies the **dragon**: one bar along the line where the Moon's path
  crosses the ecliptic, head at the ascending node and tail at the descending. The dragon is not
  decoration. An eclipse can only happen when the Sun and the Moon are both near that line, so when a
  hand lies along the dragon something is about to be covered up — which is what the clock was for.
  Point at the bar and it says how far the Sun is from the line and whether that is an eclipse season.
  The mean node follows Meeus 47.7 and runs backwards round the sky in 18.6 years; at the total solar
  eclipse of 2 August 2027 it puts the Sun 1.6° from the line, which is why that eclipse is so long,
  and 84.7° away on an ordinary day in May. The hands can be switched on over any of the three from
  *Clock hands* in the Layers panel.

  All three are held square, and none of them can be aimed. An instrument's centre is its pole, its
  rim is a circle of declination and its horizon is cut for one latitude, so dragging it about would
  only take it to pieces. What a drag does instead is what your thumb does to a real planisphere: it
  turns the star disc, and turning the disc is turning time, so the card holds still and the sky runs
  under it. A quarter turn is a quarter of a sidereal day. The arrow keys step the clock the same
  way. Magnified, a card is bigger than the window, so ctrl and drag slides it about — hold still for
  a moment first on a touch screen, since one finger already means turn and two already mean magnify.
  The same gesture slides **any** view, not only a card. In the sky views turning and sliding are two
  different things and both are wanted: turn to bring a part of the sky round, slide to put it
  somewhere else on the screen — clear of an open panel, or centred on the object you are looking at
  rather than on the pole. The slide is capped at rather more than half the short side of the window
  so the sphere cannot be pushed out of sight, and *Reset view* returns it to the middle.
  Magnifying a card works on its own pivot rather than on the point under the cursor, which would
  walk it off its pole.

  One bright index line marks the moment shown. On a planisphere it runs across the calendar ring and
  the clock ring together, which is how you read the date against the time. On an astrolabe it runs
  across the limb, which is graduated in the hours on your clock — mean time on this meridian, with
  the equation of time taken out, or the Sun would read up to a quarter of an hour off its own dial
  through the year. The marks are placed by the same bearing function as the Sun hand, so the Sun
  points at the current time on the ring without either being told about the other: checked at three
  latitudes across a year, it lands within a fifth of a minute. Everything else still works as usual — point at an object for its card, tap to select, scroll
  to magnify. None of them flies into place either: an instrument is picked up, not travelled to.
  Press the lit button again, or Reset view, and it is put down, with every switch it touched — the
  tympan, the rete, the hands, the projection, the way up — put back as it found them.

- **Brass**, on the astrolabe, and on by default there. The instrument is drawn as the thing it is:
  a graduated limb round the edge with its rivets, the **plate** in the mater's womb with the
  altitude and azimuth circles cut into it, a pierced web of brass turning over that, and the rule
  laid across the face to read the hour. That is the real stack, and it is drawn in that order, the
  plate a shade duller and darker than the rete so the piece on top reads as the piece on top.

  How solid the plate is, is yours to set, from a third of the way up to wholly opaque as brass
  really is. Its circles are incised rather than drawn on: the light comes from the upper left, so
  the near wall of a groove is the shadowed one and the far wall catches the light, which puts the
  dark fringe above and the bright one below. Get that the wrong way round and every line reads as a
  raised bead instead of a cut one. The ground below the horizon is darker, as on brass it is the
  part with nothing on it.

  How faint a star has to be before it loses its pointer is yours to set too, from first magnitude to
  fifth, and every star that gets one carries its name: a pointer exists to say which star that is,
  so its label is forced to the head of the queue rather than left to be crowded out. Forced to the
  head of the queue, not exempt from it — *Star names* still governs them, so switching the names off
  leaves the rete's pointers bare like everything else. The rete carries the ecliptic as a broad ring divided
  into its twelve signs, two straight members across the face, a hoop on the celestial equator, and
  a spread of tapering pointers, each ending in a spike on one named star.

  The frame is the real one. The rete's outer ring is the far tropic, and inside it runs a hoop on
  the near tropic; the ecliptic ring is tangent to both, touching the inner hoop at one solstice and
  the rim at the other, which is what makes a cut rete hold together. That tangency is exact here to
  four decimal places of a pixel, because the hoop is cut for the obliquity of the day rather than
  for a rounded 23.44°. A pointer is not a spoke from the middle either: it stands with its foot on
  the edge of whichever member runs nearest its star, sweeps round in an ogee and narrows to a spike,
  which is why on a real instrument the crowd of them along the inside of the outer ring all lean the
  same way.

  A last point of pedantry, since it is a common belief: the rete does not change with latitude. The
  **plate** does — that is why an astrolabe came with a stack of them, one per latitude, and why ours
  is recut whenever you move the observer. The rete changes with the epoch, as precession walks the
  stars, and with whichever stars its maker thought worth naming.

  The ecliptic ring is drawn as a true circular arc rather than as a polygon pretending to be one,
  because under stereographic projection it really is a circle: the theorem that every circle on the
  sphere maps to a circle on the plate is the reason the instrument is built on this projection at
  all, and it is why the ecliptic — tilted to the equator, and so not centred on the pole — comes out
  round but off-centre. The ring here is fitted through three points and checked against seventy-two:
  they land on it to within a ten-thousandth of a pixel, and the Sun, which is on the ecliptic by
  definition, sits on the ring to a thousandth. Under equal spacing the same test is out by ten
  pixels, which is why the brass is offered on the astrolabe and the clock and not on the
  planisphere.

- **Two more rings**, optional, on any of the three cards, and in brass where the card is brass.
  They stack outward from the card's own scale and it shrinks to make room.

  The **degree ring** runs in compass order, north through east. Where zero sits is a menu, and the
  default is north for a reason rather than by preference: on a north-up card the north point lies on
  the meridian, so zero falls where an object transits and the ring reads the hour angle directly,
  with ninety, a hundred and eighty and two hundred and seventy on the quarters. East is offered
  because the limb of a brass astrolabe is commonly divided into four quadrants of ninety from the
  horizontal diameter, which is the historical answer rather than the legible one.

  The **right ascension ring** is the odd one out, and the interesting one. Everything else outside
  the card is fixed to the observer: the hours are a clock, and the degrees go round with them. Right
  ascension belongs to the sky and turns with the stars. Reading one against the other is reading the
  sidereal time. Checked: over three hours 0h moves 45.1 degrees, which is three hours of the sky's
  own turning, while midnight on the clock ring moves a hundredth of a degree.

  With a ring outside the hours, the clock and planet hands reach on to its inner rim rather than
  stopping at the card's edge, since a hand pointing at nothing in particular is no use.

  The degree ring is divided **to the single degree**, three hundred and sixty marks with the fives
  and the tens standing taller, which is as fine as a ring of that width can be ruled and still be
  read. Measured off the rendered limb rather than asserted: the ink round the ring repeats exactly
  360 times, three times more strongly than at any neighbouring count; four pixels out only the
  seventy-two five-degree marks survive, and six and a half pixels out only the thirty-six tens.

- **A diagonal scale**, optionally, on the degree ring. A single degree is far too narrow to
  subdivide across, so the old instrument makers went the other way and used the width of the band:
  the ring is ruled into six concentric arcs and a slanted line runs from each degree mark on the
  inner arc to the next degree mark on the outer. Follow the index in until it meets your arc, and
  read how far along the slant has got — the degree is divided into six, which is **ten minutes of
  arc**. It buys precision out of the depth of the ring rather than out of its circumference, which
  is why every serious brass instrument from the sixteenth century on carries one. The band widens
  from 17 to 37 pixels when it is switched on, and the card draws in to make room.

- **The suspension**, optionally: the three pieces an astrolabe actually hangs from, and each has a
  name because each does a job. The **throne**, or *kursi*, is the scalloped lug standing off the top
  of the mater; the **shackle** is hinged into it; the **ring** passes through the shackle and takes
  the thumb. The point of the arrangement is that it swings freely in two directions, so the
  instrument hangs plumb however it is held — which is the whole basis of measuring an altitude with
  one. It keeps its proportion to the instrument, within reason, and the card gives up 66 pixels of
  radius for it. It belongs to the astrolabe alone: a planisphere is a card and does not hang from
  anything, and a clock is mounted on a wall rather than held up by the thumb. The diagonal scale
  likewise waits for a degree ring to sit in.

- **The hand it is written in.** Brass was cut with a graver by someone trained on letter forms that
  have serifs, and every surviving astrolabe reads that way, so **every letter on the astrolabe and
  the clock** is in a serif face: the numerals on all the rings, the signs of the zodiac, the
  altitudes and azimuths on the tympan, the right ascensions and declinations of the grid, the
  compass points, the names of the lines, and the names of the stars themselves. One hand cut the
  lot, which is what an engraved instrument looks like. The planisphere is a printed modern card and
  keeps the sans face it is actually printed in, and so do the two sky views. Arabic and abjad take
  the Naskh face on any card.

- **A ring of the twelve signs**, which is what a planet hand is read against. The clock comes with
  one; the astrolabe can have one, outside everything else it is wearing.

  **A sign is thirty degrees of ecliptic longitude and it is not thirty degrees of the ring.** The
  card is centred on the celestial pole, so a bearing from the pivot is set by right ascension
  alone, and right ascension runs ahead of and behind ecliptic longitude by turns —
  tan RA = cos ε · tan λ, the reduction to the equator. A sign therefore takes about **27.9°** of the
  ring near the equinoxes and **32.2°** near the solstices, and the only four places the two agree
  are the equinoxes and the solstices themselves. Measured off the drawn ring: Aries 27.90°, Cancer
  32.20°, Libra 27.90°, Capricorn 32.20°, the twelve closing the circle to 360.0000°, and each
  within 0.033° of the closed form. That last thirtieth of a degree is precession, not error: set the
  clock to J2000 and the residual falls to zero, because the page builds the ecliptic in the J2000
  frame and precesses it to the date.

  **The projection makes no difference at all.** Stereographic and equal spacing set the radius of a
  point and never its bearing, so the ring is the same ring under either — measured identical to
  8 parts in 10¹¹ of a degree.

  Every hand lands in the house its own longitude puts it in; measured for the Sun, the Moon and the
  seven planets, all nine agree. The Sun is exact to four decimal places, being on the ecliptic by
  definition. A body off the ecliptic reads out by the right ascension its ecliptic latitude costs,
  which was worst at 1.35° of ring for Mars — under a twentieth of a sign, and only visible within
  that much of a boundary.

- **Numerals**: Western, the Arabic-Indic digits (٠ ١ ٢ ٣), or **abjad**, which is what is really cut
  into a brass astrolabe. Abjad numbers the letters — alif is one, ba two, up to ya for ten, then kaf
  twenty and on by tens to sad ninety, then qaf a hundred and so to ta four hundred — and a number is
  written as the letters that sum to it, largest first. Twenty-five is كه, a hundred and eighty is قف,
  three hundred and thirty is شل. There is no zero, so it is set as a dash. The Mashriqi order is
  used; the Maghrib assigned some of the later letters differently. Every number the test throws at
  it decomposes and sums back to itself.

- **Everything on the rings is cut, not printed.** The hour limb, the degree ring, the right
  ascension ring, the planisphere's calendar and hour scales, and the cardinal points on the tympan
  are all drawn as grooves: a dark stroke offset up and to the left and a light one down and to the
  right, the light coming from the upper left, so the shadowed wall of the groove is the near one.
  The direction matters and was wrong once — with the dark on the low side the marks stand proud
  instead of sinking in, which is exactly what an incised line must not do. Tested by probing the
  pixels either side of a mark: on the north badge the upper wall reads 75 and the lower 95, and six
  of the seven diagonal-scale arcs are dark above and light below.

- **Which way up, and which hand.** Two menus settle the orientation of any chart seen from inside:
  *North at top or bottom*, and *East at right or left*. They are not independent in the way they
  look. A whole-sky chart centred on the pole has only one handedness: going round the horizon N, E,
  S, W runs one way about the zenith when you stand and look up, and the other way in a mirror, and
  no rotation turns one into the other. **North at the bottom with east at the right is the sky as
  you see it**, and so is north at the top with east at the left. The other two pairings are its
  mirror image — which is not wrong, it is exactly what a celestial globe shows, because you are
  outside it looking in, but a card held up to the real sky in that arrangement has the
  constellations back to front. The status line says which of the two you are in whenever you change
  either menu.

  **The sky view opens differently on a phone.** Hold a phone up at the sky and it is a window, not
  a globe: what is on your left has to be drawn on the left, or nothing tracks as you turn round. So
  on a touch screen it opens with north at the top and **east at the left**, which is the unmirrored
  pairing — the sky as you actually see it. On a desktop the chart is on a table rather than held up,
  and it opens mirrored, north at the top with east at the right, which is the readable arrangement
  there. The hemisphere makes no difference to this: the handedness is a property of the pairing
  alone. One tap on *East at right/left* moves between them either way.

  **The three instruments open mirrored**, deliberately: north at the top with east at the right in
  the southern hemisphere, south at the top with east at the left in the northern. That is a choice
  about what reads naturally rather than about what a card does — it puts the direction you are
  facing where a map would put it — and it is made knowing the cost. The cost is exactly one thing:
  the rings run the other way round, so the hours and the zodiac count anticlockwise on screen rather
  than clockwise. Nothing is read wrongly by it. Every mark on every ring is placed by the same
  bearing function as the hands, so the Sun still meets its own hour on the limb whichever way round
  the dial is numbered — measured at 0.12 minutes or better in both arrangements, at four latitudes.
  One click on *East at right/left* returns the unmirrored pairing.
- **A field preview**, which is the view through whatever you are pointing with. Pick a telescope and
  an eyepiece and the rest follows: magnification is the telescope's focal length over the
  eyepiece's, the true field is the eyepiece's apparent field divided by that, the exit pupil is the
  aperture over the magnification, and how faint a star the aperture reaches is the familiar
  2.7 + 5 log D — 6.9 for the naked eye, 11.2 for a 50 mm binocular, 14.2 for a 200 mm. Binoculars
  and finders carry their own field, having no eyepiece to change. The preview draws that field as a
  tangent plane, which is what an eyepiece shows, with only the stars the aperture can actually
  reach, and it says where it is pointed in both right ascension and altitude.

  While the field circle is showing, a double click aims the instrument there as well as flying the
  view to it. On an object it takes the object's own position rather than the pixel under the cursor,
  which matters at low magnification where one pixel is a third of a degree of sky.

  Where it points is its own thing, not the middle of the chart: you can look at the whole sky and
  still have the telescope on one object. A four-way pad slews it, by a whole field, half a field or
  a set number of arcminutes, and the middle button sends it to whatever is selected. What holds it
  there as the clock runs is the tracking. **Sidereal** keeps it on the stars, as a driven mount
  does. **Off** keeps it on the ground instead, and the sky drifts through the field at 15 arcseconds
  a second times the cosine of the declination — the first thing anyone meets at the eyepiece.
  **Locked on** follows a named body, which for the Moon or a comet is not the same as sidereal at
  all: over three hours the Moon leaves a sidereal field entirely.

- **Light, medium and heavy**, since setting thirty switches one at a time to get a clear chart is
  nobody's idea of an evening. **Medium is exactly how the page opens**, so choosing it changes
  nothing, and the other two are a step either side: **light** strips the chart back to what you
  would actually see and name outdoors — stars, their names, the constellation figures, the Milky
  Way, the planets and the horizon — and **heavy** turns on everything the page knows, the three
  optional rings included, so an astrolabe under heavy comes out wearing its degrees, its right
  ascensions and its signs. Only the layers move: the place, the moment, the view and the instrument
  are left alone, as they are by Reset defaults.

- **A view you have just chosen starts square, and so does a reloaded page.** Pressing a view button
  re-seats it — centred, unmagnified, unslid — rather than carrying over whatever you had dragged the
  last one to. The address bar follows the view as you move, which meant a reload put you back
  wherever you happened to have dragged and magnified to; the page now marks the hash it writes
  itself and ignores that mark's view on the way back in. A link **you** copied carries no such mark
  and keeps the view it was copied at, which is the whole point of copying it.

- **A switch that does not apply is greyed, not annotated.** *Clock hands*, *Planet hands* and the
  two outer rings used to carry the words "on a card" under them, which told a reader nothing they
  could act on. They now simply go dim and dead in the views where they mean nothing, which is the
  same information without the footnote.

- **The Layers panel folds.** Each heading takes the run of switches under it and puts them away,
  with a count of what is inside, and what you leave open is remembered. One button at the top opens
  or shuts the lot. It opens with one section showing rather than nine.

- **The four poles, each named in its own colour.** Two coordinate systems cross on the sphere and
  each has a pair of poles, which are the easiest points on it to lose. Alt/az has the **zenith** and
  the **nadir**, marked in the amber of the horizon; RA/dec has the **north** and **south celestial
  poles**, marked in the blue of the celestial grid. Each goes out with the system it belongs to, so
  what is marked is always the frame you have asked to be shown in.

- **Numbers on both grids.** A grid with nothing written on it is a net, not a scale. The
  declinations are named at ±30° and ±60° on the two meridians that face the observer's north and
  south, and the right ascensions every two hours along the equator, so wherever the view is pointed
  at least one of each falls on the screen. The horizon grid names its altitudes up both halves of
  the meridian, above the horizon and below it, and its azimuths in whole degrees sitting just clear
  of the horizon itself — which is what turns the alt/az circles on an astrolabe's tympan from
  decoration into something you can read a bearing off.

- **The celestial grid is yours to set.** An instrument used to switch it off behind you, on the
  reasoning that a tympan carries altitude and azimuth circles rather than a graticule of right
  ascension. True of brass, but this is also a chart, and a switch that turns itself off is worse
  than an anachronism. The instruments no longer touch it.

- **Daylight falls on one side of the world only.** The Sun drowns the stars, but only the ones it
  is shining on. Half the sphere on any chart that shows the whole of it is under your feet, in the
  Earth's own shadow, and the stars there are as bright at noon as at midnight, because it is night
  there. They used to be faded and dropped along with the rest, which put the sky's own daylight on
  the far side of the world. Which side a star is on is one dot product against the zenith, so each
  now takes its own limit, its own size and its own opacity. Measured at a moment with the Sun 47°
  up: above the horizon forty sampled stars drop from a mean of 202 to 146 when daylight is switched
  on, and below it the worst of forty changes by 0.3 of 255, which is the edge of a circle being
  drawn at the same size twice.

  The grids and the great circles are a separate matter and do change tone everywhere, daylight or
  not, so that they keep their contrast against a blue sky; a star sitting on one shares in that,
  which is why the same forty move by 7.8 of 255 with the lines drawn over them. A line that crosses
  the horizon cannot be two colours, so that one stays as it is.

- **Daylight fades the sky, not the lines drawn on it.** The stars, the Milky Way and the
  constellation figures wash out at sunrise, because that is what they do. The grids and the great
  circles are not sky: they are drawn on top of it, like the horizon, and they take their contrast
  from the background, darkening as the sky comes up so they read on blue as well as on black.

- **The clock and the calendar.** *Now* returns to the present. Then two kinds of noon, because they
  are two different things and the gap between them is the point: *Noon* puts the clock on twelve,
  which is an administrative convenience kept by a whole time zone, and *Solar* puts the Sun on the
  meridian, which moves by four minutes for every degree you sit from the middle of that zone and by
  up to a quarter of an hour over the year with the equation of time. In Melbourne in September they
  are seventeen minutes apart, and each button says how far it is from the other.

  The time arrows step ten minutes, or one with ctrl held. The date track reaches a century each way,
  which cannot be evenly divided — a pixel would be four months, and tomorrow would be unpickable —
  and cannot be plainly logarithmic either, today being exactly zero. So it is log-of-one-plus:
  straight through the middle, bending away at both ends. Tomorrow lands ten pixels from the centre,
  next week thirty, next month fifty, next year eighty, a decade a hundred and seventeen, a century a
  hundred and fifty. A day spans ten pixels near today and four ten-thousandths of one at the far
  end, which is the right way round, since nobody scrubbing to 2126 cares which Tuesday. Reaching
  that far ought to be honest as well as usable, so past 1800 or 2050 the date carries a warning: the
  planets come from elements fitted to that window and are an extrapolation outside it, while the
  stars, with precession, and the Sun and Moon hold up far longer.

- **An observer.** Melbourne to begin with; pick any of 700-odd cities, type a latitude and longitude,
  or use the device's location. *Set* sits under both boxes and does whatever was last typed into
  either: a place name that has not been applied yet wins, otherwise the coordinates. The horizon is drawn as a line on the sphere with the zenith marked
  and all eight points of the compass on it, north through north-west, each staying in view by
  moving to the edge of the window when its own bearing goes round the back. The part of the sky
  below the horizon is shaded, and an altitude–azimuth grid can be switched
  on. The masthead shows the observer's local time, local sidereal time and UTC, the state of the
  twilight, and today's rising and setting of the Sun and Moon.
- **The lines answer too.** Point at the horizon, the ecliptic, the celestial equator, a tropic, a
  polar circle, the galactic equator or the meridian and it says what that line is and where on it
  you are pointing. A switch puts their names on the lines themselves.
- **Rise, transit and set** for anything you hover or tap, worked out for the observer's own day:
  when it rises, when it is highest and how high, and when it sets, or that it never rises or never
  sets.
- **Coordinates on labels.** Two switches add altitude and azimuth, or right ascension and declination
  (J2000), under the name of every labelled object. Hovering anything gives both, with magnitude,
  distance, size and phase where they apply.
- **A brightness scrubber** in the key: hold the faintest magnitude wherever you like, from −1 to 8,
  or leave it on Auto to follow the zoom as it always has.
- **Names you can turn off one class at a time**: stars, deep-sky objects, planets, moons, asteroids,
  comets, satellites, meteor showers and the lines each have their own switch, and the switches sit
  in two columns.
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
- **Reset defaults** puts every switch and setting back the way the page opens, and deliberately
  leaves the place you are observing from, the view and the clock alone, since each of those has its
  own control.
- **On a phone** the stars are drawn smaller and far fewer names are shown, both scaled from the
  short side of the window, so a small screen is not covered in labels.
- **Reset view, Reset defaults, Copy link, Save image and Keys** sit together above the layers. When the sidebar is
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
