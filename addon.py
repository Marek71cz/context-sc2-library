import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs
import os
 
addon = xbmcaddon.Addon()

def setLibraryPath():
    addon.openSettings()

def addMovie():
    # create directory - original title and year
    originalTitle   = xbmc.getInfoLabel("ListItem.Originaltitle").decode('utf-8')
    year            = xbmc.getInfoLabel("ListItem.Year").decode('utf-8')
    moviePath       = xbmc.getInfoLabel("ListItem.FileNameAndPath")
    dbtype          = xbmc.getInfoLabel("ListItem.dbtype")
    tvshowtitle     = xbmc.getInfoLabel("Container.ShowTitle")

    if dbtype == 'movie':
        dirName = mf + originalTitle + ' (' + year + ')'
    # ToDo: Need to implement TV Shows
    else:
        return

    #if dbtype == 'tvshow':
    #    dirName = tf + tvshowtitle + ' (' + year + ')'

    # xbmcgui.Dialog().ok(dbtype, dirName)

    if not xbmcvfs.exists(dirName):
        xbmcvfs.mkdir(dirName)
    strmFileName    = os.path.join(dirName, originalTitle + ' (' + year + ')' + '.strm')
    file            = xbmcvfs.File(strmFileName, 'w')
    file.write(str(moviePath))
    file.close()
    xbmc.executebuiltin('UpdateLibrary(video)')

# Check settings, whether library paths are set up corretly
if addon.getSetting("movielFolder") == '':
    setLibraryPath()

mf = addon.getSetting("movielFolder")
tf = addon.getSetting("tvshowsFolder")

if mf != '':
    addMovie()
       
