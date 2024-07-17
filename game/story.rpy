label story:
    show monika 1a zorder 1 at t11
    stop music fadeout 1.0
    stop voice fadeout 1.0
    stop sound fadeout 1.0
    menu:
        m "English or Türkçe?"
        "Türkçe":
            m "İlk kim hareket ederse o gay."
        "English":
            m "Whoever move first is gay."
    play audio englishorspanish fadein 1.5
    pause 33
    stop music fadeout 1.0
    stop voice fadeout 1.0
    stop sound fadeout 1.0
    menu:
        "Onun kazanmasınımı istersin? Sen mi kazanmalısın?"
        "Ben kazanmalıyım!":
            show monika 1a zorder 1 at h11
            mc "Ben kazandım."
            mc "Haha!!"
            m 1q "Of yaa!"
            m "Ama bir dahakine ben kazanıcağım"
            mc "Hadi bakalım..."
            mc "renpy.delete(monika.chr)"
            hide monika
            m "HayıŔŗñĮ¼»ŧþŀÂŻŕěōì«"
            mc "Nah I'd win"
        "O kazansın.":
            show monika 1k zorder 1 at h11
            play audio yuppie
            m "Yuppie"
            m "Ben kazandım."
            mc "Tebrikler sen kazandın!"
            mc "Ama birdahakine ben kazanacağım!"
            m "Hadi bakalım..."
            mc "renpy.delete(monika.chr)"
            hide monika
            m "HayıŔŗñĮ¼»ŧþŀÂŻŕěōì«"
            mc "Nah I'd win"            
            
