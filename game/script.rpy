# The script of the game goes in this file.

## Dialogue beeps, code courtesy of Ren'Py FAQ
init python:
    def beep(event, **kwargs):
        if event == "show":
            renpy.music.play("music/junggle_blip_edited.mp3", channel="sound", loop = True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

screen object_menu:
    vbox xalign 0.5 yalign 0.66:
        textbutton "[objectcall]" action Null

# BACKGROUNDS
image bg_dark = "backgrounds/bg_dark.png"
image bg_light = "backgrounds/bg_light.png"

# BOXES
image object = "backgrounds/objpopup_gui.png"
image choicegui = "backgrounds/choices_gui.png"


# OBJECTS
image lightoff = "objects/flashlightoff_resize.png"
image lighton = "objects/flashlighton_resize.png"
image jacket = "objects/jacket_resize.png"
image pocket = "objects/pocket_resize.png"
image lint = "objects/lint_resize.png"
image candycane = "objects/candycane_resize.png"
image rollerskates = "objects/rollerskates_resize.png"
image box = "objects/box_resize.png"
image medoil = "objects/medoil_resize.png"
image sweatband = "objects/sweatband_resize.png"
image gameboy = "objects/gameboy_resize.png"
image eyeliner = "objects/eyeliner_resize.png"
image polaroid = "objects/polaroid_resize.png"
image napkin = "objects/pen_resize.png"
image letter = "objects/letter_resize.png"

# CHARACTERS
define j = Character("Juliet", callback=beep)

# ENDINGS
image kelsey = "backgrounds/ending_kelsey.png"
image mom = "backgrounds/ending_mom.png"

# Music
define audio.mothballs_theme = "music/mothballs.mp3"
define audio.rustle = "music/arithni_rustle_edited.mp3"

# The game starts here.

label start:
    # stops main menu music
    stop music fadeout 3.0

    # FAM/ROM COUNTERS
    $ fam = 0
    $ rom = 0

    scene bg_dark

    j "It smells like mothballs.{w} Faintly, though enough to give you a headache if you breathed it in long enough."

    j "Our house was infested with them before.{w} Moths, I mean."

    j "Hiding in our cabinets,{w} in between our food packaging,{w} flittering under the light panels,
       {w}{i}nesting{/i} in my gloves."

    j "I refused to use them after that."

    j "And I guess the fear of my fingers freezing off finally kicked Má and Ba into action."

    j "They brought mothballs home the next day and we sprinkled them all around the house.{w}
       I guess some of those landed in my closet."

    show bg_dark
    with vpunch

    play audio rustle

    j "..."

    j "What is this?"

    #FIRST OBJECT: WINDBREAKER

    show object
    show jacket

    $ objectcall = "PICK IT UP"
    call screen object_menu

    hide jacket
    hide object

    j "Jeez, that scared the hell out of me."

    j "Actually...{w} It {i}is{/i} bit dark in here."

    j "I could’ve sworn I stashed a flashlight somewhere.{w}
       Back when I used to read comics at night."

    j "Boxes and loose items of clothes litter the closet floor."

    j "I’d never cared to rearrange everything after Má stopped her weekly moth inspections.{w}
       But cramped in here now, I’m starting to wish I had."

    j "I sweep my arm around the floor, feeling around for the flashlight."

    j "From what I remember, it should’ve been right...{w} Here!{w} Aha!"

    show object
    show lightoff

    $ objectcall = "TURN IT ON"
    call screen object_menu

    hide lightoff
    hide object

    scene bg_light
    show object
    show lighton

    $ objectcall = "LOOK AWAY"
    call screen object_menu

    hide lighton
    hide object

    j "Oh, god. Too bright."

    ## POST FLASHLIGHT

    show object
    show jacket

    $ objectcall = "INSPECT"
    call screen object_menu

    hide jacket
    hide object

    j "This was actually a hand-me-down from Má.{w}
       She used to sell ones just like it in the little shop her family owned."

    j "They didn’t have the means for education after immigrating here during the war.{w}
       Má says she was lucky she got to go to college."

    j "And that meant Jimmy and I should quit complaining."

    show object
    show pocket

    $ objectcall = "WHAT'S IN HERE?"
    call screen object_menu

    hide pocket
    hide object

    j "I wonder what's left in here.{w}
       I could've sworn I left a—"

    show object
    show lint

    $ objectcall = "EW."
    call screen object_menu

    hide lint
    hide object

    show object
    show candycane

    $ objectcall = "DOUBLE EW."
    call screen object_menu

    hide candycane
    hide object

    j "Tossing the jacket aside, I tug my knees closer to my chest."

    j "It's been ten minutes since I've started hiding out here and I'm surprised no one has barged in."

    j "This may be my room, but my family's always seemed to think they had the right."

    j "But right now, the house is surprisingly quiet.{w} Almost eerie, even."

    j "Only the sound of my breath and the ticking of the clock in the bedroom tell me I haven’t frozen in place."

    j "I lean my head back until the wall catches it, stabilizing me as I stare up at the ceiling."

    j "Something about the darkness of the room hanging over my shoulders calms me."

    j "No distractions here."

    j "Nothing to see, nothing to do."

    j "And when every moment’s rest since the beginning of your life has been policed by your parents?{w}
       Well...{w}
       You learn to appreciate your hiding places."

    j "As strange as a closet may be."

    #NEW SCENE

    scene bg_light

    j "A few minutes pass and still, no one has entered.{w}
       I’m relieved, but… just the slightest bit disappointed."

    j "Footsteps, then the closing of a door.{w}
       Footsteps, then the sound of a sink.{w}
       Footsteps, then the sound of {i}Paris By Night{/i}."

    j "Just a typical Thursday evening with the Quach family."

    j "Except it's not."

    j "Ugh."

    j "A moment passes and nothing changes.{w}
       No one moves toward my room.{w}
       The door doesn’t open."

    j "{i}Why don’t they care--{/i}"

    j "No, I wasn’t expecting anything anyway.{w}
       I’m just here to calm down."

    j "Let’s see what other things I’ve left around here.{w}
       That’ll calm me down."

    ## NEW SCENE WITH MUSIC
    scene bg_light
    play music mothballs_theme fadein 3.0

    j "Rummaging through the boxes--{w}
       as much as I can with a flashlight anyway--{w}
       I find one box in particular that catches my eye."

    show object
    show rollerskates

    $ objectcall = "ADMIRE THEM!"

    hide rollerskates
    hide object

    j "These were my rollerskates from fifth grade.{w}
       I remember..."

    show choicegui

    menu rollerskates_menu:
        "Picking them out with Ba.":
            hide choicegui
            $ fam += 1

            j "Back when Toys R Us was still a thing, Ba and I had gone over to purchase a pair."

            j "It was Teresa's birthday in fifth grade and she was having a party at the local skating rink.{w}
               Somehow I’d managed to nab an invitation.{w}
               But I needed skates."

            j "I’d never ridden before that party.{w}
               And judging from the state of these skates, you can probably tell I never did again."

            j "I’d always liked pink when I was younger.
               And telling your parents you liked anything was an invitation to be bombarded with gifts of that type."

            j "So naturally, Ba picked pink skates. And when I say pink, I mean it was completely covered in
               different shades of hot pink.{w}
               A literal mess."

            j "Thankfully, I had a shred of common sense then and switched it for these.{w}
               Probably saved my social standing then."

            j "Until I fell flat on my ass."

        "Kelsey trying them on.":
            hide choicegui
            $ rom += 1

            j "Kelsey had been a friend.{w}
               She visited a lot during our drama class, and being the nosy kid she is, she found her way into my closet."

            j "My skates had been hiding there, just as they are today.{w}
               Immediately, Kelsey took a liking to them, slipping her foot in and tumbling to the floor within seconds."

            j "She’d looked at me defensively for a second, almost as though she were considering denying it’d
               happened at all."

            j "But we’d both seen her."

            j  "And soon, she laughed.{w}
                Her signature loud and hearty laugh."

            j "And I laughed with her."

            j  "I wondered how someone could radiate such infectious happiness.{w}
               I hoped she could teach me."

    scene bg_light

    j "Putting the skates on the floor, I tug the box beneath them closer to me."

    j "If I’m remembering correctly, this is The Box.{w}
       You know, the most important one."

    show object
    show box

    $ objectcall = "OPEN IT!"
    call screen object_menu

    hide box
    hide object

    j "I open the flaps up, tugging one side up before the other, and soon the contents are revealed to me.{w}
       It’s a mess.{w}
       Much like everything else."

    j "The first thing that gets me is the smell.{w}
       A strong and sinus-clearing odor. It almost hurts from breathing it this close."

    j "I quickly dig through the items with my free hand, looking for the item."

    j "I already know where it’s coming from.{w}
       I spent my whole childhood smelling this.{w}
       Up until the other kids started commenting anyway."

    show object
    show medoil

    $ objectcall = "PICK IT UP!"
    call screen object_menu

    hide medoil
    hide object

    j "Oh no. I guess I didn’t close it all the way.{w}
       It must have dripped in the box from the last time I used this."

    j "The smell lingers in the air now and I wince at its strength."

    j "I remember..."

    show choicegui

    menu dauxanh_menu:
        "Ba rubbing this on our noses":
            hide choicegui
            $ fam += 1

            j "Whenever Ba thought he was starting to get sick, he’d rub this under his nose.{w}
               Even if this was meant for joint paint, he was sure this would cure any problem."

            j "Má always laughed at him as his eyes began to water.{w}
               The strength of the odor would quickly rise to your eyes and burn.{w}
               Similar to those fast-acting eye drops."

            j "I’ve always liked the smell of dầu xanh and I was keen to copy my dad,
               so at some point, I started asking him to wipe some under my nose too."

            j "And there was instant regret."

            j "But something about having that smell on me felt like a warm hug.{w}
               It reminded me of my parents whenever I was in pain or or feeling lonely."

            j "I’d ended up rubbing it on my collarbones before school.{w}
               A good luck charm of sorts."

            j "But the smell is strong and it lingers, and soon I got weird looks from all my classmates."

            j "And I specifically remember Joseph B. shouting at my third grade teacher that I made his nose hurt."

            j "I never wore it outside again.{w}
               Rarely wore it at home."

            j "I think the last time I opened this was two months ago when I’d gotten a nasty bug bite.{w}
               And, as Ba claimed, it worked like a charm."

        "Kelsey rubbing this on our noses":
            hide choicegui
            $ rom += 1

            j "Kelsey is also Vietnamese.{w}
               So she was raised similar to how I was: Paris by Night,
               eating thịt kho for days, and never eating phở at a phở restaurant."

            j "So Kelsey was fairly at home in my home.{w}
               And though my parents thought she was rambunctious, they liked her enough and
               treated her like their own kid."

            j "I’d been complaining about my monologue for our drama class, about how I’d gone over
               the time limit and how unconvincing it was."

            j "And during that time, Kelsey found this bottle on my nightstand and offered it to me,
               claiming it’d fix all my problems."

            j "{i}Hurt?{/i} she’d said.{w}
               {i}Sứt dầu!{/i}"

            j "{i}Failed a test?{/i} {w}
               {i}Sứt dầu!{/i}"

            j "{i}Not a doctor yet?{/i}{w}
               {i}Sứt dầu!{/i}"

            j "That was when I told her how I used it more for comfort than pain.{w}
               (Although rubbing it under my nose often brought about its own pain.)"

            j "And how Ba used to rub it under his nose, though he’d stopped a while ago."

            j "Kelsey quirked an eyebrow at me as if to say, {i}That’s new.{/i}
               And before I knew it, she was smearing it under her nose."

            j "I didn’t have time to stop her before there were tears brimming at the edges of her eyes."

            j "Then in one fluid motion, she’d swiped it beneath mine."

            j "We fell back on my bed, laughing in the midst of our tears.{w}
               Though there were mostly tears."

            j "The stinging was unbearable, but the memories quickly flooded back in."

            j "And as I looked at Kelsey and watched her laugh through the pain, I realized I wanted to be like that too."

            j "{i}Screw the monologue,{/i} I’d said. {i}I’ll find another way to make it up.{/i}"

            j "She'd smiled at me encouragingly, wiping away a tear that’d fallen from the corner of my eye."

            j "And in that moment, I stopped thinking."

            j "I kissed her."

            j "And suddenly, I didn’t know whether I wanted to laugh or cry."

    scene bg_light

    j "I stare at the bottle in my hand a little longer.{w}
       Just having it in my hand now makes me feel a little bit stronger.{w}
       A little less lonely."

    j "But I tuck it safely back in the corner of the box after tightening the cap.{w}
       As comforting as the smell was, it’d be a disaster if it spilled everywhere."

    j "Except it’s too late, I realize."

    show object
    show sweatband

    $ objectcall = "OOF."
    call screen object_menu

    hide sweatband
    hide object

    j "I pick up the dầu-soaked sweatband between my index and thumb fingers, wincing at the overwhelming smell."

    j "This wasn’t even mine.{w}
       How’d it end up in here?"

    j "This belongs to…"

    show choicegui

    menu sweatband_menu:
        "Jimmy":
            hide choicegui
            $ fam += 1

            j "Jimmy, my gym rat brother."

            j "It’s complicated now.{w}
               We tend not to talk most days, working around each other instead of actually interacting."

            j "And it’s weird because we used to be close.{w}
               Until he grew up and decided his friends were more important than our family."

            j "These days, he’s barely even home.{w}
               And I never really talk to him."

            j "When we were younger, he stuck to me like glue.{w}
               We’re only two years apart, so we shared most things."

            j "And with that comes the comparing."

            j "{i}Why can’t you play the piano like Chị?{/i}{w}
               {i}Why can’t you play sports like Em?{/i}{w}
               {i}Why can’t you study like Chị?{/i}{w}
               {i}Why can’t you lose weight like Em?{/i}"

            j "I guess we started to resent each other.{w}
               Just as we did our parents."

            j "So I guess the whole family kind of doesn’t talk.{w}
               Other than the occasional lecture here and there."

            j "I just wished he’d have been by my side.{w}
               After all, wouldn’t we understand each other best?"

        "Kelsey":
            hide choicegui
            $ rom += 1

            j "Kelsey used to be on the track team in high school.{w}
               She said she joined to “differentiate” herself from the other students for college."

            j "Only to realize that all the other Asian students tried to do the same."

            j "But she was good at it, so she stayed.{w}
               And joined again once she got to college."

            j "In the days after the dầu xanh incident, I found myself running away from Kelsey.{w}
               Literally."

            j "In addition to our drama class, we had a track and field class together.{w}
               Kelsey needed an extra two credits, and I…"

            j "I wanted to get my parents off my back about my weight."

            j "Normally, we took our time doing the laps.{w}
               Kelsey could easily go faster but she decided to match my pace."

            j "But I didn’t want to talk to her.{w}
               Or even see her for that matter."

            j "And that was unfair, I know.{w}
               I just…{w}
               Didn’t know what to do."

            j "Kelsey easily caught me.{w}
               Though I suspect she'd let me go several preliminary laps to give me space."

            j "She didn’t say much.{w}
               She just put her sweatband in my hand before jogging ahead."

            j "I didn't put it on right away.{w}
               But after a few minutes of running with it in my hand, I got tired of holding it."

            j "It was weird.{w}
               And not just because of the fact that I was wearing someone else's sweatband."

            j "But once I'd put it on, it felt like support.{w}
               Like she was still running with me,{w} even if she wasn’t beside me."

    scene bg_light

    j "I place the sweatband on the floor outside of the box.{w}
       I should throw it into the wash once I leave."

    j "But the next thing that catches my eye is something I’d begged for for years."

    show object
    show gameboy

    $ objectcall = "TURN IT ON!"
    call screen object_menu

    hide gameboy
    hide object

    j "The screen turns white and the words, “GAME BOY”, appear on the screen with a font that
       reminds me of Microsoft's WordArt and a transition reminiscent of iMovie."

    j "I love it."

    j "But I’m surprised it still has juice.{w}
       Given how long it’s sat in this closet, you would think all its power has been drained."

    j "What game did I leave in here?"

    show choicegui

    menu gameboy_menu:
        "Kirby and the Magic Mirror":
            hide choicegui
            $ fam += 1

            j "The inserted game loads up and it’s the first game Má and Ba got me: {i}Kirby and the Magic Mirror.{/i}"

            j "Kirby was pink so naturally they thought I’d love him."

            j "...{w}"

            j "I did.{w}
               And I also watched his show religiously."

            j "Jimmy and I would wake up early Saturday mornings to watch cartoons."

            j "And while we may not talk too much anymore, this is one thing we still remember fondly:{w}
               {i}Kirby: Right Back at Ya!{/i}"

            j "Our schedule had always been the same.{w}
               Sonic, then Kirby, then Yugi-Oh!{w}
               We watched all three, even if Kirby was the only one we were actually interested in."

            j "It was like clockwork.{w}
               And you didn’t mess with something that was already good."

            j "Naturally, my love for Kirby extended to this game.{w}
               Until I realized I was terrible at it.{w}
               (And all other platformers.)"

            j "Regret sunk deep as I realized this was the only game I had to play on the GameBoy, and I wouldn’t
               have use for it otherwise."

            j "I was anticipating a lecture when Jimmy snuck into my room, asking to borrow the game.{w}
               And it turned out he was far better at it than I ever would be."

            j "Without realizing it, he'd somehow saved the day.{w}
               Má and Ba praised me for sharing, and my GameBoy was going to use."

            j "I still don’t know how that game ends, but as soon as I got other games, I stole my console back
               and put my own hours in."

            j "Just… no more platformers."

        "Harvest Moon":
            hide choicegui
            $ rom += 1

            j "The inserted game loads up and it’s one of the first games I’d picked myself:
               {i}Harvest Moon: More Friends of Mineral Town.{/i}"

            j "Harvest Moon was one of my favorite games.{w}
               There was something calming about being able to live a virtual life that wasn’t anything close to the one you lead."

            j "And I just loved corn.{w}
               So… I wanted to be a farmer at some point in my life."

            j "Kelsey had gotten me into playing a few games.{w}
               One of which was a farming simulator similar to Harvest Moon."

            j "But with Harvest Moon, I’m fairly methodical."

            j "Daily medicinal herbs for Alex.{w}
               Plant this plant on this day of this season.{w}
               Prepare for this event on this day of this year."

            j "So, naturally, I took that mentality into this game."

            j "I quickly overtook Kelsey in hours, skill sets, and money in just a couple of weeks.{w}
               And she looked at me with complete bewilderment."

            j "{i}It’s just a game{/i}, she'd said.
               {i}Just relax.{/i}
               {i}You don’t need to micromanage every part of it.{/i}"

            j "But I wanted to.{w}
               Or rather, I felt I needed to."

            j "I wasn’t good at sports.{w}
               I wasn’t that great at art.{w}
               And once college started, I quickly realized I wasn’t much good academically either."

            j "But this was something that made sense."

            j "I just wanted to be good at something.{w}
               To finally have control of something again."

    scene bg_light

    j "As the title appears, I shut off the game.{w}
       I wasn’t sure where it’d left off last anyway."

    j "I fold the console in half and set it neatly beside the dầu xanh before moving on to the next item."

    show object
    show eyeliner

    $ objectcall = "EXAMINE IT!"
    call screen object_menu

    hide eyeliner
    hide object

    j "I don’t know how this ended up in here.{w}
       I thought I’d lost it."

    j "I ended up buying a new one after searching for a week, but this one was for..."

    show choicegui

    menu eyeliner_menu:
        "My first attempt":
            hide choicegui
            $ fam += 1

            j "I caught onto the trend of eyeliner in middle school."

            j "While I was afraid of looking like a raccoon,
               I was more afraid of the attention that trying out eyeliner would bring me."

            j "And not from my peers--{w}
               as vicious as middle schoolers can be-- {w}
               I just knew the second my parents noticed, they’d comment."

            j "And they did, along with my neverending wealth of relatives."

            j "{i}Điệu quá!{/i}{w}
               {i}Con gái điệu!{/i}"

            j "And despite the playful teasing nature, it always made me feel bad.{w}
               There was a negative quality to it.{w}
               As if caring about my appearance was something worth teasing."

            j "Jimmy had always gotten comments like, {i}đẹp trai{/i}."

            j "But having \"pretty boy\" cooed at you as your aunts pinch your cheeks isn’t
               the same as having them slap your ass and call you vain."

            j "As if being a woman meant being subject to objectification."

            j ":')"

        "My first date":
            hide choicegui
            $ rom += 1

            j "After dancing around the elephant in the room a good month, Kelsey and I found
               what I thought to be a new normal.{w}
               One that didn’t involve talking about our kiss."

            j "But after a week, we found ourselves in the library.{w}
               And soon, Kelsey had shoved all our books aside on the table and stared at me, expectantly."

            j "{i}Let me take you out{/i}, she'd said."

            j "{i}Please{/i}, I'd replied. {i}Just end me before this final{/i}."

            j "I’d known what she’d meant.{w}
               We both knew what we had to talk about.{w}
               But we both knew what was on the line.{w}
               And this was easier."

            j "{i}A date{/i}, she'd emphasized.{w}
               She'd seemed almost exasperated, though I didn't blame her.{w}
               {i}You and me.{/i}{w}
               {i}Romantically.{/i}"

            j "I didn’t have time to react before she was standing and grabbing her things."

            j "{i}If I pass my linear algebra test tomorrow, I’m taking you out.{/i}"

            j "And with that, she shot her fingerguns at me and headed out the door."

            j "I figure she must have had that on her mind for a long time because
               she passed that test with flying colors despite her general grade range of 75."

            j "And before I knew it, I was buying myself some eyeliner and drawing the best wing I’d drawn in years."

            j "But only on one eye."

            j "The other didn't come so easy."

    scene bg_light

    j "I slip the eyeliner back into the box, right beside the other items.{w}
       But the next item that catches my eye…"

    j "Well, I wish I hadn’t seen it."

    show object
    show polaroid

    $ objectcall = "OH..."
    call screen object_menu

    hide polaroid
    hide object

    show choicegui

    # NO COUNT HERE
    menu polaroid_menu:
        "Sneaking around":
            hide choicegui

            j "Kelsey and I started seeing each other.{w}
               Romantically."

            j "We kind of just… fell into it.{w}
               We’d already been seeing so much of each other on the regular that this didn’t feel like a huge change."

            j "It felt right."

            j "I think we both knew there’d been something there.{w}
               We just didn’t know how to do anything about it."

            j "So naturally, spending time with one another was something our parents were already used to."

            j "In their eyes, we were friends.{w}
               No more, no less."

            j "But I remember counting footsteps and waiting for them to fade into the distance before I kissed her."

            j "I remember holding her hand, then tossing it aside as my door slammed open with a question about dinner."

            j "Kelsey always looked at me with a stupid grin, ready to break out into a laugh."

            j "But she always held it in long enough for the door to close again before she let her unruly guffaw escape."

            j "But somehow, simply seeing her laugh always made me laugh too."

            j "It’d start with a playful roll of my eyes, then a growing smile that soon became a full
               grin as I shook my head."

            j "And the more I resisted it, the more she’d laugh until I erupted into laughter of my own."

            j "With how often Kelsey was around, even Jimmy had grown familiar with her."

            j "And being as persistent as Kelsey is, she’d managed to hold a full conversation with him
               each time she came over."

            j "Some nights, she’d stay over."

            j "I figure our parents must’ve thought it strange at first, but they’d gotten to know us
               so well that it didn’t really matter."

            j "I think those nights were the safest moments we had."

            j "Moments where I could properly hold her hand without worrying about my door bursting open."

            j "And moments where I could kiss her without counting footsteps because everyone had gone to bed."

            j "And each time I kissed her, I would swear to myself that this was worth it."

            j "And each time, I’d promise myself that one day we wouldn’t need to sneak around anymore."

        "How it ended":
            hide choicegui

            j "And though the sneaking around was the worst in our homes, it didn’t get much better outside of them."

            j "I was afraid to hold her hand.{w}
               I’d stuff our hands into my jacket’s pockets and hide them between us."

            j "I was afraid of anyone noticing because I was afraid of what they’d say."

            j "Double the catcalling?{w}
               Double the exotification?{w}
               Double the odd looks?"

            j "But truth be told, we got more comments about looking like sisters
               than we did about anything else any time someone commented."

            j "I’d hide behind those assumptions.{w}
               Play the role they’d assumed."

            j "But each time I stayed quiet, I knew Kelsey was hurting inside.{w}
               No matter how much she said she understood."

            j "I knew I was being selfish each time I held my mouth.{w}
               Kelsey would look away, lips pursed with barely a smile on her face."

            j "The rest of those nights were quiet.{w}
               Right up until we got home and laid in our own beds."

            j "That was when my thoughts came to life and guilt spread through my chest."

            j "I was sorry.{w}
               I was always sorry."

            j "I wanted to love her proudly."

            j "I wanted to just love her."

            j "But I couldn't.{w}
               And she deserved better."

    scene bg_light

    j "I set the photo aside away from the rest.{w}
       I don’t want the dầu xanh to spill and ruin the picture."

    j "But the next thing I pull out is quite an oddity.{w}
       And I realize now that I clearly have no sense of organization."

    show object
    show napkin

    $ objectcall = "UM... WHAT?"
    call screen object_menu

    hide napkin
    hide object

    j "What is this doing here?"

    j "This reminds me of..."

    show choicegui

    menu napkin_menu:
        "Taking notes for Má":
            hide choicegui
            $ fam += 1

            j "We still have a landline for whatever reason."

            j "And being as I’ve yet to find a job post-college and I speak considerably better
               Vietnamese than Jimmy, I pick up the calls for the family."

            j "Most notably Má."

            j "Má holds hour long conversations with family members.{w}
               On the regular."

            j "So back when we’d had dial-up, the situation was far from ideal."

            j "But I’ve never properly learnt Vietnamese.{w}
               While I’m able to speak it (enough to save my life, at least), I can’t read or write it--
               aside from the names of food."

            j "I would write notes for her from relatives on the closest sheet of paper we had.{w}
               This tended to be napkins or leftover post-it sheets."

            j "But I remember the day Bà Ngoại passed.{w}
               And I didn’t really know how to write that down.{w}
               Let alone how to spell Ngoại."

            j "Má doesn’t cry often.{w}
               I don’t think I could recall any time prior."

            j "I used to think she just didn’t cry."

            j "But after I broke the news to her that night,{w}
               I realized it was more of a coping mechanism than anything else."

            j "The tears took a full year to stop."

        "That magic trick":
            hide choicegui
            $ rom += 1

            j "We were paired as partners at the beginning of drama class.{w}
               And as an ice breaker, Kelsey promised me a magic trick."

            j "All it involved was a napkin and a pen."

            j "I spent a majority of the time trying to piece together what the magic trick could possibly be,
               rather than actually seeing it."

            j "And by the end of the class, I hadn’t gotten to see it."

            j "Kelsey thought this was funny though and decided to hold out on ever showing me the trick."

            j "She was waiting for me to figure it out, she’d said.{w}
               And after a good month, I still hadn’t."

            j "She was ready to given in then,{w}
               to just show me the trick."

            j "But I’d grown too attached to the idea of figuring it out,{w}
               of proving myself to her,{w}
               that I rejected the offer."

            j "But I still haven’t."

            j "And looking at this napkin now,{w}
               fragile and soft in my fingers,{w}
               worn with time..."

            j "I wonder if I spend too much time trying to figure out how something {i}could{/i} work
               rather than just letting it."

            j "I dismantle so I can piece back together,{w}
               so I can understand."

            j "This was something I never figured out.{w}
               And it's probably too late now."

    scene bg_light

    j "There’s only one thing left in the box now as I set that last item aside."

    j "It’s crumbled, but after the photo, I already think I know what it is."

    j "I’d started writing a letter to Kelsey after it ended.{w}
       Just spilling my mind, my heart, my guts."

    j "I knew I couldn’t talk to her, but I had no one else to talk to."

    j "She was my best friend.{w}
       And there was no one else who knew."

    show object
    show letter

    $ objectcall = "READ IT."
    call screen object_menu

    hide letter
    hide object

    j "{i}Dear Kelsey,{i}"

    j "{i}You are my everything.{/i}"

    j "Ugh.{w}
       Gross."

    j "If only she knew what’s happened now.{w}
       Not even an hour ago."

    j "I fold the letter up with a sigh, tossing it over with the other objects I’d discarded."

    j "I wouldn’t even know where to start if I spoke to her now."

    j "Hey, sorry I broke up with you?"

    j "Hey, sorry I couldn’t handle being gay?"

    j "Hey.{w}
       I just came out to my parents and…{w}
       They’re not taking it so well?"

    j ".{w}
       .{w}
       .{w}"

    j "Neither am I."

    j "It feels like I’m a stranger in my own home."

    j "You know what the first thing they said was?"

    show choicegui

    menu reaction_menu:
        "\"You're brainwashed!\"":
            hide choicegui
            $ fam += 1

            j "{i}Vietnamese people aren’t gay.{/i}{w}
               {i}Gay is an American thing.{/i}{w}
               {i}You watch too much TV.{/i}"

            j "And well, what the hell do I say to that?"

            j "Every time I try to say something, they tell me I’m being rude,{w}
               that I’m talking back to them."

            j "I tried to explain that being gay wasn’t some fad.{w}
               I don’t know why they think we’re so impressionable.{w}
               Especially when they believe everything they read on Facebook."

            j "But they wouldn’t bother listening."

            j "Did your parents say that too when you came out?"

            j "I don’t know why I never asked you that."

        "\"Kelsey was your girlfriend?\"":
            hide choicegui
            $ rom += 1

            j "I told them no.{w}
               I didn’t know if that was something you wanted me to share.{w}
               Even if you were out to everyone else."

            j "I just don’t think this was completely about us anyway.{w}
               My coming out, I mean."

            j "I just wanted them to hear me."

            j "It was so tiring to keep holding that in now that I knew.{w}
               And I knew that had strained our relationship too."

            j "I’m sorry I hesitated so much with you.{w}
               I didn’t mean to."

            j "But somehow fear just consumed me and I couldn’t handle it anymore.{w}
               It felt like I was lying to everyone.{w}
               It felt like I was lying to myself."

            j "I think I just needed some time to grow on my own,{w}
               to learn to be okay with who I am."

            j "I’m sorry that that meant I couldn’t be with you.{w}
               I just… didn’t want to hurt you any more."

    j "It’s been a good forty minutes now.{w}
       And I think it’s nice that they’ve given me space, but…"

    j "It sort of feels like they don’t care at all."

    j "I mean, I did rush out of there right after dinner was over."

    j "But they all just…{w}
       Went back to their routines."

    j "I can hear the keyboard clicking in Jimmy’s room.{w}
       And the TV’s on in the living room."

    j "Do we just move on like it’d never happened?"

    j "Part of me is glad to move on that way, but…{w}
       That means I’d end up back where we started."

    j "And then...{w=1} wouldn’t this all be for nothing?"

    j ".{w}
       .{w}
       .{w}"

    j "Well, I guess I should leave the closet.{w}
       The smell of the mothballs is slowly becoming unbearable, and I’m starting to get a headache."

    j "I'm feeling..."

    show choicegui

    # NO COUNT HERE
    menu feeling_menu:
        "Refreshed.":
            hide choicegui

            j "Refreshed."

            j "It feels like a weight’s been lifted off my shoulders."

            j "And no matter what happens, it’ll be okay.{w}
               I’ll be okay."

            j "I believe in myself, and I know you believe in me too."

        "Terrified.":
            hide choicegui

            j "Terrified… honestly."

            j "Kind of scared of my family being able to see this deep into my soul."

            j "But being vulnerable is the first step in finding new things.{w}
               And well,{w}
               it’s always terrifying to stand up and show people who you are."

    scene bg_light

    j "I’ve grown tired of living like this.{w}
       Hiding in the shadows, flocking toward sources of light."

    j "I want to be the light.{w}
       I want people to feel comfortable coming to me."

    j "I turn off the flashlight and reach up for the doorknob, taking a deep breath just to calm myself for whatever happens next."

    j "But the door opens on its own and the light from my bedroom floods in.{w}
       I’m surprised to see who’s there."

    if fam > rom:
    ## FAMILY ENDING
        scene mom

        j "The first thing Má said had been something about my sitting on the floor."

        j "She said she knew I hadn’t been cleaning it once she stopped checking and threatened to start again."

        j "Just seeing her there yelling at me for something so trivial overwhelmed me."

        j "This just felt so familiar and comfortable.{w}
           Well, relatively."

        j "And I engulfed her in a hug that she slowly gave back."

        j "It took her a moment, but eventually she’d managed to say:"

        j "That I’m her daughter and she loves me.{w}
           That she loves me now and that she would forever."

        j "Nothing would change that."

        j "She offered me some fruit that she and Ba had cut in the kitchen."

        j "Durian."

        j "And now that she’d mentioned it, I could smell it coming into my room.{w}
           The door was wide open, after all, as always."

        j "And even if there were still things to unpack here, this was a place to start."

        j "This is still my home.{w}
           And they will always be."

    else:
    ## ROMANTIC ENDING
        scene kelsey

        j "Kelsey said Má had called her up.{w}
           Said something about needing her help with me."

        j "Má didn’t understand me but she figured Kelsey would be a good step forward.{w}
           That she’d be someone who would."

        j "And Kelsey didn’t need any more convincing."

        j "Two months of moping had been enough for her and it was about time she did something about it anyway.{w}
           She hadn’t been planning to let me go."

        j "I told her I wanted to be more like her."

        j "She’d always called me her butterfly.{w}
           I always joked I was a moth."

        j "But it’s finally time to live up to her expectations.{w}
           Or rather, it’s time to rise my own."

    #scene bg_light

    j "Everyone has told me what I am.{w}
       I’ve never once stopped to think."

    j "Perhaps I’m not a moth."

    j "Perhaps I’ve been a butterfly all along."

    j "And now, It’s finally time to become one.{w}
       To spread my wings and take flight."

    j "I am not plain.{w}
       I am not ugly."

    j "I am healthy.{w}
       I am beautiful."

    j "I am allowed to take up space.{w}
       To live, to breathe, to {i}love{/i}."

    j "And that, I will."

    # This ends the game.

    return
