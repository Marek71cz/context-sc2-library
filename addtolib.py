import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs
import os
 
addon   = xbmcaddon.Addon()
dbtype  = xbmc.getInfoLabel("ListItem.dbtype")

def setLibraryPath():
    addon.openSettings()

def addMovie():
    # create directory - original title and year
    originalTitle   = xbmc.getInfoLabel("ListItem.Originaltitle").decode('utf-8')
    year            = xbmc.getInfoLabel("ListItem.Year").decode('utf-8')
    moviePath       = xbmc.getInfoLabel("ListItem.FileNameAndPath")

    dirName = mf + originalTitle + ' (' + year + ')'

    # xbmcgui.Dialog().ok(dbtype, dirName)

    if not xbmcvfs.exists(dirName):
        xbmcvfs.mkdir(dirName)
    strmFileName    = os.path.join(dirName, originalTitle + ' (' + year + ')' + '.strm')
    file            = xbmcvfs.File(strmFileName, 'w')
    file.write(str(moviePath))
    file.close()
    xbmc.executebuiltin('UpdateLibrary(video)')

def addTVShow():
    originalTitle   = xbmc.getInfoLabel("ListItem.TVShowTitle").decode('utf-8')
    tvShowTitle     = xbmc.getInfoLabel("ListItem.Title")
    year            = xbmc.getInfoLabel("ListItem.Year").decode('utf-8')
    tvShowPath      = xbmc.getInfoLabel("ListItem.FileNameAndPath")
    seasonsCount    = xbmc.getInfoLabel("ListItem.Property('TotalSeasons')")

    dirName = tf + tvShowTitle + ' (' + year + ')'
    # xbmcgui.Dialog().ok(dbtype, 'Original title: ' + originalTitle, 'TV Show title: ' + tvShowTitle, 'Seasons count: ' + seasonsCount)

    #ToDo: Create Tv Show directory and season subdirectories with episode links

# Check settings, whether library paths are set up corretly
if dbtype == 'movie':
    if addon.getSetting("movielFolder") == '':
        setLibraryPath()
    mf = addon.getSetting("movielFolder")
    if mf != '':
        addMovie()

if dbtype == 'tvshow':
    xbmcgui.Dialog().ok(addon.getLocalizedString(30030), addon.getLocalizedString(30031))
    #if addon.getSetting("tvshowsFolder") == '':
    #    setLibraryPath()
    #tf = addon.getSetting("tvshowsFolder")
    #if tf != '':
    #    addTVShow()