# pyqt-dont-ask-again-dialog-example
PyQt5 dialog which is implementing "don't ask again" checkbox using QSettings

I created this because I thought there might be people who dislike being asked repeatedly whether to run a foreground app in the background or to close it.

This would be used a lot in my app as well :)

## Requirements
* PyQt5 >= 5.14

## Method Overview
Two very vital functions:
* isAskAgainEnabled() - call if you want to know "dont_ask_again" attribute is currently true(enabled) or false
* setMessage(message) - call when you want to change the message displayed in the dialog.

## Preview
![image](https://github.com/yjg30737/pyqt-dont-ask-again-dialog-example/assets/55078043/ac0bb163-6e90-4096-a2f2-ef457efb7922)
