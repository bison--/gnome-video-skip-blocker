# gnome-video-skip-blocker
blocks the gnome-shell workspace switch brwoser video/youtube chapter skip bug

## WHAT?

There is a bug in gnome-shell that makes using gnome-based linux OSes unusable for me.  
This mitigates it "good enough"

```
When switching workspaces (ctrl+alt+arrow-right) to the right, it skips YouTube video chapters (google chrome and Firefox) when it comes in contact with a playing YouTube video browser.  
When switching to a new empty workspace even when the window with the YouTube video on the second screen it will then trigger this behavior.
```

Bug Reports:
* https://gitlab.gnome.org/GNOME/mutter/-/issues/3889
* https://gitlab.gnome.org/GNOME/gnome-shell/-/issues/8461
* https://bugzilla.redhat.com/show_bug.cgi?id=2372608

Having any window "on top" of the browser/YouTube window catches the focus and prevents the skip-bug propagation from happening.  
**Note:** the "YouTube skip blocker" may be "top most", but when you click in the browser window you actively have to click the "YouTube skip blocker" after wards for them to be not only "top most", but also top in the last active window hierarchy.   
"YouTube skip blocker"

## Installation

**WIP** / for whatever reasons the desktop file doesnt work, yet...  

It only needs Python3.  
* Copy the `gnome-video-skip-blocker.desktop` file to `~/.local/share/applications` (Ubuntu/Fedora) as a template.
* Change the paths (for the icon & main.py) in `gnome-video-skip-blocker.desktop` to wherever the `main.py` is located.
* On Ubuntu / Fedora run: `update-desktop-database ~/.local/share/applications`

You can now start this tool from your Application launcher

## Note

I also added a debug-log for window events. Maybe this helps the gnome team debugging this.

Events when the bug occurs (workspace->right)
```
2025-06-17 08:41:12.988329: Event: 9, Widget: .!toplevel, Details: {'serial': 7525, 'num': '??', 'height': '??', 'keycode': '??', 'state': '??', 'time': '??', 'width': '??', 'x': '??', 'y': '??', 'char': '??', 'send_event': False, 'keysym': '??', 'keysym_num': '??', 'type': <EventType.FocusIn: '9'>, 'widget': <tkinter.Toplevel object .!toplevel>, 'x_root': '??', 'y_root': '??', 'delta': 0}
2025-06-17 08:41:13.066361: Event: 3, Widget: .!toplevel, Details: {'serial': 7555, 'num': '??', 'height': '??', 'keycode': 114, 'state': 28, 'time': 81675922, 'width': '??', 'x': -2936, 'y': -40, 'char': '', 'send_event': False, 'keysym': 'Right', 'keysym_num': 65363, 'type': <EventType.KeyRelease: '3'>, 'widget': <tkinter.Toplevel object .!toplevel>, 'x_root': 2000, 'y_root': 918, 'delta': 0}
2025-06-17 08:41:13.129389: Event: 3, Widget: .!toplevel, Details: {'serial': 7561, 'num': '??', 'height': '??', 'keycode': 64, 'state': 28, 'time': 81675986, 'width': '??', 'x': -2936, 'y': -40, 'char': '', 'send_event': False, 'keysym': 'Alt_L', 'keysym_num': 65513, 'type': <EventType.KeyRelease: '3'>, 'widget': <tkinter.Toplevel object .!toplevel>, 'x_root': 2000, 'y_root': 918, 'delta': 0}
2025-06-17 08:41:13.133074: Event: 3, Widget: .!toplevel, Details: {'serial': 7567, 'num': '??', 'height': '??', 'keycode': 37, 'state': 20, 'time': 81675990, 'width': '??', 'x': -2936, 'y': -40, 'char': '', 'send_event': False, 'keysym': 'Control_L', 'keysym_num': 65507, 'type': <EventType.KeyRelease: '3'>, 'widget': <tkinter.Toplevel object .!toplevel>, 'x_root': 2000, 'y_root': 918, 'delta': 0}
```

Events when the bug doesnt occurs (workspace->left)
```
2025-06-17 08:41:17.501352: Event: 2, Widget: .!toplevel, Details: {'serial': 7573, 'num': '??', 'height': '??', 'keycode': 37, 'state': 16, 'time': 81680357, 'width': '??', 'x': -2936, 'y': -40, 'char': '', 'send_event': False, 'keysym': 'Control_L', 'keysym_num': 65507, 'type': <EventType.KeyPress: '2'>, 'widget': <tkinter.Toplevel object .!toplevel>, 'x_root': 2000, 'y_root': 918, 'delta': 0}
2025-06-17 08:41:17.534907: Event: 2, Widget: .!toplevel, Details: {'serial': 7579, 'num': '??', 'height': '??', 'keycode': 64, 'state': 20, 'time': 81680391, 'width': '??', 'x': -2936, 'y': -40, 'char': '', 'send_event': False, 'keysym': 'Alt_L', 'keysym_num': 65513, 'type': <EventType.KeyPress: '2'>, 'widget': <tkinter.Toplevel object .!toplevel>, 'x_root': 2000, 'y_root': 918, 'delta': 0}
2025-06-17 08:41:18.106961: Event: 10, Widget: .!toplevel, Details: {'serial': 7592, 'num': '??', 'height': '??', 'keycode': '??', 'state': '??', 'time': '??', 'width': '??', 'x': '??', 'y': '??', 'char': '??', 'send_event': False, 'keysym': '??', 'keysym_num': '??', 'type': <EventType.FocusOut: '10'>, 'widget': <tkinter.Toplevel object .!toplevel>, 'x_root': '??', 'y_root': '??', 'delta': 0}
```