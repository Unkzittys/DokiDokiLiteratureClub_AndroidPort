python early:
    if renpy.android:
        config.savedir = os.environ['ANDROID_PUBLIC'] + "/DDLC-1454445547"
        config.variants = [ 'pc', 'touch', None ]
        config.gestures = { "n" : "game_menu", "s" : "hide_windows" }

init python:
    if renpy.android:
        import os

        if persistent.android_datamade:
            persistent.android_makedata = False
        else:
            persistent.android_makedata = True

        if persistent.android_makedata:

            if not os.path.exists(os.path.join(os.environ['ANDROID_PUBLIC'])):
                os.mkdir(os.path.join(os.environ['ANDROID_PUBLIC']))
            if not os.path.exists(os.path.join(os.environ['ANDROID_PUBLIC'], "characters")):
                os.mkdir(os.path.join(os.environ['ANDROID_PUBLIC'], "characters"))

            try: file(os.environ['ANDROID_PUBLIC'] + "/characters/monika.chr")
            except: open(os.environ['ANDROID_PUBLIC'] + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
            try: file(os.environ['ANDROID_PUBLIC'] + "/characters/natsuki.chr")
            except: open(os.environ['ANDROID_PUBLIC'] + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
            try: file(os.environ['ANDROID_PUBLIC'] + "/characters/yuri.chr")
            except: open(os.environ['ANDROID_PUBLIC'] + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
            try: file(os.environ['ANDROID_PUBLIC'] + "/characters/sayori.chr")
            except: open(os.environ['ANDROID_PUBLIC'] + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())
            persistent.android_datamade = True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
