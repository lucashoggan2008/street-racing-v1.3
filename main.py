from random import randint

round_8 = False
race_result = 0
just_raced = False
run = True
level = 1
intake_lv = 0
exhaust_lv = 0
turbo_lv = 0
engine_swap_lv = 0
money_per_win = 1000
money_per_loss = 100
race_count = 0
pounds = 40000000000000000
hp = 60




while run:
    if just_raced:
         home_screen = race_result
    else:
        home_screen = 'none'

    print(f"""
 ______________________________________________
| race count = {race_count}     ${pounds}         {hp}hp                                  
|  street racing                               |
|                                              |
|  Mods - buy mods to get more horse power     |         
|  Race - to race to earn money and get to     |
|           round 8                            |
|  Quit - leave game | last race result:{home_screen}                                                     
|______________________________________________|""")

    if round_8 == True:
        print("you've made it it the final round")



    action = input('>')
    if hp < 100:
        enemy_hp = randint(20, 100)
        level = 1
    if hp >= 100 and hp < 200:
        enemy_hp = randint(100, 200)
        money_per_loss = -200
        money_per_win = 2000
        level = 2
    if hp >= 200 and hp < 400:
        enemy_hp = randint(200, 400)
        money_per_loss = -400
        money_per_win = 4000
        level = 3
    if hp >= 400 and hp < 800:
        enemy_hp = randint(400, 800)
        money_per_loss = -800
        money_per_win = 8000
        level = 4
    if hp >= 800 and hp < 1600:
        enemy_hp = randint(800, 1600)
        money_per_loss = -1600
        money_per_win = 16000
        level = 5
    if hp >= 1600 and hp < 3200:
        enemy_hp = randint(1600, 3200)
        money_per_loss = -3200
        money_per_win = 32000
        level = 6
    if hp >= 3200 and hp < 6400:
        enemy_hp = randint(3200, 6400)
        money_per_loss = -6400
        money_per_win = 64000
        level = 7
    if hp >= 6400:
        enemy_hp = randint(6400, 12800)
        money_per_loss = -12800
        money_per_win = 128000
        level = 8




#racing aspect
    if action == 'race':
        just_raced = True
        race_count = race_count + 1
        if hp >= 6400:
            round_8 = True

        if enemy_hp > hp:
            print("you lost")
            pounds = pounds + money_per_loss
            race_result = 'you lost'
        else:
            print('you won')
            pounds = pounds + money_per_win
            race_result = 'you won'


#mod info
    if action == 'mods':
        print(f"""
         __________________________________________________
        |intake - +20hp -£500 lv{intake_lv}/10             
        |exhaust - +30hp -£700 lv{exhaust_lv}/10           
        |turbo - +200hp -£4000 lv{turbo_lv}/10             
        |enigne swap - +2000hp -£40000 lv{engine_swap_lv}/5
        |__________________________________________________""")

#mod selecter and changes horse power
        mod_selected = input('mod>')
        if mod_selected == 'intake' and pounds >= 500:
            if intake_lv < 10:
                hp = hp + 20
                pounds = pounds - 500
                intake_lv = intake_lv + 1
        if mod_selected == 'exhaust' and pounds >= 700:
            if exhaust_lv < 10:
                hp = hp + 30
                pounds = pounds - 700
                exhaust_lv = exhaust_lv + 1
        if mod_selected == 'turbo' and pounds >= 4000:
            if turbo_lv < 10:
                hp = hp + 200
                pounds = pounds - 4000
                turbo_lv = turbo_lv + 1
        if mod_selected == 'engine swap' and pounds >= 40000:
                if engine_swap_lv < 5:
                    hp = hp + 2000
                    pounds = pounds - 40000
                    engine_swap_lv = engine_swap_lv + 1

#ending code
    if action == 'quit' or pounds < 0:
         run = False