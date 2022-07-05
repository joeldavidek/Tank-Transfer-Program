import tankclass

# List of tanks
tk403 = tankclass.Tank(403, 22, 20.00, 2600, 52000, 0)
tk416 = tankclass.Tank(416, 40, 38.00, 16000, 608000, 0)
tk408 = tankclass.Tank(408, 28, 26.00, 4000, 104000, 0)
tk404 = tankclass.Tank(404, 29, 27.00, 4600, 124200, 0)

tank_info = {"416": tk416.info(), "403": tk403.info(),
             "408": tk408.info(), "404": tk404.info()}


# Available tanks to choose from
availtanks = {"416": tk416.tkgpf, "403": tk403.tkgpf,
              "408": tk408.tkgpf, "404": tk404.tkgpf}


# Current level of tanks
current_tank_levs = {"416": tk416.crtlev,
                     "403": tk403.crtlev, "408": tk408.crtlev, "404": tk404.crtlev}


# Total amount of gallons each tank can hold
tank_max_gal = {"416": tk416.maxgal,
                "403": tk403.maxgal, "408": tk408.maxgal, "404": tk404.maxgal}


# Maximum level in feet that each tank can hold
tank_max_fill = {"416": tk416.tkmax,
                 "403": tk403.tkmax, "408": tk408.tkmax, "404": tk404.tkmax}
