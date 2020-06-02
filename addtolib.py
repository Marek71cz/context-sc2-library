import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs
import os
 
addon   = xbmcaddon.Addon()
dbtype  = xbmc.getInfoLabel("ListItem.dbtype")

def normalizeName(name):
    name = name.replace(': ', '_')
    name = name.replace(':', '_')
    name = name.replace('*', '.')
    return name

def addMovie(mf):
    originalTitle   = xbmc.getInfoLabel("ListItem.Originaltitle").decode('utf-8')
    originalTitle   = normalizeName(originalTitle)
    year            = xbmc.getInfoLabel("ListItem.Year").decode('utf-8')
    moviePath       = xbmc.getInfoLabel("ListItem.FileNameAndPath")

    dirName = mf + originalTitle + ' (' + year + ')'

    if not xbmcvfs.exists(dirName):
        xbmcvfs.mkdir(dirName)
    strmFileName    = os.path.join(dirName, originalTitle + ' (' + year + ')' + '.strm')
    file            = xbmcvfs.File(strmFileName, 'w')
    file.write(str(moviePath))
    file.close()
    xbmc.executebuiltin('UpdateLibrary(video)')

def addTVShow(tf):
    # ToDo:
    originalTitle   = xbmc.getInfoLabel("ListItem.TVShowTitle").decode('utf-8')
    tvShowTitle     = xbmc.getInfoLabel("ListItem.Title").decode('utf-8')
    tvShowTitle     = normalizeName(tvShowTitle)
    year            = xbmc.getInfoLabel("ListItem.Year").decode('utf-8')
    tvShowPath      = xbmc.getInfoLabel("ListItem.FileNameAndPath")
    seasonsCount    = xbmc.getInfoLabel("ListItem.Property('TotalSeasons')")

    # ToDo: Create Tv Show directory and season subdirectories with episode links
    dirName = tf + tvShowTitle + ' (' + year + ')'
    # xbmcgui.Dialog().ok(dbtype, 'Original title: ' + originalTitle, 'TV Show title: ' + tvShowTitle, 'Seasons count: ' + seasonsCount)


def addItem():
    # Check settings, whether library paths are set up corretly
    if dbtype == 'movie':
        if addon.getSetting("movielFolder") == '':
            addon.openSettings()
        mf = addon.getSetting("movielFolder")
        if mf != '':
            addMovie(mf)

    if dbtype == 'tvshow':
        xbmcgui.Dialog().ok(addon.getLocalizedString(30030), addon.getLocalizedString(30031))
        #if addon.getSetting("tvshowsFolder") == '':
        #    addon.openSettings()
        #tf = addon.getSetting("tvshowsFolder")
        #if tf != '':
        #    addTVShow(tf)
        
        
addItem()