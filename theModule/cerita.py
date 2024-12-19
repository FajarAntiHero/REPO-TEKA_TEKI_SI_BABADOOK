from . import assets as ast

Story1 = "theStory/fullStoryCH1.txt"
Story2 = "theStory/fullStoryCH2.txt"
Story3 = "theStory/fullStoryCH3.txt"
Story4 = "theStory/fullStoryCH4.txt"
Story5 = "theStory/fullStoryCH5.txt"
Story6 = "theStory/fullStoryCH6.txt"

listPathFullStory = [Story1, Story2, Story3, Story4, Story5, Story6]

def story():
    judul = ast.title()
    garis = ast.line()

    for cerita in range(len(listPathFullStory)):
        ast.clearTerminal()
        
        
        print(garis.duaGaris())
        print(judul.storyChapterTitle(cerita + 1))
        print(garis.duaGaris())
        print("")
        ast.openDocument(listPathFullStory[cerita])
        print("")
        print(garis.satuGaris())

        ast.next()
        print(garis.satuGaris())
        ast.jeda(1)