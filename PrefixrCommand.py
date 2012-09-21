import sublime, sublime_plugin
# 
class PrefixrCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        #self.view.insert(edit, 1, "Hello, World!")

        braces = False
        sels = self.view.sel()
        print sels
        index = 0;
        for sel in sels:
            #print self.view.substr(sel)
            index += 1

            lines = self.view.lines(sel)
            print lines
            lineIndex = 0
            for lineRegion in lines:
                insertP = lineRegion.b
                self.view.insert(edit, insertP + lineIndex, str(lineIndex))
                lineIndex += 1 
"""

none  Displays an error dialog to the user.
messageBox(string)  none  Displays a message box to the user.
questionBox(string) bool  Displays a yes / no message box to the user, return True iff they selected yes.
options() Options Returns a reference to the application options.
windows() [Window]  Returns a list of all the open windows.
activeWindow()  Window  Returns the most recently used window.
runCommand(string, <args>)  none  Runs the named ApplicationCommand with the (optional) given arguments.
canRunCommand(string, <args>) none  Returns True iff the command is enabled with the (optional) given arguments
makeCommand(string, <args>) String  Builds a command string from a command name and arguments. This string is suitable to use as an argument to showCompletions().
packagesPath()  String  Returns the base path to the packages.0
installedPackagesPath() String  Returns the path where all the user's *.sublime-package files are.1
getClipboard()  String  Returns the contents of the clipboard.2
setClipboard(string)  none  Sets the contents of the clipboard.3
getMacro()  [String]  Returns the current macro. The macro is represented as a list of commands to run.4
setMacro([string])5
"""
