# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
## Description
"""
Construct Cache Table with PySide.GtGui.
"""
#-------------------------------------------------------------------------------

import os, sys
sys.dont_write_bytecode = True

from PySide import QtCore, QtGui

from . import define as Define
reload(Define)


CURRENT_PATH = os.path.driname(__file__)


#-------------------------------------------------------------------------------
# QTreeWidget for displaying Cache List
#-------------------------------------------------------------------------------
class cacheTreeWidget(QtGui.QTreeWidget):
    """docstring for cacheTableView"""

    mouseReleased = QtCore.Signal(QtCore.QPoint)
    keyPressed = QtCore.Signal(QtGui.QKeyEvent)

    def __init__(self, parent):
        super(cacheTableView, self).__init__(parent)
        self._parent = parent
        self.cache_nodes = self.getCacheList()
        self.initSettings()

    def initSettings(self):
        # self.verticalHeader().setVisible(False)
        # self.verticalHeader().setMovable(True)
        # self.horizontalHeader().setResizeMode(QtGui.QHeaderView.Interactive)
        # self.setSortingEnabled(True)
        # self.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        # self.setAlternatingRowColors(True)
        self.model = CacheTableModel()
        self.setModel(self.model)


    def unexpStrPath(self, path):
        cachePath = path + "/file"
        unExpPath = hou.parm(cachePath).unexpandedString()
        return unExpPath

    def env_Analysis(self, path):
        pathParts = path[0].split('/')
        if pathParts[0] == None:
            return "-"
        else:
            return pathParts[0]

#-------------------------------------------------------------------------------
# QTreeWidget for displaying Cache List
#-------------------------------------------------------------------------------
class CacheTableDelegate(QtGui.QStyledItemDelegate):
    """docstring for CacheTableModel"""

    HEADER_SETTING = Define.

    def __init__(self, parent=None):
        super(CacheTableDelegate, self).__init__(parent)

    def paint(self):
        selected = False

        if option.state & QtGui.QStyle.State_Selected:
            selected = True

        name = index.data(QtCore.Qt.BackgroundRole)
        description = index.data(DESCRIPTION_ROLE)



#-------------------------------------------------------------------------------
# EOF
#-------------------------------------------------------------------------------
