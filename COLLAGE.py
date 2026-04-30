import graphics
import os
import time
import GLOBAL_VARS

def create_collage():
    WIDTH = 800
    HEIGHT = 800

    win = graphics.GraphWin("My Window",WIDTH,HEIGHT)
    win.setCoords(0,0, WIDTH, HEIGHT)
    win.setBackground("white")
        
        
    topLeft = graphics.Point(200,600) #images labeled 1
    topRight = graphics.Point(600,600) #images labeled 2
    bottomLeft = graphics.Point(200,200) #images labeled 3
    bottomRight = graphics.Point(600,200) #images labeled 4
    center = graphics.Point (400,400) 

# ---------------- death ------------------
        
    if GLOBAL_VARS.show_youdied:
        youdied_img = graphics.Image(bottomRight, "Images/youdied.png")
        youdied_img.draw(win)
        
# ---------------- "1" images (topLeft)  ------------------

# PATH_BLUE:
    if GLOBAL_VARS.show_gotoyour925:
        gotoyour925_img = graphics.Image(topLeft, "Images/gotoyour925.png")
        gotoyour925_img.draw(win)
        
    if GLOBAL_VARS.show_smithbed:
        smithbed_img = graphics.Image(topLeft, "Images/smithbed.png")
        smithbed_img.draw(win)
        
    if GLOBAL_VARS.show_compasscafe:
        compasscafe_img = graphics.Image(topLeft, "Images/compasscafe.png")
        compasscafe_img.draw(win)
        
# PATH_PINK:

    if GLOBAL_VARS.show_major:
        major_img = graphics.Image(topLeft, "Images/major.png")
        major_img.draw(win)
   
    if GLOBAL_VARS.show_doneforday:
        doneforday_img = graphics.Image(topLeft, "Images/doneforday.png")
        doneforday_img.draw(win)
       
    if GLOBAL_VARS.show_sportspractice:
        sportspractice_img = graphics.Image(topLeft, "Images/sportspractice.png")
        sportspractice_img.draw(win)  

# PATH_GREEN:
       
    if GLOBAL_VARS.show_stealfromcc:
        stealfromcc_img = graphics.Image(topLeft, "Images/stealfromcc.png")
        stealfromcc_img.draw(win)  
       
    if GLOBAL_VARS.show_minisquirreltable:
        minisquirreltable_img = graphics.Image(topLeft, "Images/minisquirreltable.png")
        minisquirreltable_img.draw(win)  
       
    if GLOBAL_VARS.show_starve:
        starve_img = graphics.Image(topLeft, "Images/starve.png")
        starve_img.draw(win)  
    
        
# ---------------- "2" images (topRight) ------------------

# PATH_BLUE:
    if GLOBAL_VARS.show_creativewriting:
        creativewriting_img = graphics.Image(topRight, "Images/creativewriting.png")
        creativewriting_img.draw(win)
        
    if GLOBAL_VARS.show_organicchem:
        organicchem_img = graphics.Image(topRight, "Images/organicchem.png")
        organicchem_img.draw(win)
        
    if GLOBAL_VARS.show_major:
        major_img = graphics.Image(topRight, "Images/major.png")
        major_img.draw(win)
        
    if GLOBAL_VARS.show_yourbed:
        yourbed_img = graphics.Image(topRight, "Images/yourbed.png")
        yourbed_img.draw(win)
        
    if GLOBAL_VARS.show_learningcommons:
        learningcommons_img = graphics.Image(topRight, "Images/learningcommons.png")
        learningcommons_img.draw(win)
        
    if GLOBAL_VARS.show_alumnaegym:
        alumnaegym_img = graphics.Image(topRight, "Images/alumnaegym.png")
        alumnaegym_img.draw(win)
        
    if GLOBAL_VARS.show_latte:
        latte_img = graphics.Image(topRight, "Images/latte.png")
        latte_img.draw(win)
        
    if GLOBAL_VARS.show_dirtychai:
        dirtychai_img = graphics.Image(topRight, "Images/dirtychai.png")
        dirtychai_img.draw(win)
        
    if GLOBAL_VARS.show_icedtealemon:
        icedtealemon_img = graphics.Image(topRight, "Images/icedtealemon.png")
        icedtealemon_img.draw(win)
   
# PATH_PINK:
    if GLOBAL_VARS.show_stirfry:
        stirfry_img = graphics.Image(topRight, "Images/stirfry.png")
        stirfry_img.draw(win)

    if GLOBAL_VARS.show_CCdinner:
        CCdinner_img = graphics.Image(topRight, "Images/CCdinner.png")
        CCdinner_img.draw(win)

    if GLOBAL_VARS.show_troots:
        troots_img = graphics.Image(topRight, "Images/troots.png")
        troots_img.draw(win)

    if GLOBAL_VARS.show_rowing:
        rowing_img = graphics.Image(topRight, "Images/rowing.png")
        rowing_img.draw(win)
        
    if GLOBAL_VARS.show_xc:
        xc_img = graphics.Image(topRight, "Images/xc.png")
        xc_img.draw(win)
    
    if GLOBAL_VARS.show_fieldhockey:
        fieldhockey_img = graphics.Image(topRight, "Images/fieldhockey.png")
        fieldhockey_img.draw(win)
        
    if GLOBAL_VARS.show_noclass:
        noclass_img = graphics.Image(topRight, "Images/noclass.png")
        noclass_img.draw(win)

# PATH_GREEN:

    if GLOBAL_VARS.show_stealfromretailtable:
        stealfromretailtable_img = graphics.Image(topRight, "Images/stealfromretailtable.png")
        stealfromretailtable_img.draw(win)

    if GLOBAL_VARS.show_studentworker:
        studentworker_img = graphics.Image(topRight, "Images/studentworker.png")
        studentworker_img.draw(win)

    if GLOBAL_VARS.show_runfromCC:
        runfromCC_img = graphics.Image(topRight, "Images/runfromCC.png")
        runfromCC_img.draw(win)

    if GLOBAL_VARS.show_hissatthem:
        hissatthem_img = graphics.Image(topRight, "Images/hissatthem.png")
        hissatthem_img.draw(win)

    if GLOBAL_VARS.show_unbotheredbreakfast:
        unbotheredbreakfast_img = graphics.Image(topRight, "Images/unbotheredbreakfast.png")
        unbotheredbreakfast_img.draw(win)

    if GLOBAL_VARS.show_huntthemall:
        huntthemall_img = graphics.Image(topRight, "Images/huntthemall.png")
        huntthemall_img.draw(win)

    if GLOBAL_VARS.show_afterhoursnurse:
        afterhoursnurse_img = graphics.Image(topRight, "Images/afterhoursnurse.png")
        afterhoursnurse_img.draw(win)

    if GLOBAL_VARS.show_coolydicker:
        coolydicker_img = graphics.Image(topRight, "Images/coolydicker.png")
        coolydicker_img.draw(win)

    if GLOBAL_VARS.show_girlfriendfirstaidpack:
        girlfriendfirstaidpack_img = graphics.Image(topRight, "Images/girlfriendfirstaidpack.png")
        girlfriendfirstaidpack_img.draw(win)





# ---------------- "3" images (bottomLeft) ------------------

# PATH_BLUE:

    if GLOBAL_VARS.show_shakespearedeath:
        shakespearedeath_img = graphics.Image(bottomLeft, "Images/shakespearedeath.png")
        shakespearedeath_img.draw(win)
        
    if GLOBAL_VARS.show_aspirindeath:
        aspirindeath_img = graphics.Image(bottomLeft, "Images/aspirindeath.png")
        aspirindeath_img.draw(win)
        
    if GLOBAL_VARS.show_KpopDanceClub:
        KpopDanceClub_img = graphics.Image(bottomLeft, "Images/KpopDanceClub.png")
        KpopDanceClub_img.draw(win)
        
    if GLOBAL_VARS.show_Ceramics:
        Ceramics_img = graphics.Image(bottomLeft, "Images/Ceramics.png")
        Ceramics_img.draw(win)
        
    if GLOBAL_VARS.show_Frisbee:
        Frisbee_img = graphics.Image(bottomLeft, "Images/Frisbee.png")
        Frisbee_img.draw(win)
        
    if GLOBAL_VARS.show_sleepthroughday:
        sleepthroughday_img = graphics.Image(bottomLeft, "Images/sleepthroughday.png")
        sleepthroughday_img.draw(win)
        
    if GLOBAL_VARS.show_boogeyman:
        boogeyman_img = graphics.Image(bottomLeft, "Images/boogeyman.png")
        boogeyman_img.draw(win)
        
    if GLOBAL_VARS.show_maze:
        maze_img = graphics.Image(bottomLeft, "Images/maze.png")
        maze_img.draw(win)
        
    if GLOBAL_VARS.show_foodfight:
        foodfight_img = graphics.Image(bottomLeft, "Images/foodfight.png")
        foodfight_img.draw(win)
        
    if GLOBAL_VARS.show_Jerry:
        Jerry_img = graphics.Image(bottomLeft, "Images/Jerry.png")
        Jerry_img.draw(win)
    

# PATH_PINK:
 
    if GLOBAL_VARS.show_millriver:
        millriver_img = graphics.Image(bottomLeft, "Images/millriver.png")
        millriver_img.draw(win)
    
    if GLOBAL_VARS.show_Umass:
        Umass_img = graphics.Image(bottomLeft, "Images/Umass.png")
        Umass_img.draw(win)
        
    if GLOBAL_VARS.show_dunkin:
        dunkin_img = graphics.Image(bottomLeft, "Images/dunkin.png")
        dunkin_img.draw(win)
   
    if GLOBAL_VARS.show_trampled:
        trampled_img = graphics.Image(bottomLeft, "Images/trampled.png")
        trampled_img.draw(win)
    
    if GLOBAL_VARS.show_fallintowater:
        fallintowater_img = graphics.Image(bottomLeft, "Images/fallintowater.png")
        fallintowater_img.draw(win)
    
    if GLOBAL_VARS.show_hitbyball:
        hitbyball_img = graphics.Image(bottomLeft, "Images/hitbyball.png")
        hitbyball_img.draw(win)
  
#     if GLOBAL_VARS.show_cry:
#         cry_img = graphics.Image(bottomLeft, "Images/cry.png")
#         cry_img.draw(win)
        
    if GLOBAL_VARS.show_hungry:
        hungry_img = graphics.Image(bottomLeft, "Images/hungry.png")
        hungry_img.draw(win)
        
    if GLOBAL_VARS.show_full:
        full_img = graphics.Image(bottomLeft, "Images/full.png")
        full_img.draw(win)

# PATH_GREEN:

    if GLOBAL_VARS.show_campo:
        campo_img = graphics.Image(bottomLeft, "Images/campo.png")
        campo_img.draw(win)
  
    if GLOBAL_VARS.show_baristacrush:
        baristacrush_img = graphics.Image(bottomLeft, "Images/baristacrush.png")
        baristacrush_img.draw(win)
  
    if GLOBAL_VARS.show_tripandfall:
        tripandfall_img = graphics.Image(bottomLeft, "Images/tripandfall.png")
        tripandfall_img.draw(win)
  
    if GLOBAL_VARS.show_leavebrideatalter:
        leavebrideatalter_img = graphics.Image(bottomLeft, "Images/leavebrideatalter.png")
        leavebrideatalter_img.draw(win)
  
    if GLOBAL_VARS.show_throupleenergy:
        throupleenergy_img = graphics.Image(bottomLeft, "Images/throupleenergy.png")
        throupleenergy_img.draw(win)
  
    if GLOBAL_VARS.show_jealouspartner:
        jealouspartner_img = graphics.Image(bottomLeft, "Images/jealouspartner.png")
        jealouspartner_img.draw(win)
  
    if GLOBAL_VARS.show_getmarried:
        getmarried_img = graphics.Image(bottomLeft, "Images/getmarried.png")
        getmarried_img.draw(win)
  
    if GLOBAL_VARS.show_dieonhold:
        dieonhold_img = graphics.Image(bottomLeft, "Images/dieonhold.png")
        dieonhold_img.draw(win)
  
    if GLOBAL_VARS.show_diedinER:
        diedinER_img = graphics.Image(bottomLeft, "Images/diedinER.png")
        diedinER_img.draw(win)
  
    if GLOBAL_VARS.show_yourbedgreen:
        yourbedgreen_img = graphics.Image(bottomLeft, "Images/yourbed.png")
        yourbedgreen_img.draw(win)


  




# ---------------- "4" images (bottomRight) ------------------
   
# PATH_BLUE:

    if GLOBAL_VARS.show_dreaming:
        dreaming_img = graphics.Image(bottomRight, "Images/dreaming.png")
        dreaming_img.draw(win)
            
    if GLOBAL_VARS.show_frostbite:
        frostbite_img = graphics.Image(bottomRight, "Images/frostbite.png")
        frostbite_img.draw(win)
            
    if GLOBAL_VARS.show_fight:
        fight_img = graphics.Image(bottomRight, "Images/fight.png")
        fight_img.draw(win)
            
    if GLOBAL_VARS.show_cry:
        cry_img = graphics.Image(bottomRight, "Images/cry.png")
        cry_img.draw(win)
            
 
  
# PATH_PINK:
    if GLOBAL_VARS.show_youdied:
        youdied_img = graphics.Image(bottomRight, "Images/youdied.png")
        youdied_img.draw(win)
            
    if GLOBAL_VARS.show_bearattack:
        bearattack_img = graphics.Image(bottomRight, "Images/bearattack.png")
        bearattack_img.draw(win)
       
    if GLOBAL_VARS.show_smithbedpink:
        smithbed_img = graphics.Image(bottomRight, "Images/smithbed.png")
        smithbed_img.draw(win)
    
    if GLOBAL_VARS.show_pothole:
        pothole_img = graphics.Image(bottomRight, "Images/pothole.png")
        pothole_img.draw(win)

# PATH_GREEN:

    if GLOBAL_VARS.show_youdied:
        youdied_img = graphics.Image(bottomRight, "Images/youdied.png")
        youdied_img.draw(win)

    if GLOBAL_VARS.show_huntforsustinence:
        huntforsustinence_img = graphics.Image(bottomRight, "Images/huntforsustinence.png")
        huntforsustinence_img.draw(win)

    if GLOBAL_VARS.show_rabies:
        rabies_img = graphics.Image(bottomRight, "Images/rabies.png")
        rabies_img.draw(win)

    if GLOBAL_VARS.show_partnerkillsyou:
        partnerkillsyou_img = graphics.Image(bottomRight, "Images/partnerkillsyou.png")
        partnerkillsyou_img.draw(win)

    if GLOBAL_VARS.show_dogkingdom:
        dogkingdom_img = graphics.Image(bottomRight, "Images/dogkingdom.png")
        dogkingdom_img.draw(win)

    if GLOBAL_VARS.show_cupoftea:
        cupoftea_img = graphics.Image(bottomRight, "Images/cupoftea.png")
        cupoftea_img.draw(win)
        
    if GLOBAL_VARS.show_yourbedgreen4:
        yourbedgreen4_img = graphics.Image(bottomRight, "Images/yourbed.png")
        yourbedgreen4_img.draw(win)

# ---------------- death ------------------

    if GLOBAL_VARS.show_bibble:
        Bibble_img = graphics.Image(center, "Images/Bibble.png")
        Bibble_img.draw(win)
        
    win.update()
    time.sleep(10)
    win.close()
    

